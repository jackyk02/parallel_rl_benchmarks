import ray
import gym
import numpy as np
import time
import copy

# Initialize Ray without logging.
ray.init()

# Configuration parameters
NUM_ENVS = 30
NUM_EPISODES = 5000


@ray.remote
class RolloutWorker:
    """
    Remote class responsible for managing an individual CartPole environment.
    """

    def __init__(self):
        self.env = gym.make("CartPole-v1")
        self.env.reset(seed=123, options={})

    def collect_episode(self, seed):
        """
        Collects an entire episode of data until termination.
        """
        start_time = time.time()
        policy = np.random.default_rng(seed)
        observations, rewards, terminations = [], [], []

        terminated = False
        while not terminated:
            action = policy.integers(0, 2)
            obs, reward, terminated, truncated, infos = self.env.step(action)
            observations.append(obs)
            rewards.append(reward)
            terminations.append(terminated)

        # Reset environment for next episode
        self.env.reset(seed=123, options={})
        end_time = time.time()
        print(f"Time taken: {(end_time - start_time)*1000:.4f} ms")
        return (observations, rewards, terminations, np.ones(1280000))


# Initialize a list of environment.
envs = [RolloutWorker.remote() for _ in range(NUM_ENVS)]

start_time = time.time()
for episode_num in range(NUM_EPISODES):
    if episode_num == 1:
        start_time = time.time()
    # Collect a full episode from each environment
    episodes = ray.get([env.collect_episode.remote(episode_num)
                       for env in envs])

    print(f"Episode: {episode_num + 1}")

    for i in range(30):
        observations = copy.deepcopy(episodes[i][0])
        print(f"Env {i + 1}: Number of Observations = {len(observations)}")

    print("\n")


end_time = time.time()
# Print the total time taken
print(f"Total time taken: {end_time - start_time:.2f} seconds")

# Shutdown Ray when done.
ray.shutdown()
