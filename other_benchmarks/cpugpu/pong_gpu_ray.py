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
batch_size = 16  # Batch size for training
iterations = 1000  # Number of training iterations
SEED = 42  # Seed for reproducibility

# Set seeds
np.random.seed(SEED)
torch.manual_seed(SEED)


def preprocess(img):
    img = img[35:195]  # Crop
    img = img[::2, ::2, 0]  # Downsample by factor of 2
    img[img == 144] = 0  # Erase background (type 1)
    img[img == 109] = 0  # Erase background (type 2)
    img[img != 0] = 1  # Everything else (paddles, ball) just set to 1
    return img.astype(np.float64).ravel()


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


def rollout(policy, env, rs, device, state):
    prev_x = None
    xs, hs, dlogps, rewards = [], [], [], []
    done = False

    for i in range(10):
        if done:
            state = env.reset()

        cur_x = preprocess(state)
        x = torch.from_numpy(
            cur_x - prev_x if prev_x is not None else np.zeros(D)).float().to(device)
        prev_x = cur_x

        aprob, h = policy(x)
        action = 2 if rs.uniform() < aprob.item() else 3  # 2 is UP, 3 is DOWN in Pong

        xs.append(x)
        hs.append(h)
        y = 1 if action == 2 else 0
        dlogps.append(y - aprob)

        state, reward, done, info = env.step(action)

        rewards.append(reward)

    epr = np.vstack(rewards)
    discounted_epr = discount_rewards(epr)
    epdlogp = torch.vstack(dlogps)
    # Ensure this tensor is on GPU
    epdlogp *= torch.Tensor(discounted_epr).to(device)
    rewards = np.array(rewards)
    return xs, hs, epdlogp, rewards, state


ray.init()


@ray.remote
class RolloutWorker(object):
    def __init__(self):
        self.env = gym.make("Pong-v4")
        self.env.seed(SEED)
        self.rs = RandomState(SEED)
        self.policy = PolicyNetwork().to("cpu")
        self.state = self.env.reset()

    def collect_trajectories(self, policy_weights):
        self.policy.load_state_dict(policy_weights)
        xs, hs, dlogps, rewards, self.state = rollout(
            self.policy, self.env, self.rs, "cpu", self.state)
        discounted_epr = discount_rewards(np.vstack(rewards))
        return xs, hs, dlogps, discounted_epr, np.sum(rewards)


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = PolicyNetwork().to(device)
optimizer = torch.optim.RMSprop(model.parameters(), lr=learning_rate)
actors = [RolloutWorker.remote() for _ in range(batch_size)]

start_time = time.time()
round_num = 0
running_reward = None

for i in range(1, 1 + iterations):
    model_weights_cpu = {k: v.to("cpu") for k, v in model.state_dict().items()}
    model_id = ray.put(model_weights_cpu)
    trajectory_ids = [actor.collect_trajectories.remote(
        model_id) for actor in actors]
    reward_sum = 0
    all_xs, all_hs, all_dlogps, all_discounted_epr = [], [], [], []

    for batch in range(batch_size):
        [trajectory_id], _ = ray.wait(trajectory_ids)
        xs, hs, dlogps, discounted_epr, rewards = ray.get(trajectory_id)
        all_xs.extend(xs)
        all_hs.extend(hs)
        all_dlogps.extend(dlogps)
        all_discounted_epr.extend(discounted_epr)
        reward_sum += rewards

    all_xs = torch.stack(all_xs).to(device)
    all_hs = torch.stack(all_hs).to(device)
    all_dlogps = torch.stack(all_dlogps).squeeze().to(device)
    all_discounted_epr = torch.tensor(
        np.array(all_discounted_epr), dtype=torch.float32).to(device)

    # Ensure all_dlogps has the same shape as all_hs for element-wise multiplication
    all_dlogps = all_dlogps.view(-1, 1).expand_as(all_hs)

    # Calculate loss
    weighted_log_probs = (all_hs * all_dlogps).sum(dim=1)
    loss = -(weighted_log_probs * all_discounted_epr).sum()

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    print(
        f'Episode {i}: Average Reward: {reward_sum/batch_size:.2f}')
    print(
        f"Training Time: {time.time() - start_time:.2f} seconds" + " \n")

# Close Ray
ray.shutdown()
