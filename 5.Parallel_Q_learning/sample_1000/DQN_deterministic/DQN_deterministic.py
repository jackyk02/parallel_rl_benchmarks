import random
from random import sample
from collections import deque
import numpy as np
import torch.optim as optim
import torch.nn as nn
import torch
import gym
import time
import copy
import LinguaFrancaDQN_deterministic as lf
from LinguaFrancaDQN_deterministic import (
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
# Import packages

# Define the Q-Network


class QNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(QNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)
        self.relu = nn.ReLU()

    def forward(self, state):
        x = self.relu(self.fc1(state))
        x = self.fc2(x)
        return x


# Q-Network and Optimizer (in main process)
device = "cuda" if torch.cuda.is_available() else "cpu"
torch.manual_seed(1)
q_net = QNetwork(3, 32, 2).to(device)
target_net = QNetwork(3, 32, 2).to(device)
target_net.load_state_dict(q_net.state_dict())
target_net.eval()
optimizer = optim.Adam(q_net.parameters(), lr=0.01)
epsilon = 0.1


def update_q_network(batch, gamma=0.99):
    torch.manual_seed(1)
    torch.cuda.manual_seed_all(1)
    states, actions, rewards, next_states, dones = zip(*batch)
    states = torch.cat(states).to(device)
    next_states = torch.cat(next_states).to(device)
    actions = torch.tensor(actions).to(device)
    rewards = torch.tensor(rewards, dtype=torch.float32).to(device)
    dones = torch.tensor(dones, dtype=torch.float32).to(device)

    current_q_values = q_net(states).gather(
        1, actions.unsqueeze(-1)).squeeze(-1)
    next_q_values = target_net(next_states).max(1)[0]
    expected_q_values = rewards + gamma * next_q_values * (1 - dones)

    loss = nn.MSELoss()(current_q_values, expected_q_values.detach())

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()


def log_dict_to_file(all_experiences):
    import datetime
    import os
    # Getting the current time to use in the filename
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # File path for logging in the current directory
    file_path = f"all_experiences_{current_time}.txt"

    # Writing the experiences to a file
    with open(file_path, "w") as file:
        for key, value in all_experiences.items():
            file.write(f"{key}: {value}\n")

    return os.path.abspath(file_path)

# End of preamble.
# From the preamble, verbatim:
# Import packages

# Define the Q-Network


class QNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(QNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)
        self.relu = nn.ReLU()

    def forward(self, state):
        x = self.relu(self.fc1(state))
        x = self.fc2(x)
        return x


# Q-Network and Optimizer (in main process)
device = "cuda" if torch.cuda.is_available() else "cpu"
torch.manual_seed(1)
q_net = QNetwork(3, 32, 2).to(device)
target_net = QNetwork(3, 32, 2).to(device)
target_net.load_state_dict(q_net.state_dict())
target_net.eval()
optimizer = optim.Adam(q_net.parameters(), lr=0.01)
epsilon = 0.1


def update_q_network(batch, gamma=0.99):
    torch.manual_seed(1)
    torch.cuda.manual_seed_all(1)
    states, actions, rewards, next_states, dones = zip(*batch)
    states = torch.cat(states).to(device)
    next_states = torch.cat(next_states).to(device)
    actions = torch.tensor(actions).to(device)
    rewards = torch.tensor(rewards, dtype=torch.float32).to(device)
    dones = torch.tensor(dones, dtype=torch.float32).to(device)

    current_q_values = q_net(states).gather(
        1, actions.unsqueeze(-1)).squeeze(-1)
    next_q_values = target_net(next_states).max(1)[0]
    expected_q_values = rewards + gamma * next_q_values * (1 - dones)

    loss = nn.MSELoss()(current_q_values, expected_q_values.detach())

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()


def log_dict_to_file(all_experiences):
    import datetime
    import os
    # Getting the current time to use in the filename
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # File path for logging in the current directory
    file_path = f"all_experiences_{current_time}.txt"

    # Writing the experiences to a file
    with open(file_path, "w") as file:
        for key, value in all_experiences.items():
            file.write(f"{key}: {value}\n")

    return os.path.abspath(file_path)

# End of preamble.
# From the preamble, verbatim:
# Import packages

# Define the Q-Network


class QNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(QNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)
        self.relu = nn.ReLU()

    def forward(self, state):
        x = self.relu(self.fc1(state))
        x = self.fc2(x)
        return x


# Q-Network and Optimizer (in main process)
device = "cuda" if torch.cuda.is_available() else "cpu"
torch.manual_seed(1)
q_net = QNetwork(3, 32, 2).to(device)
target_net = QNetwork(3, 32, 2).to(device)
target_net.load_state_dict(q_net.state_dict())
target_net.eval()
optimizer = optim.Adam(q_net.parameters(), lr=0.01)
epsilon = 0.1


def update_q_network(batch, gamma=0.99):
    torch.manual_seed(1)
    torch.cuda.manual_seed_all(1)
    states, actions, rewards, next_states, dones = zip(*batch)
    states = torch.cat(states).to(device)
    next_states = torch.cat(next_states).to(device)
    actions = torch.tensor(actions).to(device)
    rewards = torch.tensor(rewards, dtype=torch.float32).to(device)
    dones = torch.tensor(dones, dtype=torch.float32).to(device)

    current_q_values = q_net(states).gather(
        1, actions.unsqueeze(-1)).squeeze(-1)
    next_q_values = target_net(next_states).max(1)[0]
    expected_q_values = rewards + gamma * next_q_values * (1 - dones)

    loss = nn.MSELoss()(current_q_values, expected_q_values.detach())

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()


def log_dict_to_file(all_experiences):
    import datetime
    import os
    # Getting the current time to use in the filename
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # File path for logging in the current directory
    file_path = f"all_experiences_{current_time}.txt"

    # Writing the experiences to a file
    with open(file_path, "w") as file:
        for key, value in all_experiences.items():
            file.write(f"{key}: {value}\n")

    return os.path.abspath(file_path)

# End of preamble.
# From the preamble, verbatim:
# Import packages

# Define the Q-Network


class QNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(QNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)
        self.relu = nn.ReLU()

    def forward(self, state):
        x = self.relu(self.fc1(state))
        x = self.fc2(x)
        return x


# Q-Network and Optimizer (in main process)
device = "cuda" if torch.cuda.is_available() else "cpu"
torch.manual_seed(1)
q_net = QNetwork(3, 32, 2).to(device)
target_net = QNetwork(3, 32, 2).to(device)
target_net.load_state_dict(q_net.state_dict())
target_net.eval()
optimizer = optim.Adam(q_net.parameters(), lr=0.01)
epsilon = 0.1


def update_q_network(batch, gamma=0.99):
    torch.manual_seed(1)
    torch.cuda.manual_seed_all(1)
    states, actions, rewards, next_states, dones = zip(*batch)
    states = torch.cat(states).to(device)
    next_states = torch.cat(next_states).to(device)
    actions = torch.tensor(actions).to(device)
    rewards = torch.tensor(rewards, dtype=torch.float32).to(device)
    dones = torch.tensor(dones, dtype=torch.float32).to(device)

    current_q_values = q_net(states).gather(
        1, actions.unsqueeze(-1)).squeeze(-1)
    next_q_values = target_net(next_states).max(1)[0]
    expected_q_values = rewards + gamma * next_q_values * (1 - dones)

    loss = nn.MSELoss()(current_q_values, expected_q_values.detach())

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()


def log_dict_to_file(all_experiences):
    import datetime
    import os
    # Getting the current time to use in the filename
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # File path for logging in the current directory
    file_path = f"all_experiences_{current_time}.txt"

    # Writing the experiences to a file
    with open(file_path, "w") as file:
        for key, value in all_experiences.items():
            file.write(f"{key}: {value}\n")

    return os.path.abspath(file_path)

# End of preamble.
# From the preamble, verbatim:
# Import packages

# Define the Q-Network


class QNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(QNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)
        self.relu = nn.ReLU()

    def forward(self, state):
        x = self.relu(self.fc1(state))
        x = self.fc2(x)
        return x


# Q-Network and Optimizer (in main process)
device = "cuda" if torch.cuda.is_available() else "cpu"
torch.manual_seed(1)
q_net = QNetwork(3, 32, 2).to(device)
target_net = QNetwork(3, 32, 2).to(device)
target_net.load_state_dict(q_net.state_dict())
target_net.eval()
optimizer = optim.Adam(q_net.parameters(), lr=0.01)
epsilon = 0.1


def update_q_network(batch, gamma=0.99):
    torch.manual_seed(1)
    torch.cuda.manual_seed_all(1)
    states, actions, rewards, next_states, dones = zip(*batch)
    states = torch.cat(states).to(device)
    next_states = torch.cat(next_states).to(device)
    actions = torch.tensor(actions).to(device)
    rewards = torch.tensor(rewards, dtype=torch.float32).to(device)
    dones = torch.tensor(dones, dtype=torch.float32).to(device)

    current_q_values = q_net(states).gather(
        1, actions.unsqueeze(-1)).squeeze(-1)
    next_q_values = target_net(next_states).max(1)[0]
    expected_q_values = rewards + gamma * next_q_values * (1 - dones)

    loss = nn.MSELoss()(current_q_values, expected_q_values.detach())

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()


def log_dict_to_file(all_experiences):
    import datetime
    import os
    # Getting the current time to use in the filename
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # File path for logging in the current directory
    file_path = f"all_experiences_{current_time}.txt"

    # Writing the experiences to a file
    with open(file_path, "w") as file:
        for key, value in all_experiences.items():
            file.write(f"{key}: {value}\n")

    return os.path.abspath(file_path)

# End of preamble.
# From the preamble, verbatim:
# Import packages

# Define the Q-Network


class QNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(QNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)
        self.relu = nn.ReLU()

    def forward(self, state):
        x = self.relu(self.fc1(state))
        x = self.fc2(x)
        return x


# Q-Network and Optimizer (in main process)
device = "cuda" if torch.cuda.is_available() else "cpu"
torch.manual_seed(1)
q_net = QNetwork(3, 32, 2).to(device)
target_net = QNetwork(3, 32, 2).to(device)
target_net.load_state_dict(q_net.state_dict())
target_net.eval()
optimizer = optim.Adam(q_net.parameters(), lr=0.01)
epsilon = 0.1


def update_q_network(batch, gamma=0.99):
    torch.manual_seed(1)
    torch.cuda.manual_seed_all(1)
    states, actions, rewards, next_states, dones = zip(*batch)
    states = torch.cat(states).to(device)
    next_states = torch.cat(next_states).to(device)
    actions = torch.tensor(actions).to(device)
    rewards = torch.tensor(rewards, dtype=torch.float32).to(device)
    dones = torch.tensor(dones, dtype=torch.float32).to(device)

    current_q_values = q_net(states).gather(
        1, actions.unsqueeze(-1)).squeeze(-1)
    next_q_values = target_net(next_states).max(1)[0]
    expected_q_values = rewards + gamma * next_q_values * (1 - dones)

    loss = nn.MSELoss()(current_q_values, expected_q_values.detach())

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()


def log_dict_to_file(all_experiences):
    import datetime
    import os
    # Getting the current time to use in the filename
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # File path for logging in the current directory
    file_path = f"all_experiences_{current_time}.txt"

    # Writing the experiences to a file
    with open(file_path, "w") as file:
        for key, value in all_experiences.items():
            file.write(f"{key}: {value}\n")

    return os.path.abspath(file_path)

# End of preamble.
# From the preamble, verbatim:
# Import packages

# Define the Q-Network


class QNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(QNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)
        self.relu = nn.ReLU()

    def forward(self, state):
        x = self.relu(self.fc1(state))
        x = self.fc2(x)
        return x


# Q-Network and Optimizer (in main process)
device = "cuda" if torch.cuda.is_available() else "cpu"
torch.manual_seed(1)
q_net = QNetwork(3, 32, 2).to(device)
target_net = QNetwork(3, 32, 2).to(device)
target_net.load_state_dict(q_net.state_dict())
target_net.eval()
optimizer = optim.Adam(q_net.parameters(), lr=0.01)
epsilon = 0.1


def update_q_network(batch, gamma=0.99):
    torch.manual_seed(1)
    torch.cuda.manual_seed_all(1)
    states, actions, rewards, next_states, dones = zip(*batch)
    states = torch.cat(states).to(device)
    next_states = torch.cat(next_states).to(device)
    actions = torch.tensor(actions).to(device)
    rewards = torch.tensor(rewards, dtype=torch.float32).to(device)
    dones = torch.tensor(dones, dtype=torch.float32).to(device)

    current_q_values = q_net(states).gather(
        1, actions.unsqueeze(-1)).squeeze(-1)
    next_q_values = target_net(next_states).max(1)[0]
    expected_q_values = rewards + gamma * next_q_values * (1 - dones)

    loss = nn.MSELoss()(current_q_values, expected_q_values.detach())

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()


def log_dict_to_file(all_experiences):
    import datetime
    import os
    # Getting the current time to use in the filename
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # File path for logging in the current directory
    file_path = f"all_experiences_{current_time}.txt"

    # Writing the experiences to a file
    with open(file_path, "w") as file:
        for key, value in all_experiences.items():
            file.write(f"{key}: {value}\n")

    return os.path.abspath(file_path)

# End of preamble.
# From the preamble, verbatim:
# Import packages

# Define the Q-Network


class QNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(QNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)
        self.relu = nn.ReLU()

    def forward(self, state):
        x = self.relu(self.fc1(state))
        x = self.fc2(x)
        return x


# Q-Network and Optimizer (in main process)
device = "cuda" if torch.cuda.is_available() else "cpu"
torch.manual_seed(1)
q_net = QNetwork(3, 32, 2).to(device)
target_net = QNetwork(3, 32, 2).to(device)
target_net.load_state_dict(q_net.state_dict())
target_net.eval()
optimizer = optim.Adam(q_net.parameters(), lr=0.01)
epsilon = 0.1


def update_q_network(batch, gamma=0.99):
    torch.manual_seed(1)
    torch.cuda.manual_seed_all(1)
    states, actions, rewards, next_states, dones = zip(*batch)
    states = torch.cat(states).to(device)
    next_states = torch.cat(next_states).to(device)
    actions = torch.tensor(actions).to(device)
    rewards = torch.tensor(rewards, dtype=torch.float32).to(device)
    dones = torch.tensor(dones, dtype=torch.float32).to(device)

    current_q_values = q_net(states).gather(
        1, actions.unsqueeze(-1)).squeeze(-1)
    next_q_values = target_net(next_states).max(1)[0]
    expected_q_values = rewards + gamma * next_q_values * (1 - dones)

    loss = nn.MSELoss()(current_q_values, expected_q_values.detach())

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()


def log_dict_to_file(all_experiences):
    import datetime
    import os
    # Getting the current time to use in the filename
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # File path for logging in the current directory
    file_path = f"all_experiences_{current_time}.txt"

    # Writing the experiences to a file
    with open(file_path, "w") as file:
        for key, value in all_experiences.items():
            file.write(f"{key}: {value}\n")

    return os.path.abspath(file_path)

# End of preamble.
# From the preamble, verbatim:
# Import packages

# Define the Q-Network


class QNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(QNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)
        self.relu = nn.ReLU()

    def forward(self, state):
        x = self.relu(self.fc1(state))
        x = self.fc2(x)
        return x


# Q-Network and Optimizer (in main process)
device = "cuda" if torch.cuda.is_available() else "cpu"
torch.manual_seed(1)
q_net = QNetwork(3, 32, 2).to(device)
target_net = QNetwork(3, 32, 2).to(device)
target_net.load_state_dict(q_net.state_dict())
target_net.eval()
optimizer = optim.Adam(q_net.parameters(), lr=0.01)
epsilon = 0.1


def update_q_network(batch, gamma=0.99):
    torch.manual_seed(1)
    torch.cuda.manual_seed_all(1)
    states, actions, rewards, next_states, dones = zip(*batch)
    states = torch.cat(states).to(device)
    next_states = torch.cat(next_states).to(device)
    actions = torch.tensor(actions).to(device)
    rewards = torch.tensor(rewards, dtype=torch.float32).to(device)
    dones = torch.tensor(dones, dtype=torch.float32).to(device)

    current_q_values = q_net(states).gather(
        1, actions.unsqueeze(-1)).squeeze(-1)
    next_q_values = target_net(next_states).max(1)[0]
    expected_q_values = rewards + gamma * next_q_values * (1 - dones)

    loss = nn.MSELoss()(current_q_values, expected_q_values.detach())

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()


def log_dict_to_file(all_experiences):
    import datetime
    import os
    # Getting the current time to use in the filename
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # File path for logging in the current directory
    file_path = f"all_experiences_{current_time}.txt"

    # Writing the experiences to a file
    with open(file_path, "w") as file:
        for key, value in all_experiences.items():
            file.write(f"{key}: {value}\n")

    return os.path.abspath(file_path)

# End of preamble.
# From the preamble, verbatim:
# Import packages

# Define the Q-Network


class QNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(QNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)
        self.relu = nn.ReLU()

    def forward(self, state):
        x = self.relu(self.fc1(state))
        x = self.fc2(x)
        return x


# Q-Network and Optimizer (in main process)
device = "cuda" if torch.cuda.is_available() else "cpu"
torch.manual_seed(1)
q_net = QNetwork(3, 32, 2).to(device)
target_net = QNetwork(3, 32, 2).to(device)
target_net.load_state_dict(q_net.state_dict())
target_net.eval()
optimizer = optim.Adam(q_net.parameters(), lr=0.01)
epsilon = 0.1


def update_q_network(batch, gamma=0.99):
    torch.manual_seed(1)
    torch.cuda.manual_seed_all(1)
    states, actions, rewards, next_states, dones = zip(*batch)
    states = torch.cat(states).to(device)
    next_states = torch.cat(next_states).to(device)
    actions = torch.tensor(actions).to(device)
    rewards = torch.tensor(rewards, dtype=torch.float32).to(device)
    dones = torch.tensor(dones, dtype=torch.float32).to(device)

    current_q_values = q_net(states).gather(
        1, actions.unsqueeze(-1)).squeeze(-1)
    next_q_values = target_net(next_states).max(1)[0]
    expected_q_values = rewards + gamma * next_q_values * (1 - dones)

    loss = nn.MSELoss()(current_q_values, expected_q_values.detach())

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()


def log_dict_to_file(all_experiences):
    import datetime
    import os
    # Getting the current time to use in the filename
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # File path for logging in the current directory
    file_path = f"all_experiences_{current_time}.txt"

    # Writing the experiences to a file
    with open(file_path, "w") as file:
        for key, value in all_experiences.items():
            file.write(f"{key}: {value}\n")

    return os.path.abspath(file_path)
# End of preamble.


# Python class for reactor _dqn_deterministic_main
class __dqn_deterministic_main:

    # Constructor
    def __init__(self, **kwargs):
        # Define parameters and their default values
        # Handle parameters that are set in instantiation
        self.__dict__.update(kwargs)
        # Define state variables

    @property
    def bank_index(self):
        return self._bank_index  # pylint: disable=no-member


# Python class for reactor _rolloutreactor
class __rolloutreactor:

    # Constructor
    def __init__(self, **kwargs):
        # Define parameters and their default values
        # Handle parameters that are set in instantiation
        self.__dict__.update(kwargs)
        # Define state variables
        self.env = None
        self.obs = None
        self.q_net = None
        self.rng = None

    @property
    def bank_index(self):
        return self._bank_index  # pylint: disable=no-member

    def reaction_function_0(self):

        random.seed(1)
        self.env = gym.make("Blackjack-v1")
        self.env.seed(1)
        self.obs = self.env.reset()
        self.rng = np.random.RandomState(1)
        self.q_net = QNetwork(3, 32, 2).to("cpu")
        return 0

    def reaction_function_1(self, gradients, trajectories):

        random.seed(1)
        self.q_net.load_state_dict(gradients.value)
        experiences = []

        for _ in range(100):
            state_tensor = torch.from_numpy(
                np.array(self.obs)).float().unsqueeze(0)
            if self.rng.uniform(0, 1) < epsilon:
                action = self.rng.randint(0, 2)
            else:
                with torch.no_grad():
                    action = self.q_net(state_tensor).max(1)[1].item()

            next_state, reward, done, _ = self.env.step(action)
            next_state_tensor = torch.from_numpy(
                np.array(next_state)).float().unsqueeze(0)  # Convert to tensor
            # Use tensor here
            experiences.append(
                (state_tensor, action, reward, next_state_tensor, done))

            if done:
                self.obs = self.env.reset()
            else:
                self.obs = next_state

        trajectories.set(experiences)
        return 0

# Python class for reactor _replaybufferreactor


class __replaybufferreactor:

    # Constructor
    def __init__(self, **kwargs):
        # Define parameters and their default values
        # Handle parameters that are set in instantiation
        self.__dict__.update(kwargs)
        # Define state variables
        self.experiences = None

    @property
    def bank_index(self):
        return self._bank_index  # pylint: disable=no-member

    def reaction_function_0(self):

        # Initialize ReplayBuffer
        self.experiences = deque(maxlen=20000)
        return 0

    def reaction_function_1(self, trajectories, dataset):

        # Append Trajectories into ReplayBuffer
        for i in range(16):
            new_experiences = trajectories[i].value
            if new_experiences is not None:
                self.experiences.extend(new_experiences)

        result = list(self.experiences)[:min(1000, len(self.experiences))]
        dataset.set(result)
        return 0

# Python class for reactor _learnerreactor


class __learnerreactor:

    # Constructor
    def __init__(self, **kwargs):
        # Define parameters and their default values
        # Handle parameters that are set in instantiation
        self.__dict__.update(kwargs)
        # Define state variables
        self.start_time = None
        self.q_net_state = None
        self.round = None

    @property
    def bank_index(self):
        return self._bank_index  # pylint: disable=no-member

    def reaction_function_0(self, gradients):

        # Initialize the policy
        self.start_time = time.time()
        self.round = 0
        self.q_net_state = {key: tensor.to(
            "cpu") for key, tensor in q_net.state_dict().items()}
        gradients.set(self.q_net_state)
        return 0

    def reaction_function_1(self, dataset, gradients):

        random.seed(1)
        # Update the policy
        batch = dataset.value
        if batch:
            update_q_network(batch)

        self.q_net_state = {key: tensor.to(
            "cpu") for key, tensor in q_net.state_dict().items()}
        print(self.q_net_state["fc1.weight"][5])
        if self.round % 10 == 0:  # Update target network every 10 rounds
            target_net.load_state_dict(q_net.state_dict())

        print(
            f"Round {self.round}, Training Time: {time.time()-self.start_time:.2f}")
        self.round += 1

        log_dict_to_file(self.q_net_state)

        gradients.set(self.q_net_state)
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
dqn_deterministic_main_lf = [None] * 1
dqn_deterministic_rollout_lf = [None] * 16
dqn_deterministic_replay_lf = [None] * 1
dqn_deterministic_learner_lf = [None] * 1
dqn_deterministic_delay_lf = [None] * 1
# Start initializing DQN_deterministic of class _dqn_deterministic_main
for dqn_deterministic_main_i in range(1):
    bank_index = dqn_deterministic_main_i
    dqn_deterministic_main_lf[0] = __dqn_deterministic_main(
        _bank_index=0,
    )
    # Start initializing DQN_deterministic.rollout of class _rolloutreactor
    for dqn_deterministic_rollout_i in range(16):
        bank_index = dqn_deterministic_rollout_i
        dqn_deterministic_rollout_lf[dqn_deterministic_rollout_i] = __rolloutreactor(
            _bank_index=dqn_deterministic_rollout_i,
        )
    # Start initializing DQN_deterministic.replay of class _replaybufferreactor
    for dqn_deterministic_replay_i in range(1):
        bank_index = dqn_deterministic_replay_i
        dqn_deterministic_replay_lf[0] = __replaybufferreactor(
            _bank_index=0,
        )
    # Start initializing DQN_deterministic.learner of class _learnerreactor
    for dqn_deterministic_learner_i in range(1):
        bank_index = dqn_deterministic_learner_i
        dqn_deterministic_learner_lf[0] = __learnerreactor(
            _bank_index=0,
        )
    # Start initializing DQN_deterministic.delay of class __lf_gendelay_0
    for dqn_deterministic_delay_i in range(1):
        bank_index = dqn_deterministic_delay_i
        dqn_deterministic_delay_lf[0] = ___lf_gendelay_0(
            _bank_index=dqn_deterministic_delay_i,
            _delay=0,
        )


# The main function
def main(argv):
    start(argv)


# As is customary in Python programs, the main() function
# should only be executed if the main module is active.
if __name__ == "__main__":
    main(sys.argv)
