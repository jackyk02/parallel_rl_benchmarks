import gym
import numpy as np
import time

NUM_STEPS = 1000000

class RolloutWorker:
    """
    Class responsible for managing an individual CartPole environment.
    """

    def __init__(self):
        self.env = gym.make("Blackjack-v1")
        self.env.reset(seed=123, options={})

    def step(self, seed):
        """
        Takes a step in the environment using a random policy based on the provided seed.
        """
        policy = np.random.default_rng(seed)
        result = self.env.step(policy.integers(0, 2))

        if result[2] or result[3]:
            self.env.reset(seed=123, options={})

        return result


env = RolloutWorker()
start_time = None

for step_num in range(NUM_STEPS):
    if step_num == 1:
        start_time = time.time()
    print(f"Step: {step_num + 1}")
    new_observations, reward, terminated, truncated, info = env.step(step_num)
    print(
        f"Observations={new_observations}, Reward={reward}, Terminated={terminated}")
    print("\n")

end_time = time.time()
# Print the total time taken
print(f"Total time taken: {end_time - start_time:.2f} seconds")
