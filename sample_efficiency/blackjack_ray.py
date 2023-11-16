import ray
import gym
import numpy as np
import time

# Initialize Ray without logging.
ray.init(configure_logging=False, log_to_driver=False)

# Configuration parameters
NUM_ENVS = 31
NUM_STEPS = 1000000


@ray.remote
class RolloutWorker:
    """
    Remote class responsible for managing an individual CartPole environment.
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


# Initialize a list of environment.
envs = [RolloutWorker.remote() for _ in range(NUM_ENVS)]
start_time = None

for step_num in range(NUM_STEPS):
    if step_num == 1:
        start_time = time.time()

    # Perform a step in each environment using the current step number as seed
    results = ray.get([env.step.remote(step_num) for env in envs])
    print(f"Step: {step_num + 1}")

    for i, (new_observations, reward, terminated, truncated, info) in enumerate(results):
        print(
            f"Env {i + 1}: Observations={new_observations}, Reward={reward}, Terminated={terminated}")
    print("\n")

end_time = time.time()
# Print the total time taken
print(f"Total time taken: {end_time - start_time:.2f} seconds")

# Shutdown Ray when done.
ray.shutdown()
