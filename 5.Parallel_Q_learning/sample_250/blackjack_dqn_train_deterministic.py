import time
import gym
import ray
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from collections import deque
from random import sample
import random

# Initialize Ray
ray.init(ignore_reinit_error=True)

# Define the Q-Network


class QNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(QNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)
        self.relu = nn.ReLU()

    def forward(self, state):
        x = self.relu(self.fc1(state))
        x = self.fc2(x)
        return x


# Q-Network and Optimizer (in main process)
device = "cuda" if torch.cuda.is_available() else "cpu"
torch.manual_seed(1)
q_net = QNetwork(3, 32, 2).to(device)
target_net = QNetwork(3, 32, 2).to(device)
target_net.load_state_dict(q_net.state_dict())
target_net.eval()
optimizer = optim.Adam(q_net.parameters(), lr=0.01)


def update_q_network(batch, gamma=0.99):
    torch.manual_seed(1)
    torch.cuda.manual_seed_all(1)

    states, actions, rewards, next_states, dones = zip(*batch)
    states = torch.cat(states).to(device)
    next_states = torch.cat(next_states).to(device)
    actions = torch.tensor(actions).to(device)
    rewards = torch.tensor(rewards, dtype=torch.float32).to(device)
    dones = torch.tensor(dones, dtype=torch.float32).to(device)

    current_q_values = q_net(states).gather(
        1, actions.unsqueeze(-1)).squeeze(-1)
    next_q_values = target_net(next_states).max(1)[0]
    expected_q_values = rewards + gamma * next_q_values * (1 - dones)

    loss = nn.MSELoss()(current_q_values, expected_q_values.detach())

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# Rollout Actor


@ray.remote
class RolloutActor:
    def __init__(self):
        random.seed(1)
        self.env = gym.make("Blackjack-v1")
        self.env.seed(1)
        self.state = self.env.reset()
        self.rng = np.random.RandomState(1)
        self.q_net = QNetwork(3, 32, 2).to("cpu")

    def rollout(self, q_net_state_dict, epsilon=0.1):
        random.seed(1)
        self.q_net.load_state_dict(q_net_state_dict)
        experiences = []

        for _ in range(100):
            state_tensor = torch.from_numpy(
                np.array(self.state)).float().unsqueeze(0)
            if self.rng.uniform(0, 1) < epsilon:
                action = self.rng.randint(0, 2)
            else:
                with torch.no_grad():
                    action = self.q_net(state_tensor).max(1)[1].item()

            next_state, reward, done, _ = self.env.step(action)
            next_state_tensor = torch.from_numpy(
                np.array(next_state)).float().unsqueeze(0)  # Convert to tensor
            # Use tensor here
            experiences.append(
                (state_tensor, action, reward, next_state_tensor, done))

            if done:
                self.state = self.env.reset()
            else:
                self.state = next_state

        return experiences


# Replay Buffer Actor


@ray.remote
class ReplayBufferActor:
    def __init__(self):
        self.experiences = deque(maxlen=20000)

    def manage_experiences(self, new_experiences=None):
        if new_experiences is not None:
            self.experiences.extend(new_experiences)
        return list(self.experiences)[:min(250, len(self.experiences))]


def log_dict_to_file(all_experiences):
    import datetime
    import os
    # Getting the current time to use in the filename
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # File path for logging in the current directory
    file_path = f"all_experiences_{current_time}.txt"

    # Writing the experiences to a file
    with open(file_path, "w") as file:
        for key, value in all_experiences.items():
            file.write(f"{key}: {value}\n")

    return os.path.abspath(file_path)


def log_experiences_to_file(all_experiences):
    import datetime
    import os
    # Getting the current time to use in the filename
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # File path for logging in the current directory
    file_path = f"all_experiences_{current_time}.txt"

    # Writing the experiences to a file
    with open(file_path, "w") as file:
        for experience in all_experiences:
            file.write(f"{experience}\n")

    return os.path.abspath(file_path)


# Training loop
num_actors = 16
rollout_actors = [RolloutActor.remote() for _ in range(num_actors)]
replay_buffer_actor = ReplayBufferActor.remote()
start_time = time.time()
q_net_state = {key: tensor.to("cpu")
               for key, tensor in q_net.state_dict().items()}

for round in range(1000):  # Number of training iterations
    random.seed(1)
    futures = [actor.rollout.remote(q_net_state) for actor in rollout_actors]
    experiences = ray.get(futures)

    all_experiences = [exp for actor_exp in experiences for exp in actor_exp]
    # log_experiences_to_file(all_experiences)
    batch = ray.get(
        replay_buffer_actor.manage_experiences.remote(all_experiences))

    if batch:
        update_q_network(batch)

    q_net_state = {key: tensor.to("cpu")
                   for key, tensor in q_net.state_dict().items()}

    print(q_net_state["fc1.weight"][5])

    if round % 10 == 0:  # Update target network every 10 rounds
        target_net.load_state_dict(q_net.state_dict())

    print(f"Round {round}, Training Time: {time.time()-start_time:.2f}s")


log_dict_to_file(q_net_state)
