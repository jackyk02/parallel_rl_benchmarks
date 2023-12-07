import gym
import numpy as np
import time

NUM_STEPS = 3000
NUM_ENVS = 15


class RolloutWorker:
    def __init__(self, num_envs):
        self.num_envs = num_envs
        env_fns = [lambda: gym.make("Pong-v4") for _ in range(num_envs)]
        self.env = gym.vector.SyncVectorEnv(env_fns)
        self.env.reset()

    def step(self):
        # Generate a list of actions, one for each environment
        actions = [np.random.choice(self.env.single_action_space.n)
                   for _ in range(self.num_envs)]
        observations, rewards, terminated, info = self.env.step(actions)
        return observations, rewards, terminated, info


env = RolloutWorker(NUM_ENVS)
start_time = None

for step_num in range(NUM_STEPS):
    if step_num == 1:
        start_time = time.time()
    print(f"Step: {step_num + 1}")
    observations, rewards, terminated, info = env.step()
    print(
        f"Observations={observations[0][0][0]}, Rewards={rewards[0]}, Terminated={terminated[0]}")
    print("\n")

end_time = time.time()
print(f"Total time taken: {end_time - start_time:.2f} seconds")
