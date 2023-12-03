import time
from numpy.random import RandomState
import numpy as np
import torch
import gym
import copy
import LinguaFrancapong_gpu as lf
from LinguaFrancapong_gpu import (
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

# Constants
H = 100  # Number of hidden layer neurons
D = 80 * 80  # Input dimensionality: 80x80 grid
gamma = 0.99  # Discount factor for reward
learning_rate = 1e-4  # Learning rate
episodes = 1000  # Number of training iterations
SEED = 42  # Seed for reproducibility

# Set seeds
np.random.seed(SEED)
torch.manual_seed(SEED)


def preprocess(img):
    img = img[35:195]  # Crop
    img = img[::2, ::2, 0]  # Downsample by factor of 2
    img[img == 144] = 0  # Erase background (type 1)
    img[img == 109] = 0  # Erase background (type 2)
    img[img != 0] = 1  # Everything else (paddles, ball) just set to 1
    return img.astype(np.float64).ravel()


class PolicyNetwork(torch.nn.Module):
    def __init__(self):
        super(PolicyNetwork, self).__init__()
        self.fc1 = torch.nn.Linear(D, H)
        self.fc2 = torch.nn.Linear(H, 1)
        self.relu = torch.nn.ReLU()
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x):
        h = self.relu(self.fc1(x))
        logp = self.fc2(h)
        p = self.sigmoid(logp)
        return p, h


def discount_rewards(r):
    discounted_r = np.zeros_like(r)
    running_add = 0
    for t in reversed(range(0, r.size)):
        if r[t] != 0:
            # Reset the sum, since this was a game boundary (pong specific!)
            running_add = 0
        running_add = running_add * gamma + r[t]
        discounted_r[t] = running_add

    # Standardize the rewards to be unit normal
    discounted_r -= np.mean(discounted_r)
    discounted_r /= np.std(discounted_r)
    return discounted_r


def rollout(policy, env, rs, device):

    observation = env.reset()
    prev_x = None
    xs, hs, dlogps, rewards = [], [], [], []
    done = False

    while not done:
        cur_x = preprocess(observation)
        x = torch.from_numpy(
            cur_x - prev_x if prev_x is not None else np.zeros(D)).float().to(device)
        prev_x = cur_x

        aprob, h = policy(x)
        action = 2 if rs.uniform() < aprob.item() else 3  # 2 is UP, 3 is DOWN in Pong

        xs.append(x)
        hs.append(h)
        y = 1 if action == 2 else 0
        dlogps.append(y - aprob)

        observation, reward, done, info = env.step(action)
        rewards.append(reward)

    epr = np.vstack(rewards)
    discounted_epr = discount_rewards(epr)
    epdlogp = torch.vstack(dlogps)
    # Ensure this tensor is on GPU
    epdlogp *= torch.Tensor(discounted_epr).to(device)
    rewards = np.array(rewards)
    return xs, hs, epdlogp, rewards

# End of preamble.
# From the preamble, verbatim:


# Constants
H = 100  # Number of hidden layer neurons
D = 80 * 80  # Input dimensionality: 80x80 grid
gamma = 0.99  # Discount factor for reward
learning_rate = 1e-4  # Learning rate
episodes = 1000  # Number of training iterations
SEED = 42  # Seed for reproducibility

# Set seeds
np.random.seed(SEED)
torch.manual_seed(SEED)


def preprocess(img):
    img = img[35:195]  # Crop
    img = img[::2, ::2, 0]  # Downsample by factor of 2
    img[img == 144] = 0  # Erase background (type 1)
    img[img == 109] = 0  # Erase background (type 2)
    img[img != 0] = 1  # Everything else (paddles, ball) just set to 1
    return img.astype(np.float64).ravel()


class PolicyNetwork(torch.nn.Module):
    def __init__(self):
        super(PolicyNetwork, self).__init__()
        self.fc1 = torch.nn.Linear(D, H)
        self.fc2 = torch.nn.Linear(H, 1)
        self.relu = torch.nn.ReLU()
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x):
        h = self.relu(self.fc1(x))
        logp = self.fc2(h)
        p = self.sigmoid(logp)
        return p, h


def discount_rewards(r):
    discounted_r = np.zeros_like(r)
    running_add = 0
    for t in reversed(range(0, r.size)):
        if r[t] != 0:
            # Reset the sum, since this was a game boundary (pong specific!)
            running_add = 0
        running_add = running_add * gamma + r[t]
        discounted_r[t] = running_add

    # Standardize the rewards to be unit normal
    discounted_r -= np.mean(discounted_r)
    discounted_r /= np.std(discounted_r)
    return discounted_r


def rollout(policy, env, rs, device):

    observation = env.reset()
    prev_x = None
    xs, hs, dlogps, rewards = [], [], [], []
    done = False

    while not done:
        cur_x = preprocess(observation)
        x = torch.from_numpy(
            cur_x - prev_x if prev_x is not None else np.zeros(D)).float().to(device)
        prev_x = cur_x

        aprob, h = policy(x)
        action = 2 if rs.uniform() < aprob.item() else 3  # 2 is UP, 3 is DOWN in Pong

        xs.append(x)
        hs.append(h)
        y = 1 if action == 2 else 0
        dlogps.append(y - aprob)

        observation, reward, done, info = env.step(action)
        rewards.append(reward)

    epr = np.vstack(rewards)
    discounted_epr = discount_rewards(epr)
    epdlogp = torch.vstack(dlogps)
    # Ensure this tensor is on GPU
    epdlogp *= torch.Tensor(discounted_epr).to(device)
    rewards = np.array(rewards)
    return xs, hs, epdlogp, rewards

# End of preamble.
# From the preamble, verbatim:


# Constants
H = 100  # Number of hidden layer neurons
D = 80 * 80  # Input dimensionality: 80x80 grid
gamma = 0.99  # Discount factor for reward
learning_rate = 1e-4  # Learning rate
episodes = 1000  # Number of training iterations
SEED = 42  # Seed for reproducibility

# Set seeds
np.random.seed(SEED)
torch.manual_seed(SEED)


def preprocess(img):
    img = img[35:195]  # Crop
    img = img[::2, ::2, 0]  # Downsample by factor of 2
    img[img == 144] = 0  # Erase background (type 1)
    img[img == 109] = 0  # Erase background (type 2)
    img[img != 0] = 1  # Everything else (paddles, ball) just set to 1
    return img.astype(np.float64).ravel()


class PolicyNetwork(torch.nn.Module):
    def __init__(self):
        super(PolicyNetwork, self).__init__()
        self.fc1 = torch.nn.Linear(D, H)
        self.fc2 = torch.nn.Linear(H, 1)
        self.relu = torch.nn.ReLU()
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x):
        h = self.relu(self.fc1(x))
        logp = self.fc2(h)
        p = self.sigmoid(logp)
        return p, h


def discount_rewards(r):
    discounted_r = np.zeros_like(r)
    running_add = 0
    for t in reversed(range(0, r.size)):
        if r[t] != 0:
            # Reset the sum, since this was a game boundary (pong specific!)
            running_add = 0
        running_add = running_add * gamma + r[t]
        discounted_r[t] = running_add

    # Standardize the rewards to be unit normal
    discounted_r -= np.mean(discounted_r)
    discounted_r /= np.std(discounted_r)
    return discounted_r


def rollout(policy, env, rs, device):

    observation = env.reset()
    prev_x = None
    xs, hs, dlogps, rewards = [], [], [], []
    done = False

    while not done:
        cur_x = preprocess(observation)
        x = torch.from_numpy(
            cur_x - prev_x if prev_x is not None else np.zeros(D)).float().to(device)
        prev_x = cur_x

        aprob, h = policy(x)
        action = 2 if rs.uniform() < aprob.item() else 3  # 2 is UP, 3 is DOWN in Pong

        xs.append(x)
        hs.append(h)
        y = 1 if action == 2 else 0
        dlogps.append(y - aprob)

        observation, reward, done, info = env.step(action)
        rewards.append(reward)

    epr = np.vstack(rewards)
    discounted_epr = discount_rewards(epr)
    epdlogp = torch.vstack(dlogps)
    # Ensure this tensor is on GPU
    epdlogp *= torch.Tensor(discounted_epr).to(device)
    rewards = np.array(rewards)
    return xs, hs, epdlogp, rewards

# End of preamble.
# From the preamble, verbatim:


# Constants
H = 100  # Number of hidden layer neurons
D = 80 * 80  # Input dimensionality: 80x80 grid
gamma = 0.99  # Discount factor for reward
learning_rate = 1e-4  # Learning rate
episodes = 1000  # Number of training iterations
SEED = 42  # Seed for reproducibility

# Set seeds
np.random.seed(SEED)
torch.manual_seed(SEED)


def preprocess(img):
    img = img[35:195]  # Crop
    img = img[::2, ::2, 0]  # Downsample by factor of 2
    img[img == 144] = 0  # Erase background (type 1)
    img[img == 109] = 0  # Erase background (type 2)
    img[img != 0] = 1  # Everything else (paddles, ball) just set to 1
    return img.astype(np.float64).ravel()


class PolicyNetwork(torch.nn.Module):
    def __init__(self):
        super(PolicyNetwork, self).__init__()
        self.fc1 = torch.nn.Linear(D, H)
        self.fc2 = torch.nn.Linear(H, 1)
        self.relu = torch.nn.ReLU()
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x):
        h = self.relu(self.fc1(x))
        logp = self.fc2(h)
        p = self.sigmoid(logp)
        return p, h


def discount_rewards(r):
    discounted_r = np.zeros_like(r)
    running_add = 0
    for t in reversed(range(0, r.size)):
        if r[t] != 0:
            # Reset the sum, since this was a game boundary (pong specific!)
            running_add = 0
        running_add = running_add * gamma + r[t]
        discounted_r[t] = running_add

    # Standardize the rewards to be unit normal
    discounted_r -= np.mean(discounted_r)
    discounted_r /= np.std(discounted_r)
    return discounted_r


def rollout(policy, env, rs, device):

    observation = env.reset()
    prev_x = None
    xs, hs, dlogps, rewards = [], [], [], []
    done = False

    while not done:
        cur_x = preprocess(observation)
        x = torch.from_numpy(
            cur_x - prev_x if prev_x is not None else np.zeros(D)).float().to(device)
        prev_x = cur_x

        aprob, h = policy(x)
        action = 2 if rs.uniform() < aprob.item() else 3  # 2 is UP, 3 is DOWN in Pong

        xs.append(x)
        hs.append(h)
        y = 1 if action == 2 else 0
        dlogps.append(y - aprob)

        observation, reward, done, info = env.step(action)
        rewards.append(reward)

    epr = np.vstack(rewards)
    discounted_epr = discount_rewards(epr)
    epdlogp = torch.vstack(dlogps)
    # Ensure this tensor is on GPU
    epdlogp *= torch.Tensor(discounted_epr).to(device)
    rewards = np.array(rewards)
    return xs, hs, epdlogp, rewards

# End of preamble.
# From the preamble, verbatim:


# Constants
H = 100  # Number of hidden layer neurons
D = 80 * 80  # Input dimensionality: 80x80 grid
gamma = 0.99  # Discount factor for reward
learning_rate = 1e-4  # Learning rate
episodes = 1000  # Number of training iterations
SEED = 42  # Seed for reproducibility

# Set seeds
np.random.seed(SEED)
torch.manual_seed(SEED)


def preprocess(img):
    img = img[35:195]  # Crop
    img = img[::2, ::2, 0]  # Downsample by factor of 2
    img[img == 144] = 0  # Erase background (type 1)
    img[img == 109] = 0  # Erase background (type 2)
    img[img != 0] = 1  # Everything else (paddles, ball) just set to 1
    return img.astype(np.float64).ravel()


class PolicyNetwork(torch.nn.Module):
    def __init__(self):
        super(PolicyNetwork, self).__init__()
        self.fc1 = torch.nn.Linear(D, H)
        self.fc2 = torch.nn.Linear(H, 1)
        self.relu = torch.nn.ReLU()
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x):
        h = self.relu(self.fc1(x))
        logp = self.fc2(h)
        p = self.sigmoid(logp)
        return p, h


def discount_rewards(r):
    discounted_r = np.zeros_like(r)
    running_add = 0
    for t in reversed(range(0, r.size)):
        if r[t] != 0:
            # Reset the sum, since this was a game boundary (pong specific!)
            running_add = 0
        running_add = running_add * gamma + r[t]
        discounted_r[t] = running_add

    # Standardize the rewards to be unit normal
    discounted_r -= np.mean(discounted_r)
    discounted_r /= np.std(discounted_r)
    return discounted_r


def rollout(policy, env, rs, device):

    observation = env.reset()
    prev_x = None
    xs, hs, dlogps, rewards = [], [], [], []
    done = False

    while not done:
        cur_x = preprocess(observation)
        x = torch.from_numpy(
            cur_x - prev_x if prev_x is not None else np.zeros(D)).float().to(device)
        prev_x = cur_x

        aprob, h = policy(x)
        action = 2 if rs.uniform() < aprob.item() else 3  # 2 is UP, 3 is DOWN in Pong

        xs.append(x)
        hs.append(h)
        y = 1 if action == 2 else 0
        dlogps.append(y - aprob)

        observation, reward, done, info = env.step(action)
        rewards.append(reward)

    epr = np.vstack(rewards)
    discounted_epr = discount_rewards(epr)
    epdlogp = torch.vstack(dlogps)
    # Ensure this tensor is on GPU
    epdlogp *= torch.Tensor(discounted_epr).to(device)
    rewards = np.array(rewards)
    return xs, hs, epdlogp, rewards

# End of preamble.
# From the preamble, verbatim:


# Constants
H = 100  # Number of hidden layer neurons
D = 80 * 80  # Input dimensionality: 80x80 grid
gamma = 0.99  # Discount factor for reward
learning_rate = 1e-4  # Learning rate
episodes = 1000  # Number of training iterations
SEED = 42  # Seed for reproducibility

# Set seeds
np.random.seed(SEED)
torch.manual_seed(SEED)


def preprocess(img):
    img = img[35:195]  # Crop
    img = img[::2, ::2, 0]  # Downsample by factor of 2
    img[img == 144] = 0  # Erase background (type 1)
    img[img == 109] = 0  # Erase background (type 2)
    img[img != 0] = 1  # Everything else (paddles, ball) just set to 1
    return img.astype(np.float64).ravel()


class PolicyNetwork(torch.nn.Module):
    def __init__(self):
        super(PolicyNetwork, self).__init__()
        self.fc1 = torch.nn.Linear(D, H)
        self.fc2 = torch.nn.Linear(H, 1)
        self.relu = torch.nn.ReLU()
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x):
        h = self.relu(self.fc1(x))
        logp = self.fc2(h)
        p = self.sigmoid(logp)
        return p, h


def discount_rewards(r):
    discounted_r = np.zeros_like(r)
    running_add = 0
    for t in reversed(range(0, r.size)):
        if r[t] != 0:
            # Reset the sum, since this was a game boundary (pong specific!)
            running_add = 0
        running_add = running_add * gamma + r[t]
        discounted_r[t] = running_add

    # Standardize the rewards to be unit normal
    discounted_r -= np.mean(discounted_r)
    discounted_r /= np.std(discounted_r)
    return discounted_r


def rollout(policy, env, rs, device):

    observation = env.reset()
    prev_x = None
    xs, hs, dlogps, rewards = [], [], [], []
    done = False

    while not done:
        cur_x = preprocess(observation)
        x = torch.from_numpy(
            cur_x - prev_x if prev_x is not None else np.zeros(D)).float().to(device)
        prev_x = cur_x

        aprob, h = policy(x)
        action = 2 if rs.uniform() < aprob.item() else 3  # 2 is UP, 3 is DOWN in Pong

        xs.append(x)
        hs.append(h)
        y = 1 if action == 2 else 0
        dlogps.append(y - aprob)

        observation, reward, done, info = env.step(action)
        rewards.append(reward)

    epr = np.vstack(rewards)
    discounted_epr = discount_rewards(epr)
    epdlogp = torch.vstack(dlogps)
    # Ensure this tensor is on GPU
    epdlogp *= torch.Tensor(discounted_epr).to(device)
    rewards = np.array(rewards)
    return xs, hs, epdlogp, rewards

# End of preamble.
# From the preamble, verbatim:


# Constants
H = 100  # Number of hidden layer neurons
D = 80 * 80  # Input dimensionality: 80x80 grid
gamma = 0.99  # Discount factor for reward
learning_rate = 1e-4  # Learning rate
episodes = 1000  # Number of training iterations
SEED = 42  # Seed for reproducibility

# Set seeds
np.random.seed(SEED)
torch.manual_seed(SEED)


def preprocess(img):
    img = img[35:195]  # Crop
    img = img[::2, ::2, 0]  # Downsample by factor of 2
    img[img == 144] = 0  # Erase background (type 1)
    img[img == 109] = 0  # Erase background (type 2)
    img[img != 0] = 1  # Everything else (paddles, ball) just set to 1
    return img.astype(np.float64).ravel()


class PolicyNetwork(torch.nn.Module):
    def __init__(self):
        super(PolicyNetwork, self).__init__()
        self.fc1 = torch.nn.Linear(D, H)
        self.fc2 = torch.nn.Linear(H, 1)
        self.relu = torch.nn.ReLU()
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x):
        h = self.relu(self.fc1(x))
        logp = self.fc2(h)
        p = self.sigmoid(logp)
        return p, h


def discount_rewards(r):
    discounted_r = np.zeros_like(r)
    running_add = 0
    for t in reversed(range(0, r.size)):
        if r[t] != 0:
            # Reset the sum, since this was a game boundary (pong specific!)
            running_add = 0
        running_add = running_add * gamma + r[t]
        discounted_r[t] = running_add

    # Standardize the rewards to be unit normal
    discounted_r -= np.mean(discounted_r)
    discounted_r /= np.std(discounted_r)
    return discounted_r


def rollout(policy, env, rs, device):

    observation = env.reset()
    prev_x = None
    xs, hs, dlogps, rewards = [], [], [], []
    done = False

    while not done:
        cur_x = preprocess(observation)
        x = torch.from_numpy(
            cur_x - prev_x if prev_x is not None else np.zeros(D)).float().to(device)
        prev_x = cur_x

        aprob, h = policy(x)
        action = 2 if rs.uniform() < aprob.item() else 3  # 2 is UP, 3 is DOWN in Pong

        xs.append(x)
        hs.append(h)
        y = 1 if action == 2 else 0
        dlogps.append(y - aprob)

        observation, reward, done, info = env.step(action)
        rewards.append(reward)

    epr = np.vstack(rewards)
    discounted_epr = discount_rewards(epr)
    epdlogp = torch.vstack(dlogps)
    # Ensure this tensor is on GPU
    epdlogp *= torch.Tensor(discounted_epr).to(device)
    rewards = np.array(rewards)
    return xs, hs, epdlogp, rewards

# End of preamble.
# From the preamble, verbatim:


# Constants
H = 100  # Number of hidden layer neurons
D = 80 * 80  # Input dimensionality: 80x80 grid
gamma = 0.99  # Discount factor for reward
learning_rate = 1e-4  # Learning rate
episodes = 1000  # Number of training iterations
SEED = 42  # Seed for reproducibility

# Set seeds
np.random.seed(SEED)
torch.manual_seed(SEED)


def preprocess(img):
    img = img[35:195]  # Crop
    img = img[::2, ::2, 0]  # Downsample by factor of 2
    img[img == 144] = 0  # Erase background (type 1)
    img[img == 109] = 0  # Erase background (type 2)
    img[img != 0] = 1  # Everything else (paddles, ball) just set to 1
    return img.astype(np.float64).ravel()


class PolicyNetwork(torch.nn.Module):
    def __init__(self):
        super(PolicyNetwork, self).__init__()
        self.fc1 = torch.nn.Linear(D, H)
        self.fc2 = torch.nn.Linear(H, 1)
        self.relu = torch.nn.ReLU()
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x):
        h = self.relu(self.fc1(x))
        logp = self.fc2(h)
        p = self.sigmoid(logp)
        return p, h


def discount_rewards(r):
    discounted_r = np.zeros_like(r)
    running_add = 0
    for t in reversed(range(0, r.size)):
        if r[t] != 0:
            # Reset the sum, since this was a game boundary (pong specific!)
            running_add = 0
        running_add = running_add * gamma + r[t]
        discounted_r[t] = running_add

    # Standardize the rewards to be unit normal
    discounted_r -= np.mean(discounted_r)
    discounted_r /= np.std(discounted_r)
    return discounted_r


def rollout(policy, env, rs, device):

    observation = env.reset()
    prev_x = None
    xs, hs, dlogps, rewards = [], [], [], []
    done = False

    while not done:
        cur_x = preprocess(observation)
        x = torch.from_numpy(
            cur_x - prev_x if prev_x is not None else np.zeros(D)).float().to(device)
        prev_x = cur_x

        aprob, h = policy(x)
        action = 2 if rs.uniform() < aprob.item() else 3  # 2 is UP, 3 is DOWN in Pong

        xs.append(x)
        hs.append(h)
        y = 1 if action == 2 else 0
        dlogps.append(y - aprob)

        observation, reward, done, info = env.step(action)
        rewards.append(reward)

    epr = np.vstack(rewards)
    discounted_epr = discount_rewards(epr)
    epdlogp = torch.vstack(dlogps)
    # Ensure this tensor is on GPU
    epdlogp *= torch.Tensor(discounted_epr).to(device)
    rewards = np.array(rewards)
    return xs, hs, epdlogp, rewards
# End of preamble.


# Python class for reactor _pong_gpu_main
class __pong_gpu_main:

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
        self.policy = None
        self.env = gym.make("Pong-v0")

    @property
    def bank_index(self):
        return self._bank_index  # pylint: disable=no-member

    def reaction_function_0(self):
        self.rs = RandomState(SEED)
        self.policy = PolicyNetwork().to("cpu")
        return 0

    def reaction_function_1(self, global_parameters, updated_parameters):

        self.policy.load_state_dict(global_parameters.value)
        xs, hs, dlogps, rewards = rollout(
            self.policy, self.env, self.rs, "cpu")
        discounted_epr = discount_rewards(np.vstack(rewards))
        res = [xs, hs, dlogps, discounted_epr, np.sum(rewards)]
        updated_parameters.set(res)
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
        self.results = None
        self.round_num = None
        self.start_time = None

    @property
    def bank_index(self):
        return self._bank_index  # pylint: disable=no-member

    def reaction_function_0(self, global_parameters):

        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu")
        self.model = PolicyNetwork().to(self.device)
        self.optimizer = torch.optim.RMSprop(
            self.model.parameters(), lr=learning_rate)

        self.start_time = time.time()
        self.round_num = 0
        self.running_reward = None
        model_weights_cpu = {k: v.to("cpu")
                             for k, v in self.model.state_dict().items()}
        global_parameters.set(model_weights_cpu)
        return 0

    def reaction_function_1(self, updated_parameters, global_parameters):

        reward_sum = 0
        all_xs, all_hs, all_dlogps, all_discounted_epr = [], [], [], []

        for i in range(4):
            xs = updated_parameters[i].value[0]
            hs = updated_parameters[i].value[1]
            dlogps = updated_parameters[i].value[2]
            discounted_epr = updated_parameters[i].value[3]
            rewards = updated_parameters[i].value[4]

            all_xs.extend(xs)
            all_hs.extend(hs)
            all_dlogps.extend(dlogps)
            all_discounted_epr.extend(discounted_epr)
            reward_sum += rewards

        all_xs = torch.stack(all_xs).to(self.device)
        all_hs = torch.stack(all_hs).to(self.device)
        all_dlogps = torch.stack(all_dlogps).squeeze().to(self.device)
        all_discounted_epr = torch.tensor(
            np.array(all_discounted_epr), dtype=torch.float32).to(self.device)

        # Ensure all_dlogps has the same shape as all_hs for element-wise multiplication
        all_dlogps = all_dlogps.view(-1, 1).expand_as(all_hs)

        # Calculate loss
        weighted_log_probs = (all_hs * all_dlogps).sum(dim=1)
        loss = -(weighted_log_probs * all_discounted_epr).sum()

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        # last round
        if self.round_num == episodes:
            print(
                f"Total time taken: {time.time() - self.start_time:.2f} seconds")
            request_stop()

        # first round
        if int(self.round_num) == 0:
            self.start_time = time.time()

        # print round number
        print("Episode: "+str(self.round_num))
        self.round_num += 1

        # print running reward
        print("Reward: " + str(reward_sum/4))

        print(
            f"Training Time: {time.time() - self.start_time:.2f} seconds" + " \n")

        model_weights_cpu = {k: v.to("cpu")
                             for k, v in self.model.state_dict().items()}

        global_parameters.set(model_weights_cpu)
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
pong_gpu_main_lf = [None] * 1
pong_gpu_client_lf = [None] * 4
pong_gpu_server_lf = [None] * 1
pong_gpu_delay_lf = [None] * 1
# Start initializing pong_gpu of class _pong_gpu_main
for pong_gpu_main_i in range(1):
    bank_index = pong_gpu_main_i
    pong_gpu_main_lf[0] = __pong_gpu_main(
        _bank_index=0,
    )
    # Start initializing pong_gpu.client of class _clientreactor
    for pong_gpu_client_i in range(4):
        bank_index = pong_gpu_client_i
        pong_gpu_client_lf[pong_gpu_client_i] = __clientreactor(
            _bank_index=pong_gpu_client_i,
        )
    # Start initializing pong_gpu.server of class _serverreactor
    for pong_gpu_server_i in range(1):
        bank_index = pong_gpu_server_i
        pong_gpu_server_lf[0] = __serverreactor(
            _bank_index=0,
        )
    # Start initializing pong_gpu.delay of class __lf_gendelay_0
    for pong_gpu_delay_i in range(1):
        bank_index = pong_gpu_delay_i
        pong_gpu_delay_lf[0] = ___lf_gendelay_0(
            _bank_index=pong_gpu_delay_i,
            _delay=0,
        )


# The main function
def main(argv):
    start(argv)


# As is customary in Python programs, the main() function
# should only be executed if the main module is active.
if __name__ == "__main__":
    main(sys.argv)
