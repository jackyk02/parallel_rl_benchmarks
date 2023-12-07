import logging
import gym
import torch
import torch.nn as nn
import numpy as np
import time
import ray

ray.init()

logging.basicConfig(filename="infer_log.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


class PolicyNetwork(nn.Module):
    def __init__(self, obs_space, action_space):
        super(PolicyNetwork, self).__init__()
        self.fc = nn.Linear(obs_space, 64)
        self.action_head = nn.Linear(64, action_space)

    def forward(self, x):
        x = torch.relu(self.fc(x))
        action_probs = torch.softmax(self.action_head(x), dim=-1)
        return action_probs


def load_policy(agent_idx):
    policy = PolicyNetwork(
        env.observation_space[agent_idx].shape[0], env.action_space[agent_idx].n)
    policy_load_path = f"policy_agent_{agent_idx}.pth"
    policy.load_state_dict(torch.load(policy_load_path))
    policy.eval()
    return policy


@ray.remote
class PolicyActor:
    def __init__(self, agent_idx):
        self.agent_idx = agent_idx
        self.policy = load_policy(self.agent_idx)

    def get_action(self, state):
        state = torch.from_numpy(
            np.array(state[self.agent_idx])).float().unsqueeze(0)
        with torch.no_grad():
            probs = self.policy(state)
        action = torch.argmax(probs, dim=-1)
        return action.item()


env = gym.make('ma_gym:TrafficJunction4-v1')
n_agents = env.n_agents
actor_handles = [PolicyActor.remote(i) for i in range(n_agents)]
episode = 100000  # Specify the episode you want to run
state_n = env.reset()
done_n = [False] * n_agents
total_reward = 0

start_time = time.time()

for i in range(episode):
    if all(done_n):
        env.reset()
        total_reward = 0
    action_n = [actor.get_action.remote(state_n) for actor in actor_handles]
    action_n = ray.get(action_n)
    next_state_n, rewards, done_n, _ = env.step(action_n)
    state_n = next_state_n

    total_reward += sum(rewards)

    # Log the time every 10,000 episodes
    if i % 10000 == 0 and i != 0:
        elapsed_time = time.time() - start_time
        logging.info(
            f"Episode: {i}, Elapsed Time: {elapsed_time:.2f} seconds")

    # print round number
    print("Episode: "+str(i))

    # print running reward
    print("Reward: " + str(total_reward) + " \n")


print(f"Total Time taken: {time.time()-start_time:.2f} seconds")

ray.shutdown()
