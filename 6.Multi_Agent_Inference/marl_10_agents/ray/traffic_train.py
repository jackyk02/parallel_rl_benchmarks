import gym
import time
import torch
import torch.nn as nn
import torch.optim as optim
from torch.distributions import Categorical
import numpy as np


class PolicyNetwork(nn.Module):
    def __init__(self, obs_space, action_space):
        super(PolicyNetwork, self).__init__()
        # Define your network architecture here
        self.fc = nn.Linear(obs_space, 64)
        self.action_head = nn.Linear(64, action_space)

    def forward(self, x):
        x = torch.relu(self.fc(x))
        action_probs = torch.softmax(self.action_head(x), dim=-1)
        return action_probs


env = gym.make('ma_gym:TrafficJunction10-v1')
n_agents = env.n_agents
policies = [PolicyNetwork(env.observation_space[i].shape[0],
                          env.action_space[i].n) for i in range(n_agents)]
optimizers = [optim.Adam(policy.parameters(), lr=1e-2) for policy in policies]
total_episodes = 100
gamma = 0.99


def train():
    start_time = time.time()
    for episode in range(total_episodes):
        state_n = env.reset()
        done_n = [False] * n_agents
        log_probs = [[] for _ in range(n_agents)]
        rewards = [[] for _ in range(n_agents)]
        total_reward = 0

        while not all(done_n):
            action_n = []
            for i, policy in enumerate(policies):
                state = state_n[i]
                if isinstance(state, list):  # Check if the state is a list
                    state = np.array(state)  # Convert it to a NumPy array

                state = torch.from_numpy(state).float().unsqueeze(0)
                probs = policy(state)
                m = Categorical(probs)
                action = m.sample()
                log_probs[i].append(m.log_prob(action))
                action_n.append(action.item())

            next_state_n, reward_n, done_n, _ = env.step(action_n)

            for i in range(n_agents):
                rewards[i].append(reward_n[i])
                state_n[i] = next_state_n[i]
                total_reward += reward_n[i]

        # Policy Gradient Update after all agents have completed their episode
        for i, policy in enumerate(policies):
            optimizer = optimizers[i]
            R = 0
            policy_loss = []
            returns = []
            for r in rewards[i][::-1]:
                R = r + gamma * R
                returns.insert(0, R)
            returns = torch.tensor(returns)
            for log_prob, R in zip(log_probs[i], returns):
                policy_loss.append(-log_prob * R)
            optimizer.zero_grad()
            policy_loss = torch.cat(policy_loss).sum()
            policy_loss.backward()
            optimizer.step()
            # Clear log probabilities and rewards after updating
            log_probs[i] = []
            rewards[i] = []

        # Print episode number and total reward
        print(
            f"Episode {episode + 1}/{total_episodes}, Total Reward: {total_reward}")

    end_time = time.time()
    print(f"Training time: {end_time - start_time:.2f} seconds")


train()

for i, policy in enumerate(policies):
    policy_save_path = f"policy_agent_{i}.pth"
    torch.save(policy.state_dict(), policy_save_path)
