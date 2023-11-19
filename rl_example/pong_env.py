import gym
import numpy as np


def policy_forward(weights, x):
    h = np.dot(weights["W1"], x)
    h[h < 0] = 0  # ReLU nonlinearity.
    logp = np.dot(weights["W2"], h)
    # Softmax
    p = 1.0 / (1.0 + np.exp(-logp))
    return p, h


def preprocess(img):
    img = img[35:195]
    img = img[::2, ::2, 0]
    img[img == 144] = 0
    img[img == 109] = 0
    img[img != 0] = 1
    return img.astype(np.float64).ravel()


env = gym.make("Pong-v4")
observation = env.reset()
if isinstance(observation, tuple):
    observation = observation[0]

prev_x = None
xs, hs, dlogps, drs = [], [], [], []

# Define the size of the processed observation (you need to adjust this based on your network architecture)
D = len(preprocess(observation))

# Initialize weights (you need to adjust sizes and values based on your network architecture)
weights = {"W1": np.random.randn(10, D), "W2": np.random.randn(10)}

terminated = truncated = False
while not terminated and not truncated:
    cur_x = preprocess(observation)
    x = cur_x - prev_x if prev_x is not None else np.zeros(D)
    prev_x = cur_x

    aprob, h = policy_forward(weights, x)
    action = 2 if np.random.uniform() < aprob else 3

    xs.append(x)
    hs.append(h)
    y = 1 if action == 2 else 0
    dlogps.append(y - aprob)

    observation, reward, terminated, info = env.step(action)
    drs.append(reward)
