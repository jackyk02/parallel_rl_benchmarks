import gym
import torch
import numpy as np
from numpy.random import RandomState
import ray
import time

# Constants
H = 100  # Number of hidden layer neurons
D = 80 * 80  # Input dimensionality: 80x80 grid
gamma = 0.99  # Discount factor for reward
learning_rate = 1e-4  # Learning rate
batch_size = 3  # Batch size for training
iterations = 1000  # Number of training iterations
SEED = 42  # Seed for reproducibility

# Device configuration
device = torch.device("cpu")

# Set seeds
np.random.seed(SEED)
torch.manual_seed(SEED)


def preprocess(img):
    img = img[35:195]  # Crop
    img = img[::2, ::2, 0]  # Downsample by factor of 2
    img[img == 144] = 0  # Erase background (type 1)
    img[img == 109] = 0  # Erase background (type 2)
    img[img != 0] = 1  # Everything else (paddles, ball) just set to 1
    return img.astype(np.float64).ravel()  # Changed np.float to np.float64


class PolicyNetwork(torch.nn.Module):
    def __init__(self):
        super(PolicyNetwork, self).__init__()
        self.fc1 = torch.nn.Linear(D, H)
        self.fc2 = torch.nn.Linear(H, 1)
        self.relu = torch.nn.ReLU()
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x):
        h = self.relu(self.fc1(x))
        logp = self.fc2(h)
        p = self.sigmoid(logp)
        return p, h


def discount_rewards(r):
    discounted_r = np.zeros_like(r)
    running_add = 0
    for t in reversed(range(0, r.size)):
        if r[t] != 0:
            # Reset the sum, since this was a game boundary (pong specific!)
            running_add = 0
        running_add = running_add * gamma + r[t]
        discounted_r[t] = running_add

    # Standardize the rewards to be unit normal
    discounted_r -= np.mean(discounted_r)
    discounted_r /= np.std(discounted_r)
    return discounted_r


def rollout(policy, env, rs):
    observation = env.reset()
    prev_x = None
    xs, hs, dlogps, rewards = [], [], [], []
    done = False

    while not done:
        cur_x = preprocess(observation)
        x = torch.from_numpy(
            cur_x - prev_x if prev_x is not None else np.zeros(D)).float().to(device)
        prev_x = cur_x

        aprob, h = policy(x)
        action = 2 if rs.uniform() < aprob.item() else 3  # 2 is UP, 3 is DOWN in Pong

        xs.append(x)
        hs.append(h)
        y = 1 if action == 2 else 0
        dlogps.append(y - aprob)

        observation, reward, done, info = env.step(action)
        rewards.append(reward)

    epr = np.vstack(rewards)
    discounted_epr = discount_rewards(epr)
    epdlogp = torch.vstack(dlogps)
    # Modulate the gradient with advantage
    epdlogp *= torch.Tensor(discounted_epr).to(device)
    rewards = np.array(rewards)
    return xs, hs, epdlogp, rewards


ray.init()


@ray.remote
class RolloutWorker(object):
    def __init__(self):
        self.env = gym.make("Pong-v4")
        self.env.seed(SEED)
        self.rs = RandomState(SEED)

    def compute_gradient(self, policy_weights):
        policy = PolicyNetwork().to(device)
        policy.load_state_dict(policy_weights)
        xs, hs, epdlogp, rewards = rollout(policy, self.env, self.rs)

        loss = -torch.cat([h * logp for h, logp in zip(hs, epdlogp)]).sum()
        policy.zero_grad()
        loss.backward()

        total_reward = np.sum(rewards)
        return {k: v.grad.cpu() for k, v in policy.named_parameters()}, total_reward


model = PolicyNetwork().to(device)
optimizer = torch.optim.RMSprop(model.parameters(), lr=learning_rate)
actors = [RolloutWorker.remote() for _ in range(batch_size)]

start_time = time.time()
round_num = 0
running_reward = None

for i in range(1, 1 + iterations):
    model_weights = model.state_dict()
    model_id = ray.put(model_weights)
    gradient_ids = [actor.compute_gradient.remote(
        model_id) for actor in actors]
    reward_sum = 0

    for batch in range(batch_size):
        [grad_id], _ = ray.wait(gradient_ids)
        gradients, reward = ray.get(grad_id)
        reward_sum += reward

        for name, param in model.named_parameters():
            param.grad = gradients[name].to(device)
        optimizer.step()
        optimizer.zero_grad()

    # Update running reward
    running_reward = reward_sum / batch_size if running_reward is None else running_reward * \
        0.99 + (reward_sum / batch_size) * 0.01

    # Check if it's the first round
    if int(round_num) == 0:
        start_time = time.time()

    # Print round number
    print("Round: " + str(round_num))
    round_num += 1

    # Calculate and print elapsed time
    elapsed_time = time.time() - start_time
    print(f"Training time: {elapsed_time:.4f} seconds")

    # Print running reward
    print("Reward: " + str(running_reward) + " \n")

# Close Ray
ray.shutdown()
