import random
import numpy as np
import time
import gym
import copy
import LinguaFrancapong_lf as lf
from LinguaFrancapong_lf import (
    Tag, action_capsule_t, port_capsule, request_stop, schedule_copy, start
)
import os
import sys
sys.path.append(os.path.dirname(__file__))
# List imported names, but do not use pylint's --extension-pkg-allow-list option
# so that these names will be assumed present without having to compile and install.
# pylint: disable=no-name-in-module, import-error
# pylint: disable=c-extension-no-member
try:
    from LinguaFrancaBase.constants import BILLION, FOREVER, NEVER, instant_t, interval_t
    from LinguaFrancaBase.functions import (
        DAY, DAYS, HOUR, HOURS, MINUTE, MINUTES, MSEC, MSECS, NSEC, NSECS, SEC, SECS, USEC,
        USECS, WEEK, WEEKS
    )
    from LinguaFrancaBase.classes import Make
except ModuleNotFoundError:
    print("No module named 'LinguaFrancaBase'. "
          "Install using \"pip3 install LinguaFrancaBase\".")
    sys.exit(1)

# From the preamble, verbatim:

os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"


H = 800  # The number of hidden layer neurons.
gamma = 0.99  # The discount factor for reward.
decay_rate = 0.99  # The decay factor for RMSProp leaky sum of grad^2.
D = 80 * 80  # The input dimensionality: 80x80 grid.
learning_rate = 1e-4  # Magnitude of the update.

SEED = 42
np.random.seed(SEED)
random.seed(SEED)
os.environ["PYTHONHASHSEED"] = str(SEED)


def preprocess(img):
    img = img[35:195]
    img = img[::2, ::2, 0]
    img[img == 144] = 0
    img[img == 109] = 0
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


def rollout(weights, env):
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
        observation = observation[0]
    # Note that prev_x is used in computing the difference frame.
    prev_x = None
    xs, hs, dlogps, drs = [], [], [], []
    terminated = truncated = False
    while not terminated:
        cur_x = preprocess(observation)
        x = cur_x - prev_x if prev_x is not None else np.zeros(D)
        prev_x = cur_x

        aprob, h = policy_forward(weights, x)
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
        drs.append(reward)
    return xs, hs, dlogps, drs


def policy_forward(weights, x):
    h1 = np.dot(weights["W1"], x)
    h1[h1 < 0] = 0  # ReLU nonlinearity
    h2 = np.dot(weights["W2"], h1)
    h2[h2 < 0] = 0
    h3 = np.dot(weights["W3"], h2)
    h3[h3 < 0] = 0
    h4 = np.dot(weights["W4"], h3)
    h4[h4 < 0] = 0
    h5 = np.dot(weights["W5"], h4)
    h5[h5 < 0] = 0
    logp = np.dot(weights["W6"], h5)
    p = 1.0 / (1.0 + np.exp(-logp))
    return p, h5


def policy_backward(weights, eph, epx, epdlogp):
    """Backward pass to calculate gradients."""
    dW6 = np.dot(eph.T, epdlogp).ravel()
    dh5 = np.outer(epdlogp, weights["W6"])
    dh5[eph <= 0] = 0
    dW5 = np.dot(eph.T, dh5)
    dh4 = np.dot(dh5, weights["W5"].T)
    dh4[eph <= 0] = 0
    dW4 = np.dot(eph.T, dh4)
    dh3 = np.dot(dh4, weights["W4"].T)
    dh3[eph <= 0] = 0
    dW3 = np.dot(eph.T, dh3)
    dh2 = np.dot(dh3, weights["W3"].T)
    dh2[eph <= 0] = 0
    dW2 = np.dot(eph.T, dh2)
    dh1 = np.dot(dh2, weights["W2"].T)
    dh1[eph <= 0] = 0
    dW1 = np.dot(epx.T, dh1)
    return {"W6": dW6, "W5": dW5, "W4": dW4, "W3": dW3, "W2": dW2, "W1": dW1}


def update(weights, grad_buffer, rmsprop_cache, lr, decay):
    """Applies the gradients to the model parameters with RMSProp."""
    for k, v in weights.items():
        g = grad_buffer[k]
        rmsprop_cache[k] = decay * rmsprop_cache[k] + (1 - decay) * g ** 2
        weights[k] += lr * g / (np.sqrt(rmsprop_cache[k]) + 1e-5)


def zero_grads(grad_buffer):
    """Reset the batch gradient buffer."""
    for k, v in grad_buffer.items():
        grad_buffer[k] = np.zeros_like(v)

# End of preamble.
# From the preamble, verbatim:


os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"


H = 600  # The number of hidden layer neurons.
gamma = 0.99  # The discount factor for reward.
decay_rate = 0.99  # The decay factor for RMSProp leaky sum of grad^2.
D = 80 * 80  # The input dimensionality: 80x80 grid.
learning_rate = 1e-4  # Magnitude of the update.

SEED = 42
np.random.seed(SEED)
random.seed(SEED)
os.environ["PYTHONHASHSEED"] = str(SEED)


def preprocess(img):
    img = img[35:195]
    img = img[::2, ::2, 0]
    img[img == 144] = 0
    img[img == 109] = 0
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


def rollout(weights, env):
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
        observation = observation[0]
    # Note that prev_x is used in computing the difference frame.
    prev_x = None
    xs, hs, dlogps, drs = [], [], [], []
    terminated = truncated = False
    while not terminated:
        cur_x = preprocess(observation)
        x = cur_x - prev_x if prev_x is not None else np.zeros(D)
        prev_x = cur_x

        aprob, h = policy_forward(weights, x)
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
        drs.append(reward)
    return xs, hs, dlogps, drs


def policy_forward(weights, x):
    h1 = np.dot(weights["W1"], x)
    h1[h1 < 0] = 0  # ReLU nonlinearity
    h2 = np.dot(weights["W2"], h1)
    h2[h2 < 0] = 0
    h3 = np.dot(weights["W3"], h2)
    h3[h3 < 0] = 0
    h4 = np.dot(weights["W4"], h3)
    h4[h4 < 0] = 0
    h5 = np.dot(weights["W5"], h4)
    h5[h5 < 0] = 0
    logp = np.dot(weights["W6"], h5)
    p = 1.0 / (1.0 + np.exp(-logp))
    return p, h5


def policy_backward(weights, eph, epx, epdlogp):
    """Backward pass to calculate gradients."""
    dW6 = np.dot(eph.T, epdlogp).ravel()
    dh5 = np.outer(epdlogp, weights["W6"])
    dh5[eph <= 0] = 0
    dW5 = np.dot(eph.T, dh5)
    dh4 = np.dot(dh5, weights["W5"].T)
    dh4[eph <= 0] = 0
    dW4 = np.dot(eph.T, dh4)
    dh3 = np.dot(dh4, weights["W4"].T)
    dh3[eph <= 0] = 0
    dW3 = np.dot(eph.T, dh3)
    dh2 = np.dot(dh3, weights["W3"].T)
    dh2[eph <= 0] = 0
    dW2 = np.dot(eph.T, dh2)
    dh1 = np.dot(dh2, weights["W2"].T)
    dh1[eph <= 0] = 0
    dW1 = np.dot(epx.T, dh1)
    return {"W6": dW6, "W5": dW5, "W4": dW4, "W3": dW3, "W2": dW2, "W1": dW1}


def update(weights, grad_buffer, rmsprop_cache, lr, decay):
    """Applies the gradients to the model parameters with RMSProp."""
    for k, v in weights.items():
        g = grad_buffer[k]
        rmsprop_cache[k] = decay * rmsprop_cache[k] + (1 - decay) * g ** 2
        weights[k] += lr * g / (np.sqrt(rmsprop_cache[k]) + 1e-5)


def zero_grads(grad_buffer):
    """Reset the batch gradient buffer."""
    for k, v in grad_buffer.items():
        grad_buffer[k] = np.zeros_like(v)

# End of preamble.
# From the preamble, verbatim:


os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"


H = 600  # The number of hidden layer neurons.
gamma = 0.99  # The discount factor for reward.
decay_rate = 0.99  # The decay factor for RMSProp leaky sum of grad^2.
D = 80 * 80  # The input dimensionality: 80x80 grid.
learning_rate = 1e-4  # Magnitude of the update.

SEED = 42
np.random.seed(SEED)
random.seed(SEED)
os.environ["PYTHONHASHSEED"] = str(SEED)


def preprocess(img):
    img = img[35:195]
    img = img[::2, ::2, 0]
    img[img == 144] = 0
    img[img == 109] = 0
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


def rollout(weights, env):
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
        observation = observation[0]
    # Note that prev_x is used in computing the difference frame.
    prev_x = None
    xs, hs, dlogps, drs = [], [], [], []
    terminated = truncated = False
    while not terminated:
        cur_x = preprocess(observation)
        x = cur_x - prev_x if prev_x is not None else np.zeros(D)
        prev_x = cur_x

        aprob, h = policy_forward(weights, x)
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
        drs.append(reward)
    return xs, hs, dlogps, drs


def policy_forward(weights, x):
    h1 = np.dot(weights["W1"], x)
    h1[h1 < 0] = 0  # ReLU nonlinearity
    h2 = np.dot(weights["W2"], h1)
    h2[h2 < 0] = 0
    h3 = np.dot(weights["W3"], h2)
    h3[h3 < 0] = 0
    h4 = np.dot(weights["W4"], h3)
    h4[h4 < 0] = 0
    h5 = np.dot(weights["W5"], h4)
    h5[h5 < 0] = 0
    logp = np.dot(weights["W6"], h5)
    p = 1.0 / (1.0 + np.exp(-logp))
    return p, h5


def policy_backward(weights, eph, epx, epdlogp):
    """Backward pass to calculate gradients."""
    dW6 = np.dot(eph.T, epdlogp).ravel()
    dh5 = np.outer(epdlogp, weights["W6"])
    dh5[eph <= 0] = 0
    dW5 = np.dot(eph.T, dh5)
    dh4 = np.dot(dh5, weights["W5"].T)
    dh4[eph <= 0] = 0
    dW4 = np.dot(eph.T, dh4)
    dh3 = np.dot(dh4, weights["W4"].T)
    dh3[eph <= 0] = 0
    dW3 = np.dot(eph.T, dh3)
    dh2 = np.dot(dh3, weights["W3"].T)
    dh2[eph <= 0] = 0
    dW2 = np.dot(eph.T, dh2)
    dh1 = np.dot(dh2, weights["W2"].T)
    dh1[eph <= 0] = 0
    dW1 = np.dot(epx.T, dh1)
    return {"W6": dW6, "W5": dW5, "W4": dW4, "W3": dW3, "W2": dW2, "W1": dW1}


def update(weights, grad_buffer, rmsprop_cache, lr, decay):
    """Applies the gradients to the model parameters with RMSProp."""
    for k, v in weights.items():
        g = grad_buffer[k]
        rmsprop_cache[k] = decay * rmsprop_cache[k] + (1 - decay) * g ** 2
        weights[k] += lr * g / (np.sqrt(rmsprop_cache[k]) + 1e-5)


def zero_grads(grad_buffer):
    """Reset the batch gradient buffer."""
    for k, v in grad_buffer.items():
        grad_buffer[k] = np.zeros_like(v)

# End of preamble.
# From the preamble, verbatim:


os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"


H = 600  # The number of hidden layer neurons.
gamma = 0.99  # The discount factor for reward.
decay_rate = 0.99  # The decay factor for RMSProp leaky sum of grad^2.
D = 80 * 80  # The input dimensionality: 80x80 grid.
learning_rate = 1e-4  # Magnitude of the update.

SEED = 42
np.random.seed(SEED)
random.seed(SEED)
os.environ["PYTHONHASHSEED"] = str(SEED)


def preprocess(img):
    img = img[35:195]
    img = img[::2, ::2, 0]
    img[img == 144] = 0
    img[img == 109] = 0
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


def rollout(weights, env):
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
        observation = observation[0]
    # Note that prev_x is used in computing the difference frame.
    prev_x = None
    xs, hs, dlogps, drs = [], [], [], []
    terminated = truncated = False
    while not terminated:
        cur_x = preprocess(observation)
        x = cur_x - prev_x if prev_x is not None else np.zeros(D)
        prev_x = cur_x

        aprob, h = policy_forward(weights, x)
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
        drs.append(reward)
    return xs, hs, dlogps, drs


def policy_forward(weights, x):
    h1 = np.dot(weights["W1"], x)
    h1[h1 < 0] = 0  # ReLU nonlinearity
    h2 = np.dot(weights["W2"], h1)
    h2[h2 < 0] = 0
    h3 = np.dot(weights["W3"], h2)
    h3[h3 < 0] = 0
    h4 = np.dot(weights["W4"], h3)
    h4[h4 < 0] = 0
    h5 = np.dot(weights["W5"], h4)
    h5[h5 < 0] = 0
    logp = np.dot(weights["W6"], h5)
    p = 1.0 / (1.0 + np.exp(-logp))
    return p, h5


def policy_backward(weights, eph, epx, epdlogp):
    """Backward pass to calculate gradients."""
    dW6 = np.dot(eph.T, epdlogp).ravel()
    dh5 = np.outer(epdlogp, weights["W6"])
    dh5[eph <= 0] = 0
    dW5 = np.dot(eph.T, dh5)
    dh4 = np.dot(dh5, weights["W5"].T)
    dh4[eph <= 0] = 0
    dW4 = np.dot(eph.T, dh4)
    dh3 = np.dot(dh4, weights["W4"].T)
    dh3[eph <= 0] = 0
    dW3 = np.dot(eph.T, dh3)
    dh2 = np.dot(dh3, weights["W3"].T)
    dh2[eph <= 0] = 0
    dW2 = np.dot(eph.T, dh2)
    dh1 = np.dot(dh2, weights["W2"].T)
    dh1[eph <= 0] = 0
    dW1 = np.dot(epx.T, dh1)
    return {"W6": dW6, "W5": dW5, "W4": dW4, "W3": dW3, "W2": dW2, "W1": dW1}


def update(weights, grad_buffer, rmsprop_cache, lr, decay):
    """Applies the gradients to the model parameters with RMSProp."""
    for k, v in weights.items():
        g = grad_buffer[k]
        rmsprop_cache[k] = decay * rmsprop_cache[k] + (1 - decay) * g ** 2
        weights[k] += lr * g / (np.sqrt(rmsprop_cache[k]) + 1e-5)


def zero_grads(grad_buffer):
    """Reset the batch gradient buffer."""
    for k, v in grad_buffer.items():
        grad_buffer[k] = np.zeros_like(v)

# End of preamble.
# From the preamble, verbatim:


os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"


H = 600  # The number of hidden layer neurons.
gamma = 0.99  # The discount factor for reward.
decay_rate = 0.99  # The decay factor for RMSProp leaky sum of grad^2.
D = 80 * 80  # The input dimensionality: 80x80 grid.
learning_rate = 1e-4  # Magnitude of the update.

SEED = 42
np.random.seed(SEED)
random.seed(SEED)
os.environ["PYTHONHASHSEED"] = str(SEED)


def preprocess(img):
    img = img[35:195]
    img = img[::2, ::2, 0]
    img[img == 144] = 0
    img[img == 109] = 0
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


def rollout(weights, env):
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
        observation = observation[0]
    # Note that prev_x is used in computing the difference frame.
    prev_x = None
    xs, hs, dlogps, drs = [], [], [], []
    terminated = truncated = False
    while not terminated:
        cur_x = preprocess(observation)
        x = cur_x - prev_x if prev_x is not None else np.zeros(D)
        prev_x = cur_x

        aprob, h = policy_forward(weights, x)
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
        drs.append(reward)
    return xs, hs, dlogps, drs


def policy_forward(weights, x):
    h1 = np.dot(weights["W1"], x)
    h1[h1 < 0] = 0  # ReLU nonlinearity
    h2 = np.dot(weights["W2"], h1)
    h2[h2 < 0] = 0
    h3 = np.dot(weights["W3"], h2)
    h3[h3 < 0] = 0
    h4 = np.dot(weights["W4"], h3)
    h4[h4 < 0] = 0
    h5 = np.dot(weights["W5"], h4)
    h5[h5 < 0] = 0
    logp = np.dot(weights["W6"], h5)
    p = 1.0 / (1.0 + np.exp(-logp))
    return p, h5


def policy_backward(weights, eph, epx, epdlogp):
    """Backward pass to calculate gradients."""
    dW6 = np.dot(eph.T, epdlogp).ravel()
    dh5 = np.outer(epdlogp, weights["W6"])
    dh5[eph <= 0] = 0
    dW5 = np.dot(eph.T, dh5)
    dh4 = np.dot(dh5, weights["W5"].T)
    dh4[eph <= 0] = 0
    dW4 = np.dot(eph.T, dh4)
    dh3 = np.dot(dh4, weights["W4"].T)
    dh3[eph <= 0] = 0
    dW3 = np.dot(eph.T, dh3)
    dh2 = np.dot(dh3, weights["W3"].T)
    dh2[eph <= 0] = 0
    dW2 = np.dot(eph.T, dh2)
    dh1 = np.dot(dh2, weights["W2"].T)
    dh1[eph <= 0] = 0
    dW1 = np.dot(epx.T, dh1)
    return {"W6": dW6, "W5": dW5, "W4": dW4, "W3": dW3, "W2": dW2, "W1": dW1}


def update(weights, grad_buffer, rmsprop_cache, lr, decay):
    """Applies the gradients to the model parameters with RMSProp."""
    for k, v in weights.items():
        g = grad_buffer[k]
        rmsprop_cache[k] = decay * rmsprop_cache[k] + (1 - decay) * g ** 2
        weights[k] += lr * g / (np.sqrt(rmsprop_cache[k]) + 1e-5)


def zero_grads(grad_buffer):
    """Reset the batch gradient buffer."""
    for k, v in grad_buffer.items():
        grad_buffer[k] = np.zeros_like(v)

# End of preamble.
# From the preamble, verbatim:


os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"


H = 600  # The number of hidden layer neurons.
gamma = 0.99  # The discount factor for reward.
decay_rate = 0.99  # The decay factor for RMSProp leaky sum of grad^2.
D = 80 * 80  # The input dimensionality: 80x80 grid.
learning_rate = 1e-4  # Magnitude of the update.

SEED = 42
np.random.seed(SEED)
random.seed(SEED)
os.environ["PYTHONHASHSEED"] = str(SEED)


def preprocess(img):
    img = img[35:195]
    img = img[::2, ::2, 0]
    img[img == 144] = 0
    img[img == 109] = 0
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


def rollout(weights, env):
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
        observation = observation[0]
    # Note that prev_x is used in computing the difference frame.
    prev_x = None
    xs, hs, dlogps, drs = [], [], [], []
    terminated = truncated = False
    while not terminated:
        cur_x = preprocess(observation)
        x = cur_x - prev_x if prev_x is not None else np.zeros(D)
        prev_x = cur_x

        aprob, h = policy_forward(weights, x)
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
        drs.append(reward)
    return xs, hs, dlogps, drs


def policy_forward(weights, x):
    h1 = np.dot(weights["W1"], x)
    h1[h1 < 0] = 0  # ReLU nonlinearity
    h2 = np.dot(weights["W2"], h1)
    h2[h2 < 0] = 0
    h3 = np.dot(weights["W3"], h2)
    h3[h3 < 0] = 0
    h4 = np.dot(weights["W4"], h3)
    h4[h4 < 0] = 0
    h5 = np.dot(weights["W5"], h4)
    h5[h5 < 0] = 0
    logp = np.dot(weights["W6"], h5)
    p = 1.0 / (1.0 + np.exp(-logp))
    return p, h5


def policy_backward(weights, eph, epx, epdlogp):
    """Backward pass to calculate gradients."""
    dW6 = np.dot(eph.T, epdlogp).ravel()
    dh5 = np.outer(epdlogp, weights["W6"])
    dh5[eph <= 0] = 0
    dW5 = np.dot(eph.T, dh5)
    dh4 = np.dot(dh5, weights["W5"].T)
    dh4[eph <= 0] = 0
    dW4 = np.dot(eph.T, dh4)
    dh3 = np.dot(dh4, weights["W4"].T)
    dh3[eph <= 0] = 0
    dW3 = np.dot(eph.T, dh3)
    dh2 = np.dot(dh3, weights["W3"].T)
    dh2[eph <= 0] = 0
    dW2 = np.dot(eph.T, dh2)
    dh1 = np.dot(dh2, weights["W2"].T)
    dh1[eph <= 0] = 0
    dW1 = np.dot(epx.T, dh1)
    return {"W6": dW6, "W5": dW5, "W4": dW4, "W3": dW3, "W2": dW2, "W1": dW1}


def update(weights, grad_buffer, rmsprop_cache, lr, decay):
    """Applies the gradients to the model parameters with RMSProp."""
    for k, v in weights.items():
        g = grad_buffer[k]
        rmsprop_cache[k] = decay * rmsprop_cache[k] + (1 - decay) * g ** 2
        weights[k] += lr * g / (np.sqrt(rmsprop_cache[k]) + 1e-5)


def zero_grads(grad_buffer):
    """Reset the batch gradient buffer."""
    for k, v in grad_buffer.items():
        grad_buffer[k] = np.zeros_like(v)

# End of preamble.
# From the preamble, verbatim:


os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"


H = 600  # The number of hidden layer neurons.
gamma = 0.99  # The discount factor for reward.
decay_rate = 0.99  # The decay factor for RMSProp leaky sum of grad^2.
D = 80 * 80  # The input dimensionality: 80x80 grid.
learning_rate = 1e-4  # Magnitude of the update.

SEED = 42
np.random.seed(SEED)
random.seed(SEED)
os.environ["PYTHONHASHSEED"] = str(SEED)


def preprocess(img):
    img = img[35:195]
    img = img[::2, ::2, 0]
    img[img == 144] = 0
    img[img == 109] = 0
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


def rollout(weights, env):
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
        observation = observation[0]
    # Note that prev_x is used in computing the difference frame.
    prev_x = None
    xs, hs, dlogps, drs = [], [], [], []
    terminated = truncated = False
    while not terminated:
        cur_x = preprocess(observation)
        x = cur_x - prev_x if prev_x is not None else np.zeros(D)
        prev_x = cur_x

        aprob, h = policy_forward(weights, x)
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
        drs.append(reward)
    return xs, hs, dlogps, drs


def policy_forward(weights, x):
    h1 = np.dot(weights["W1"], x)
    h1[h1 < 0] = 0  # ReLU nonlinearity
    h2 = np.dot(weights["W2"], h1)
    h2[h2 < 0] = 0
    h3 = np.dot(weights["W3"], h2)
    h3[h3 < 0] = 0
    h4 = np.dot(weights["W4"], h3)
    h4[h4 < 0] = 0
    h5 = np.dot(weights["W5"], h4)
    h5[h5 < 0] = 0
    logp = np.dot(weights["W6"], h5)
    p = 1.0 / (1.0 + np.exp(-logp))
    return p, h5


def policy_backward(weights, eph, epx, epdlogp):
    """Backward pass to calculate gradients."""
    dW6 = np.dot(eph.T, epdlogp).ravel()
    dh5 = np.outer(epdlogp, weights["W6"])
    dh5[eph <= 0] = 0
    dW5 = np.dot(eph.T, dh5)
    dh4 = np.dot(dh5, weights["W5"].T)
    dh4[eph <= 0] = 0
    dW4 = np.dot(eph.T, dh4)
    dh3 = np.dot(dh4, weights["W4"].T)
    dh3[eph <= 0] = 0
    dW3 = np.dot(eph.T, dh3)
    dh2 = np.dot(dh3, weights["W3"].T)
    dh2[eph <= 0] = 0
    dW2 = np.dot(eph.T, dh2)
    dh1 = np.dot(dh2, weights["W2"].T)
    dh1[eph <= 0] = 0
    dW1 = np.dot(epx.T, dh1)
    return {"W6": dW6, "W5": dW5, "W4": dW4, "W3": dW3, "W2": dW2, "W1": dW1}


def update(weights, grad_buffer, rmsprop_cache, lr, decay):
    """Applies the gradients to the model parameters with RMSProp."""
    for k, v in weights.items():
        g = grad_buffer[k]
        rmsprop_cache[k] = decay * rmsprop_cache[k] + (1 - decay) * g ** 2
        weights[k] += lr * g / (np.sqrt(rmsprop_cache[k]) + 1e-5)


def zero_grads(grad_buffer):
    """Reset the batch gradient buffer."""
    for k, v in grad_buffer.items():
        grad_buffer[k] = np.zeros_like(v)

# End of preamble.
# From the preamble, verbatim:


os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"


H = 800  # The number of hidden layer neurons.
gamma = 0.99  # The discount factor for reward.
decay_rate = 0.99  # The decay factor for RMSProp leaky sum of grad^2.
D = 80 * 80  # The input dimensionality: 80x80 grid.
learning_rate = 1e-4  # Magnitude of the update.

SEED = 42
np.random.seed(SEED)
random.seed(SEED)
os.environ["PYTHONHASHSEED"] = str(SEED)


def preprocess(img):
    img = img[35:195]
    img = img[::2, ::2, 0]
    img[img == 144] = 0
    img[img == 109] = 0
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


def rollout(weights, env):
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
        observation = observation[0]
    # Note that prev_x is used in computing the difference frame.
    prev_x = None
    xs, hs, dlogps, drs = [], [], [], []
    terminated = truncated = False
    while not terminated:
        cur_x = preprocess(observation)
        x = cur_x - prev_x if prev_x is not None else np.zeros(D)
        prev_x = cur_x

        aprob, h = policy_forward(weights, x)
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
        drs.append(reward)
    return xs, hs, dlogps, drs


def policy_forward(weights, x):
    h1 = np.dot(weights["W1"], x)
    h1[h1 < 0] = 0  # ReLU nonlinearity
    h2 = np.dot(weights["W2"], h1)
    h2[h2 < 0] = 0
    h3 = np.dot(weights["W3"], h2)
    h3[h3 < 0] = 0
    h4 = np.dot(weights["W4"], h3)
    h4[h4 < 0] = 0
    h5 = np.dot(weights["W5"], h4)
    h5[h5 < 0] = 0
    logp = np.dot(weights["W6"], h5)
    p = 1.0 / (1.0 + np.exp(-logp))
    return p, h5


def policy_backward(weights, eph, epx, epdlogp):
    """Backward pass to calculate gradients."""
    dW6 = np.dot(eph.T, epdlogp).ravel()
    dh5 = np.outer(epdlogp, weights["W6"])
    dh5[eph <= 0] = 0
    dW5 = np.dot(eph.T, dh5)
    dh4 = np.dot(dh5, weights["W5"].T)
    dh4[eph <= 0] = 0
    dW4 = np.dot(eph.T, dh4)
    dh3 = np.dot(dh4, weights["W4"].T)
    dh3[eph <= 0] = 0
    dW3 = np.dot(eph.T, dh3)
    dh2 = np.dot(dh3, weights["W3"].T)
    dh2[eph <= 0] = 0
    dW2 = np.dot(eph.T, dh2)
    dh1 = np.dot(dh2, weights["W2"].T)
    dh1[eph <= 0] = 0
    dW1 = np.dot(epx.T, dh1)
    return {"W6": dW6, "W5": dW5, "W4": dW4, "W3": dW3, "W2": dW2, "W1": dW1}


def update(weights, grad_buffer, rmsprop_cache, lr, decay):
    """Applies the gradients to the model parameters with RMSProp."""
    for k, v in weights.items():
        g = grad_buffer[k]
        rmsprop_cache[k] = decay * rmsprop_cache[k] + (1 - decay) * g ** 2
        weights[k] += lr * g / (np.sqrt(rmsprop_cache[k]) + 1e-5)


def zero_grads(grad_buffer):
    """Reset the batch gradient buffer."""
    for k, v in grad_buffer.items():
        grad_buffer[k] = np.zeros_like(v)
# End of preamble.


# Python class for reactor _pong_lf_main
class __pong_lf_main:

    # Constructor
    def __init__(self, **kwargs):
        # Define parameters and their default values
        # Handle parameters that are set in instantiation
        self.__dict__.update(kwargs)
        # Define state variables

    @property
    def bank_index(self):
        return self._bank_index  # pylint: disable=no-member


# Python class for reactor _clientreactor
class __clientreactor:

    # Constructor
    def __init__(self, **kwargs):
        # Define parameters and their default values
        # Handle parameters that are set in instantiation
        self.__dict__.update(kwargs)
        # Define state variables
        self.env = gym.make("Pong-v4")
        self.env.seed(SEED)

    @property
    def bank_index(self):
        return self._bank_index  # pylint: disable=no-member

    def reaction_function_0(self):

        return 0

    def reaction_function_1(self, global_parameters, updated_parameters):

        start_time = time.time()
        # Compute a simulation episode.
        w1 = global_parameters.value[0]
        w2 = global_parameters.value[1]
        w3 = global_parameters.value[2]
        w4 = global_parameters.value[3]
        w5 = global_parameters.value[4]
        w6 = global_parameters.value[5]
        # Update the weights dictionary with all the weights
        weights = {"W1": w1, "W2": w2, "W3": w3, "W4": w4, "W5": w5, "W6": w6}

        xs, hs, dlogps, drs = rollout(weights, self.env)
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

        backward_result = policy_backward(weights, eph, epx, epdlogp)
        ids = [
            backward_result["W1"],
            backward_result["W2"],
            backward_result["W3"],
            backward_result["W4"],
            backward_result["W5"],
            backward_result["W6"],
            reward_sum
        ]
        updated_parameters.set(ids)

        # End timing
        end_time = time.time()

        # Print the elapsed time
        print(f"Time taken: {end_time - start_time} seconds")
        return 0

# Python class for reactor _serverreactor


class __serverreactor:

    # Constructor
    def __init__(self, **kwargs):
        # Define parameters and their default values
        # Handle parameters that are set in instantiation
        self.__dict__.update(kwargs)
        # Define state variables
        self.running_reward = None
        self.grad_buffer = None
        self.rmsprop_cache = None
        self.results = None
        self.round_num = None
        self.start_time = None
        self.weights = None

    @property
    def bank_index(self):
        return self._bank_index  # pylint: disable=no-member

    def reaction_function_0(self, global_parameters):

        self.weights = {}
        self.weights["W1"] = np.random.randn(H, D) / np.sqrt(D)
        self.weights["W2"] = np.random.randn(H, H) / np.sqrt(H)  # New layer
        self.weights["W3"] = np.random.randn(H, H) / np.sqrt(H)  # New layer
        self.weights["W4"] = np.random.randn(H, H) / np.sqrt(H)  # New layer
        self.weights["W5"] = np.random.randn(H, H) / np.sqrt(H)  # New layer
        self.weights["W6"] = np.random.randn(H) / np.sqrt(H)     # Output layer
        self.round_num = 0
        self.results = [()] * 3
        w1 = self.weights["W1"]
        w2 = self.weights["W2"]
        w3 = self.weights["W3"]
        w4 = self.weights["W4"]
        w5 = self.weights["W5"]
        w6 = self.weights["W6"]
        ids = [w1, w2, w3, w4, w5, w6]
        self.running_reward = None
        # "Xavier" initialization.
        # Update buffers that add up gradients over a batch.
        self.grad_buffer = {k: np.zeros_like(v)
                            for k, v in self.weights.items()}
        # Update the rmsprop memory.
        self.rmsprop_cache = {k: np.zeros_like(
            v) for k, v in self.weights.items()}
        global_parameters.set(ids)
        return 0

    def reaction_function_1(self, updated_parameters, global_parameters):

        grad = {}
        for i in range(6):
            grad["W1"] = updated_parameters[i].value[0]
            grad["W2"] = updated_parameters[i].value[1]
            grad["W3"] = updated_parameters[i].value[2]
            grad["W4"] = updated_parameters[i].value[3]
            grad["W5"] = updated_parameters[i].value[4]
            grad["W6"] = updated_parameters[i].value[5]
            reward_sum = updated_parameters[i].value[6]
            # grad, reward_sum = self.results[batch]
            # Accumulate the gradient over batch.
            for k in self.weights:
                grad[k] = grad[k].T
                self.grad_buffer[k] += grad[k]
            self.running_reward = (
                reward_sum
                if self.running_reward is None
                else self.running_reward * 0.99 + reward_sum * 0.01
            )
        update(self.weights, self.grad_buffer,
               self.rmsprop_cache, learning_rate, decay_rate)
        zero_grads(self.grad_buffer)
        ids = [
            self.weights["W1"],
            self.weights["W2"],
            self.weights["W3"],
            self.weights["W4"],
            self.weights["W5"],
            self.weights["W6"]
        ]
        # first round
        if int(self.round_num) == 0:
            self.start_time = time.time()
        # print round number
        print("Round: "+str(self.round_num))
        self.round_num += 1
        # time diff
        elapsed_time = time.time() - self.start_time
        print(f"Training time: {elapsed_time:.4f} seconds")
        # print running reward
        print("Reward: " + str(self.running_reward) + " \n")
        global_parameters.set(ids)
        return 0

# Python class for reactor __lf_gendelay_0


class ___lf_gendelay_0:

    # Constructor
    def __init__(self, **kwargs):
        # Define parameters and their default values
        self._delay: interval_t = 0
        # Handle parameters that are set in instantiation
        self.__dict__.update(kwargs)
        # Define state variables

    @property
    def delay(self):
        return self._delay  # pylint: disable=no-member

    @property
    def bank_index(self):
        return self._bank_index  # pylint: disable=no-member


# Instantiate classes
pong_lf_main_lf = [None] * 1
pong_lf_client_lf = [None] * 6
pong_lf_server_lf = [None] * 1
pong_lf_delay_lf = [None] * 1
# Start initializing pong_lf of class _pong_lf_main
for pong_lf_main_i in range(1):
    bank_index = pong_lf_main_i
    pong_lf_main_lf[0] = __pong_lf_main(
        _bank_index=0,
    )
    # Start initializing pong_lf.client of class _clientreactor
    for pong_lf_client_i in range(6):
        bank_index = pong_lf_client_i
        pong_lf_client_lf[pong_lf_client_i] = __clientreactor(
            _bank_index=pong_lf_client_i,
        )
    # Start initializing pong_lf.server of class _serverreactor
    for pong_lf_server_i in range(1):
        bank_index = pong_lf_server_i
        pong_lf_server_lf[0] = __serverreactor(
            _bank_index=0,
        )
    # Start initializing pong_lf.delay of class __lf_gendelay_0
    for pong_lf_delay_i in range(1):
        bank_index = pong_lf_delay_i
        pong_lf_delay_lf[0] = ___lf_gendelay_0(
            _bank_index=pong_lf_delay_i,
            _delay=0,
        )


# The main function
def main(argv):
    start(argv)


# As is customary in Python programs, the main() function
# should only be executed if the main module is active.
if __name__ == "__main__":
    main(sys.argv)
