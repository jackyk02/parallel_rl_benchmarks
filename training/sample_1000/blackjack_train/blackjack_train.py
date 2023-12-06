from torch.distributions import Categorical
from collections import deque
import numpy as np
import torch.optim as optim
import torch.nn as nn
import torch
import gym
import time
import copy
import LinguaFrancablackjack_train as lf
from LinguaFrancablackjack_train import (
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

# Define the Policy Network


class PolicyNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(PolicyNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)  # Additional layer
        self.relu = nn.ReLU()
        self.softmax = nn.Softmax(dim=1)

    def forward(self, state):
        x = self.relu(self.fc1(state))
        x = self.fc2(x)
        action_probs = self.softmax(x)
        return action_probs


# Policy Network and Optimizer (in main process)
device = "cuda" if torch.cuda.is_available() else "cpu"
policy_net = PolicyNetwork(3, 32, 2).to(device)
optimizer = optim.Adam(policy_net.parameters(), lr=0.01)


def update_policy_network(batch):
    if batch is None:
        return
    state_tensors, actions, rewards = zip(*batch)

    state_tensors = torch.cat(state_tensors).to(device)
    actions = torch.tensor(actions).to(device)
    rewards = torch.tensor(rewards, dtype=torch.float32).to(device)

    action_probs = policy_net(state_tensors)
    action_log_probs = torch.log(action_probs + 1e-8)

    selected_log_probs = action_log_probs[torch.arange(
        action_log_probs.size(0)), actions]
    loss = -torch.sum(selected_log_probs * rewards)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# End of preamble.
# From the preamble, verbatim:
# Import packages

# Define the Policy Network


class PolicyNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(PolicyNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)  # Additional layer
        self.relu = nn.ReLU()
        self.softmax = nn.Softmax(dim=1)

    def forward(self, state):
        x = self.relu(self.fc1(state))
        x = self.fc2(x)
        action_probs = self.softmax(x)
        return action_probs


# Policy Network and Optimizer (in main process)
device = "cuda" if torch.cuda.is_available() else "cpu"
policy_net = PolicyNetwork(3, 32, 2).to(device)
optimizer = optim.Adam(policy_net.parameters(), lr=0.01)


def update_policy_network(batch):
    if batch is None:
        return
    state_tensors, actions, rewards = zip(*batch)

    state_tensors = torch.cat(state_tensors).to(device)
    actions = torch.tensor(actions).to(device)
    rewards = torch.tensor(rewards, dtype=torch.float32).to(device)

    action_probs = policy_net(state_tensors)
    action_log_probs = torch.log(action_probs + 1e-8)

    selected_log_probs = action_log_probs[torch.arange(
        action_log_probs.size(0)), actions]
    loss = -torch.sum(selected_log_probs * rewards)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# End of preamble.
# From the preamble, verbatim:
# Import packages

# Define the Policy Network


class PolicyNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(PolicyNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)  # Additional layer
        self.relu = nn.ReLU()
        self.softmax = nn.Softmax(dim=1)

    def forward(self, state):
        x = self.relu(self.fc1(state))
        x = self.fc2(x)
        action_probs = self.softmax(x)
        return action_probs


# Policy Network and Optimizer (in main process)
device = "cuda" if torch.cuda.is_available() else "cpu"
policy_net = PolicyNetwork(3, 32, 2).to(device)
optimizer = optim.Adam(policy_net.parameters(), lr=0.01)


def update_policy_network(batch):
    if batch is None:
        return
    state_tensors, actions, rewards = zip(*batch)

    state_tensors = torch.cat(state_tensors).to(device)
    actions = torch.tensor(actions).to(device)
    rewards = torch.tensor(rewards, dtype=torch.float32).to(device)

    action_probs = policy_net(state_tensors)
    action_log_probs = torch.log(action_probs + 1e-8)

    selected_log_probs = action_log_probs[torch.arange(
        action_log_probs.size(0)), actions]
    loss = -torch.sum(selected_log_probs * rewards)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# End of preamble.
# From the preamble, verbatim:
# Import packages

# Define the Policy Network


class PolicyNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(PolicyNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)  # Additional layer
        self.relu = nn.ReLU()
        self.softmax = nn.Softmax(dim=1)

    def forward(self, state):
        x = self.relu(self.fc1(state))
        x = self.fc2(x)
        action_probs = self.softmax(x)
        return action_probs


# Policy Network and Optimizer (in main process)
device = "cuda" if torch.cuda.is_available() else "cpu"
policy_net = PolicyNetwork(3, 32, 2).to(device)
optimizer = optim.Adam(policy_net.parameters(), lr=0.01)


def update_policy_network(batch):
    if batch is None:
        return
    state_tensors, actions, rewards = zip(*batch)

    state_tensors = torch.cat(state_tensors).to(device)
    actions = torch.tensor(actions).to(device)
    rewards = torch.tensor(rewards, dtype=torch.float32).to(device)

    action_probs = policy_net(state_tensors)
    action_log_probs = torch.log(action_probs + 1e-8)

    selected_log_probs = action_log_probs[torch.arange(
        action_log_probs.size(0)), actions]
    loss = -torch.sum(selected_log_probs * rewards)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# End of preamble.
# From the preamble, verbatim:
# Import packages

# Define the Policy Network


class PolicyNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(PolicyNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)  # Additional layer
        self.relu = nn.ReLU()
        self.softmax = nn.Softmax(dim=1)

    def forward(self, state):
        x = self.relu(self.fc1(state))
        x = self.fc2(x)
        action_probs = self.softmax(x)
        return action_probs


# Policy Network and Optimizer (in main process)
device = "cuda" if torch.cuda.is_available() else "cpu"
policy_net = PolicyNetwork(3, 32, 2).to(device)
optimizer = optim.Adam(policy_net.parameters(), lr=0.01)


def update_policy_network(batch):
    if batch is None:
        return
    state_tensors, actions, rewards = zip(*batch)

    state_tensors = torch.cat(state_tensors).to(device)
    actions = torch.tensor(actions).to(device)
    rewards = torch.tensor(rewards, dtype=torch.float32).to(device)

    action_probs = policy_net(state_tensors)
    action_log_probs = torch.log(action_probs + 1e-8)

    selected_log_probs = action_log_probs[torch.arange(
        action_log_probs.size(0)), actions]
    loss = -torch.sum(selected_log_probs * rewards)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# End of preamble.
# From the preamble, verbatim:
# Import packages

# Define the Policy Network


class PolicyNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(PolicyNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)  # Additional layer
        self.relu = nn.ReLU()
        self.softmax = nn.Softmax(dim=1)

    def forward(self, state):
        x = self.relu(self.fc1(state))
        x = self.fc2(x)
        action_probs = self.softmax(x)
        return action_probs


# Policy Network and Optimizer (in main process)
device = "cuda" if torch.cuda.is_available() else "cpu"
policy_net = PolicyNetwork(3, 32, 2).to(device)
optimizer = optim.Adam(policy_net.parameters(), lr=0.01)


def update_policy_network(batch):
    if batch is None:
        return
    state_tensors, actions, rewards = zip(*batch)

    state_tensors = torch.cat(state_tensors).to(device)
    actions = torch.tensor(actions).to(device)
    rewards = torch.tensor(rewards, dtype=torch.float32).to(device)

    action_probs = policy_net(state_tensors)
    action_log_probs = torch.log(action_probs + 1e-8)

    selected_log_probs = action_log_probs[torch.arange(
        action_log_probs.size(0)), actions]
    loss = -torch.sum(selected_log_probs * rewards)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# End of preamble.
# From the preamble, verbatim:
# Import packages

# Define the Policy Network


class PolicyNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(PolicyNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)  # Additional layer
        self.relu = nn.ReLU()
        self.softmax = nn.Softmax(dim=1)

    def forward(self, state):
        x = self.relu(self.fc1(state))
        x = self.fc2(x)
        action_probs = self.softmax(x)
        return action_probs


# Policy Network and Optimizer (in main process)
device = "cuda" if torch.cuda.is_available() else "cpu"
policy_net = PolicyNetwork(3, 32, 2).to(device)
optimizer = optim.Adam(policy_net.parameters(), lr=0.01)


def update_policy_network(batch):
    if batch is None:
        return
    state_tensors, actions, rewards = zip(*batch)

    state_tensors = torch.cat(state_tensors).to(device)
    actions = torch.tensor(actions).to(device)
    rewards = torch.tensor(rewards, dtype=torch.float32).to(device)

    action_probs = policy_net(state_tensors)
    action_log_probs = torch.log(action_probs + 1e-8)

    selected_log_probs = action_log_probs[torch.arange(
        action_log_probs.size(0)), actions]
    loss = -torch.sum(selected_log_probs * rewards)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# End of preamble.
# From the preamble, verbatim:
# Import packages

# Define the Policy Network


class PolicyNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(PolicyNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)  # Additional layer
        self.relu = nn.ReLU()
        self.softmax = nn.Softmax(dim=1)

    def forward(self, state):
        x = self.relu(self.fc1(state))
        x = self.fc2(x)
        action_probs = self.softmax(x)
        return action_probs


# Policy Network and Optimizer (in main process)
device = "cuda" if torch.cuda.is_available() else "cpu"
policy_net = PolicyNetwork(3, 32, 2).to(device)
optimizer = optim.Adam(policy_net.parameters(), lr=0.01)


def update_policy_network(batch):
    if batch is None:
        return
    state_tensors, actions, rewards = zip(*batch)

    state_tensors = torch.cat(state_tensors).to(device)
    actions = torch.tensor(actions).to(device)
    rewards = torch.tensor(rewards, dtype=torch.float32).to(device)

    action_probs = policy_net(state_tensors)
    action_log_probs = torch.log(action_probs + 1e-8)

    selected_log_probs = action_log_probs[torch.arange(
        action_log_probs.size(0)), actions]
    loss = -torch.sum(selected_log_probs * rewards)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# End of preamble.
# From the preamble, verbatim:
# Import packages

# Define the Policy Network


class PolicyNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(PolicyNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)  # Additional layer
        self.relu = nn.ReLU()
        self.softmax = nn.Softmax(dim=1)

    def forward(self, state):
        x = self.relu(self.fc1(state))
        x = self.fc2(x)
        action_probs = self.softmax(x)
        return action_probs


# Policy Network and Optimizer (in main process)
device = "cuda" if torch.cuda.is_available() else "cpu"
policy_net = PolicyNetwork(3, 32, 2).to(device)
optimizer = optim.Adam(policy_net.parameters(), lr=0.01)


def update_policy_network(batch):
    if batch is None:
        return
    state_tensors, actions, rewards = zip(*batch)

    state_tensors = torch.cat(state_tensors).to(device)
    actions = torch.tensor(actions).to(device)
    rewards = torch.tensor(rewards, dtype=torch.float32).to(device)

    action_probs = policy_net(state_tensors)
    action_log_probs = torch.log(action_probs + 1e-8)

    selected_log_probs = action_log_probs[torch.arange(
        action_log_probs.size(0)), actions]
    loss = -torch.sum(selected_log_probs * rewards)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# End of preamble.
# From the preamble, verbatim:
# Import packages

# Define the Policy Network


class PolicyNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(PolicyNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)  # Additional layer
        self.relu = nn.ReLU()
        self.softmax = nn.Softmax(dim=1)

    def forward(self, state):
        x = self.relu(self.fc1(state))
        x = self.fc2(x)
        action_probs = self.softmax(x)
        return action_probs


# Policy Network and Optimizer (in main process)
device = "cuda" if torch.cuda.is_available() else "cpu"
policy_net = PolicyNetwork(3, 32, 2).to(device)
optimizer = optim.Adam(policy_net.parameters(), lr=0.01)


def update_policy_network(batch):
    if batch is None:
        return
    state_tensors, actions, rewards = zip(*batch)

    state_tensors = torch.cat(state_tensors).to(device)
    actions = torch.tensor(actions).to(device)
    rewards = torch.tensor(rewards, dtype=torch.float32).to(device)

    action_probs = policy_net(state_tensors)
    action_log_probs = torch.log(action_probs + 1e-8)

    selected_log_probs = action_log_probs[torch.arange(
        action_log_probs.size(0)), actions]
    loss = -torch.sum(selected_log_probs * rewards)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
# End of preamble.


# Python class for reactor _blackjack_train_main
class __blackjack_train_main:

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

    @property
    def bank_index(self):
        return self._bank_index  # pylint: disable=no-member

    def reaction_function_0(self):

        self.env = gym.make("Blackjack-v1")
        self.obs = self.env.reset()
        self.policy_net = PolicyNetwork(3, 32, 2).to("cpu")
        return 0

    def reaction_function_1(self, gradients, trajectories):

        self.policy_net.load_state_dict(gradients.value)
        experiences = []

        for _ in range(100):
            state_tensor = torch.from_numpy(
                np.array(self.obs)).float().unsqueeze(0)
            action_probs = self.policy_net(state_tensor).detach().numpy()
            action = np.random.choice(2, p=action_probs.ravel())

            next_state, reward, done, _ = self.env.step(action)
            experiences.append((state_tensor, action, reward))

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
        self.experiences = deque(maxlen=5000)
        return 0

    def reaction_function_1(self, trajectories, dataset):

        # Append Trajectories into ReplayBuffer
        for i in range(16):
            new_experiences = trajectories[i].value
            if new_experiences is not None:
                self.experiences.extend(new_experiences)

        result = list(self.experiences)[:1000]
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
        self.policy_net_state = None
        self.round = None

    @property
    def bank_index(self):
        return self._bank_index  # pylint: disable=no-member

    def reaction_function_0(self, gradients):

        # Initialize the policy
        self.start_time = time.time()
        self.round = 0
        self.policy_net_state = {key: tensor.to(
            "cpu") for key, tensor in policy_net.state_dict().items()}
        gradients.set(self.policy_net_state)
        return 0

    def reaction_function_1(self, dataset, gradients):

        # Update the policy
        batch = dataset.value
        if batch:
            print(len(batch))
            update_policy_network(batch)

        print(
            f"Round {self.round}, Training Time: {time.time()-self.start_time:.2f}")
        self.round += 1

        self.policy_net_state = {key: tensor.to(
            "cpu") for key, tensor in policy_net.state_dict().items()}

        gradients.set(self.policy_net_state)
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
blackjack_train_main_lf = [None] * 1
blackjack_train_rollout_lf = [None] * 16
blackjack_train_replay_lf = [None] * 1
blackjack_train_learner_lf = [None] * 1
blackjack_train_delay_lf = [None] * 1
# Start initializing blackjack_train of class _blackjack_train_main
for blackjack_train_main_i in range(1):
    bank_index = blackjack_train_main_i
    blackjack_train_main_lf[0] = __blackjack_train_main(
        _bank_index=0,
    )
    # Start initializing blackjack_train.rollout of class _rolloutreactor
    for blackjack_train_rollout_i in range(16):
        bank_index = blackjack_train_rollout_i
        blackjack_train_rollout_lf[blackjack_train_rollout_i] = __rolloutreactor(
            _bank_index=blackjack_train_rollout_i,
        )
    # Start initializing blackjack_train.replay of class _replaybufferreactor
    for blackjack_train_replay_i in range(1):
        bank_index = blackjack_train_replay_i
        blackjack_train_replay_lf[0] = __replaybufferreactor(
            _bank_index=0,
        )
    # Start initializing blackjack_train.learner of class _learnerreactor
    for blackjack_train_learner_i in range(1):
        bank_index = blackjack_train_learner_i
        blackjack_train_learner_lf[0] = __learnerreactor(
            _bank_index=0,
        )
    # Start initializing blackjack_train.delay of class __lf_gendelay_0
    for blackjack_train_delay_i in range(1):
        bank_index = blackjack_train_delay_i
        blackjack_train_delay_lf[0] = ___lf_gendelay_0(
            _bank_index=blackjack_train_delay_i,
            _delay=0,
        )


# The main function
def main(argv):
    start(argv)


# As is customary in Python programs, the main() function
# should only be executed if the main module is active.
if __name__ == "__main__":
    main(sys.argv)
