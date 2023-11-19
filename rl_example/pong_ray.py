import gym
import time
import ray
import numpy as np
import os
import random

os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"


H = 200  # The number of hidden layer neurons.
gamma = 0.99  # The discount factor for reward.
decay_rate = 0.99  # The decay factor for RMSProp leaky sum of grad^2.
D = 80 * 80  # The input dimensionality: 80x80 grid.
learning_rate = 1e-4  # Magnitude of the update.

SEED = 42
np.random.seed(SEED)
random.seed(SEED)
os.environ["PYTHONHASHSEED"] = str(SEED)


def preprocess(img):
    # Crop the image.
    img = img[35:195]
    # Downsample by factor of 2.
    img = img[::2, ::2, 0]
    # Erase background (background type 1).
    img[img == 144] = 0
    # Erase background (background type 2).
    img[img == 109] = 0
    # Set everything else (paddles, ball) to 1.
    img[img != 0] = 1
    return img.astype(np.float64).ravel()


def process_rewards(r):
    """Compute discounted reward from a vector of rewards."""
    discounted_r = np.zeros_like(r)
    running_add = 0
    for t in reversed(range(0, r.size)):
        # Reset the sum, since this was a game boundary (pong specific!).
        if r[t] != 0:
            running_add = 0
        running_add = running_add * gamma + r[t]
        discounted_r[t] = running_add
    return discounted_r


def rollout(model, env):
    """Evaluates env and model until the env returns "Terminated" or "Truncated".

    Returns:
        xs: A list of observations
        hs: A list of model hidden states per observation
        dlogps: A list of gradients
        drs: A list of rewards.

    """
    # Reset the game.
    observation = env.reset()
    if isinstance(observation, tuple):
        # Extract the observation array if it's a tuple.
        observation = observation[0]
    # Note that prev_x is used in computing the difference frame.
    prev_x = None
    xs, hs, dlogps, drs = [], [], [], []
    terminated = False
    while not terminated:
        cur_x = preprocess(observation)
        x = cur_x - prev_x if prev_x is not None else np.zeros(D)
        prev_x = cur_x

        aprob, h = model.policy_forward(x)
        # Sample an action.
        action = 2 if np.random.uniform() < aprob else 3

        # The observation.
        xs.append(x)
        # The hidden state.
        hs.append(h)
        y = 1 if action == 2 else 0  # A "fake label".
        # The gradient that encourages the action that was taken to be
        # taken (see http://cs231n.github.io/neural-networks-2/#losses if
        # confused).
        dlogps.append(y - aprob)

        observation, reward, terminated, info = env.step(action)

        # Record reward (has to be done after we call step() to get reward
        # for previous action).
        drs.append(reward)
    return xs, hs, dlogps, drs


class Model(object):
    """This class holds the neural network weights."""

    def __init__(self):
        np.random.seed(SEED)
        self.weights = {}
        np.random.seed(seed=100)
        self.weights["W1"] = np.random.randn(H, D) / np.sqrt(D)
        self.weights["W2"] = np.random.randn(H) / np.sqrt(H)
        np.random.seed(seed=None)

    def policy_forward(self, x):
        h = np.dot(self.weights["W1"], x)
        h[h < 0] = 0  # ReLU nonlinearity.
        logp = np.dot(self.weights["W2"], h)
        # Softmax
        p = 1.0 / (1.0 + np.exp(-logp))
        # Return probability of taking action 2, and hidden state.
        return p, h

    def policy_backward(self, eph, epx, epdlogp):
        """Backward pass to calculate gradients.

        Arguments:
            eph: Array of intermediate hidden states.
            epx: Array of experiences (observations).
            epdlogp: Array of logps (output of last layer before softmax).

        """
        dW2 = np.dot(eph.T, epdlogp).ravel()
        dh = np.outer(epdlogp, self.weights["W2"])
        # Backprop relu.
        dh[eph <= 0] = 0
        dW1 = np.dot(dh.T, epx)
        return {"W1": dW1, "W2": dW2}

    def update(self, grad_buffer, rmsprop_cache, lr, decay):
        """Applies the gradients to the model parameters with RMSProp."""
        for k, v in self.weights.items():
            g = grad_buffer[k]
            rmsprop_cache[k] = decay * rmsprop_cache[k] + (1 - decay) * g ** 2
            self.weights[k] += lr * g / (np.sqrt(rmsprop_cache[k]) + 1e-5)


def zero_grads(grad_buffer):
    """Reset the batch gradient buffer."""
    for k, v in grad_buffer.items():
        grad_buffer[k] = np.zeros_like(v)


ray.init()


@ray.remote
class RolloutWorker(object):
    def __init__(self):
        np.random.seed(SEED)
        self.env = gym.make("Pong-v4")
        self.env.seed(SEED)

    def compute_gradient(self, model):
        start_time = time.time()
        # Compute a simulation episode.
        xs, hs, dlogps, drs = rollout(model, self.env)
        reward_sum = sum(drs)
        # Vectorize the arrays.
        epx = np.vstack(xs)
        eph = np.vstack(hs)
        epdlogp = np.vstack(dlogps)
        epr = np.vstack(drs)

        # Compute the discounted reward backward through time.
        discounted_epr = process_rewards(epr)
        # Standardize the rewards to be unit normal (helps control the gradient
        # estimator variance).
        discounted_epr -= np.mean(discounted_epr)
        discounted_epr /= np.std(discounted_epr)
        # Modulate the gradient with advantage (the policy gradient magic
        # happens right here).
        epdlogp *= discounted_epr

        bw = model.policy_backward(eph, epx, epdlogp)

        # End timing
        end_time = time.time()

        # Print the elapsed time
        print(f"Time taken: {end_time - start_time} seconds")

        return bw, reward_sum


start_time = 0
round_num = 0
iterations = 1000
batch_size = 3
model = Model()
actors = [RolloutWorker.remote() for _ in range(batch_size)]

running_reward = None
# "Xavier" initialization.
# Update buffers that add up gradients over a batch.
grad_buffer = {k: np.zeros_like(v) for k, v in model.weights.items()}
# Update the rmsprop memory.
rmsprop_cache = {k: np.zeros_like(v) for k, v in model.weights.items()}

for i in range(1, 1 + iterations):
    model_id = ray.put(model)
    gradient_ids = []
    # Launch tasks to compute gradients from multiple rollouts in parallel.
    gradient_ids = [actor.compute_gradient.remote(
        model_id) for actor in actors]
    for batch in range(batch_size):
        [grad_id], gradient_ids = ray.wait(gradient_ids)
        grad, reward_sum = ray.get(grad_id)
        # Accumulate the gradient over batch.
        for k in model.weights:
            grad_buffer[k] += grad[k]
        running_reward = (
            reward_sum
            if running_reward is None
            else running_reward * 0.99 + reward_sum * 0.01
        )
    model.update(grad_buffer, rmsprop_cache, learning_rate, decay_rate)
    zero_grads(grad_buffer)

    # first round
    if int(round_num) == 0:
        start_time = time.time()

    # time diff
    elapsed_time = time.time() - start_time
    print(f"Training time: {elapsed_time:.4f} seconds")

    # print round number
    print("Round: "+str(round_num))
    round_num += 1

    # print running reward
    print("Reward: " + str(running_reward) + " \n")
