import gym
import numpy as np
import time

NUM_STEPS = 1000000
NUM_ENVS = 31

class RolloutWorker:
    def __init__(self, num_envs):
        self.num_envs = num_envs
        self.env = gym.vector.make("Blackjack-v1", num_envs=num_envs)
        self.env.reset(seed=123)

    def step(self, seeds):
        policies = np.random.default_rng(seeds).integers(0, 2, size=(self.num_envs,))
        observations, rewards, terminated, truncated, info = self.env.step(policies)
        return observations, rewards, terminated, truncated, info

env = RolloutWorker(NUM_ENVS)
start_time = None

for step_num in range(NUM_STEPS):
    if step_num == 1:
        start_time = time.time()
    print(f"Step: {step_num + 1}")
    seeds = np.full(NUM_ENVS, step_num)  # You can customize this as needed
    observations, rewards, terminated, truncated, info = env.step(seeds)
    print(f"Observations={observations}, Rewards={rewards}, Terminated={terminated}")
    print("\n")

end_time = time.time()
print(f"Total time taken: {end_time - start_time:.2f} seconds")
