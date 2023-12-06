import time
import gym
import ray
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from collections import deque
from torch.distributions import Categorical

# Initialize Ray
ray.init(ignore_reinit_error=True)


# Define the Policy Network
class PolicyNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(PolicyNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)  # Additional layer
        self.relu = nn.ReLU()
        self.softmax = nn.Softmax(dim=1)

    def forward(self, state):
        x = self.relu(self.fc1(state))
        x = self.fc2(x)
        action_probs = self.softmax(x)
        return action_probs


# Policy Network and Optimizer (in main process)
device = "cuda" if torch.cuda.is_available() else "cpu"
policy_net = PolicyNetwork(3, 32, 2).to(device)
optimizer = optim.Adam(policy_net.parameters(), lr=0.01)


def update_policy_network(batch):
    if batch is None:
        return
    state_tensors, actions, rewards = zip(*batch)

    state_tensors = torch.cat(state_tensors).to(device)
    actions = torch.tensor(actions).to(device)
    rewards = torch.tensor(rewards, dtype=torch.float32).to(device)

    action_probs = policy_net(state_tensors)
    action_log_probs = torch.log(action_probs + 1e-8)

    selected_log_probs = action_log_probs[torch.arange(
        action_log_probs.size(0)), actions]
    loss = -torch.sum(selected_log_probs * rewards)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()


# Rollout Actor
@ray.remote
class RolloutActor:
    def __init__(self):
        self.env = gym.make("Blackjack-v1")
        self.state = self.env.reset()
        self.policy_net = PolicyNetwork(3, 32, 2).to("cpu")

    def rollout(self, policy_net_state_dict):
        # Adjust dimensions as per the environment
        self.policy_net.load_state_dict(policy_net_state_dict)
        experiences = []

        for _ in range(10):
            state_tensor = torch.from_numpy(
                np.array(self.state)).float().unsqueeze(0)
            action_probs = self.policy_net(state_tensor).detach().numpy()
            action = np.random.choice(2, p=action_probs.ravel())

            next_state, reward, done, _ = self.env.step(action)
            experiences.append((state_tensor, action, reward))

            if done:
                self.state = self.env.reset()
            else:
                self.state = next_state

        return experiences

# Replay Buffer Actor


@ray.remote
class ReplayBufferActor:
    def __init__(self):
        self.experiences = deque(maxlen=10000)

    def manage_experiences(self, new_experiences=None):
        if new_experiences is not None:
            self.experiences.extend(new_experiences)
        return list(self.experiences)[:5000]


# Training loop
num_actors = 16
rollout_actors = [RolloutActor.remote() for _ in range(num_actors)]
replay_buffer_actor = ReplayBufferActor.remote()
start_time = time.time()
policy_net_state = {key: tensor.to("cpu")
                    for key, tensor in policy_net.state_dict().items()}

for round in range(10000):  # Number of training iterations
    futures = [actor.rollout.remote(policy_net_state)
               for actor in rollout_actors]
    experiences = ray.get(futures)

    all_experiences = [exp for actor_exp in experiences for exp in actor_exp]
    batch = ray.get(
        replay_buffer_actor.manage_experiences.remote(all_experiences))

    # Perform learning if a sufficient batch is available
    if batch:
        print(len(batch))
        update_policy_network(batch)

    policy_net_state = {key: tensor.to('cpu')
                        for key, tensor in policy_net.state_dict().items()}

    print(f"Round {round}, Training Time: {time.time()-start_time:.2f}")
