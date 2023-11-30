import gym
import ma_gym
import torch
import torch.nn as nn
import numpy as np
import time

env = gym.make('ma_gym:TrafficJunction10-v1')
n_agents = env.n_agents


class PolicyNetwork(nn.Module):
    def __init__(self, obs_space, action_space):
        super(PolicyNetwork, self).__init__()
        self.fc = nn.Linear(obs_space, 128)
        self.action_head = nn.Linear(128, action_space)

    def forward(self, x):
        x = torch.relu(self.fc(x))
        action_probs = torch.softmax(self.action_head(x), dim=-1)
        return action_probs


def load_policy(agent_idx, episode):
    policy = PolicyNetwork(
        env.observation_space[agent_idx].shape[0], env.action_space[agent_idx].n)
    policy_load_path = f"policy_agent_{agent_idx}_episode_{episode}.pth"
    policy.load_state_dict(torch.load(policy_load_path))
    policy.eval()
    return policy


def inference():
    episode_to_load = 1000  # Load policies trained after 1000 episodes

    policies = [load_policy(i, episode_to_load) for i in range(n_agents)]
    start_time = time.time()  # To measure the total time taken for the episode

    for episode in range(1000):  # You can specify the number of episodes for inference
        state_n = env.reset()
        done_n = [False] * n_agents
        total_reward = 0  # To keep track of the total reward for the episode

        while not all(done_n):
            action_n = []
            for i, policy in enumerate(policies):
                state = state_n[i]
                if isinstance(state, list):
                    state = np.array(state)
                state = torch.from_numpy(state).float().unsqueeze(0)
                with torch.no_grad():
                    probs = policy(state)
                action = torch.argmax(probs, dim=-1)
                action_n.append(action.item())

            next_state_n, rewards, done_n, _ = env.step(action_n)
            state_n = next_state_n

            total_reward += sum(rewards)  # Accumulate the rewards

        end_time = time.time()
        episode_time = end_time - start_time

        print(
            f"Episode {episode + 1} - Total Reward: {total_reward}")
    print(f"Total Time: {episode_time:.2f} seconds")


inference()
