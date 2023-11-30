import logging
import time
import numpy as np
import torch.nn as nn
import torch
import gym
import copy
import LinguaFrancatrafficv4 as lf
from LinguaFrancatrafficv4 import (
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
env = gym.make("ma_gym:TrafficJunction4-v1")
EPISODES = 10000
logging.basicConfig(filename="infer_log.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


class PolicyNetwork(nn.Module):
    def __init__(self, obs_space, action_space):
        super(PolicyNetwork, self).__init__()
        self.fc = nn.Linear(obs_space, 64)
        self.action_head = nn.Linear(64, action_space)

    def forward(self, x):
        x = torch.relu(self.fc(x))
        action_probs = torch.softmax(self.action_head(x), dim=-1)
        return action_probs


def load_policy(agent_idx):
    policy = PolicyNetwork(
        env.observation_space[agent_idx].shape[0], env.action_space[agent_idx].n)
    policy_load_path = f"policy_agent_{agent_idx}.pth"
    policy.load_state_dict(torch.load(policy_load_path))
    policy.eval()
    return policy


# End of preamble.
# From the preamble, verbatim:
env = gym.make("ma_gym:TrafficJunction4-v1")
EPISODES = 10000
logging.basicConfig(filename="infer_log.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


class PolicyNetwork(nn.Module):
    def __init__(self, obs_space, action_space):
        super(PolicyNetwork, self).__init__()
        self.fc = nn.Linear(obs_space, 64)
        self.action_head = nn.Linear(64, action_space)

    def forward(self, x):
        x = torch.relu(self.fc(x))
        action_probs = torch.softmax(self.action_head(x), dim=-1)
        return action_probs


def load_policy(agent_idx):
    policy = PolicyNetwork(
        env.observation_space[agent_idx].shape[0], env.action_space[agent_idx].n)
    policy_load_path = f"policy_agent_{agent_idx}.pth"
    policy.load_state_dict(torch.load(policy_load_path))
    policy.eval()
    return policy


# End of preamble.
# From the preamble, verbatim:
env = gym.make("ma_gym:TrafficJunction4-v1")
EPISODES = 10000
logging.basicConfig(filename="infer_log.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


class PolicyNetwork(nn.Module):
    def __init__(self, obs_space, action_space):
        super(PolicyNetwork, self).__init__()
        self.fc = nn.Linear(obs_space, 64)
        self.action_head = nn.Linear(64, action_space)

    def forward(self, x):
        x = torch.relu(self.fc(x))
        action_probs = torch.softmax(self.action_head(x), dim=-1)
        return action_probs


def load_policy(agent_idx):
    policy = PolicyNetwork(
        env.observation_space[agent_idx].shape[0], env.action_space[agent_idx].n)
    policy_load_path = f"policy_agent_{agent_idx}.pth"
    policy.load_state_dict(torch.load(policy_load_path))
    policy.eval()
    return policy


# End of preamble.
# From the preamble, verbatim:
env = gym.make("ma_gym:TrafficJunction4-v1")
EPISODES = 10000
logging.basicConfig(filename="infer_log.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


class PolicyNetwork(nn.Module):
    def __init__(self, obs_space, action_space):
        super(PolicyNetwork, self).__init__()
        self.fc = nn.Linear(obs_space, 64)
        self.action_head = nn.Linear(64, action_space)

    def forward(self, x):
        x = torch.relu(self.fc(x))
        action_probs = torch.softmax(self.action_head(x), dim=-1)
        return action_probs


def load_policy(agent_idx):
    policy = PolicyNetwork(
        env.observation_space[agent_idx].shape[0], env.action_space[agent_idx].n)
    policy_load_path = f"policy_agent_{agent_idx}.pth"
    policy.load_state_dict(torch.load(policy_load_path))
    policy.eval()
    return policy


# End of preamble.
# From the preamble, verbatim:
env = gym.make("ma_gym:TrafficJunction4-v1")
EPISODES = 10000
logging.basicConfig(filename="infer_log.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


class PolicyNetwork(nn.Module):
    def __init__(self, obs_space, action_space):
        super(PolicyNetwork, self).__init__()
        self.fc = nn.Linear(obs_space, 64)
        self.action_head = nn.Linear(64, action_space)

    def forward(self, x):
        x = torch.relu(self.fc(x))
        action_probs = torch.softmax(self.action_head(x), dim=-1)
        return action_probs


def load_policy(agent_idx):
    policy = PolicyNetwork(
        env.observation_space[agent_idx].shape[0], env.action_space[agent_idx].n)
    policy_load_path = f"policy_agent_{agent_idx}.pth"
    policy.load_state_dict(torch.load(policy_load_path))
    policy.eval()
    return policy


# End of preamble.
# From the preamble, verbatim:
env = gym.make("ma_gym:TrafficJunction4-v1")
EPISODES = 10000
logging.basicConfig(filename="infer_log.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


class PolicyNetwork(nn.Module):
    def __init__(self, obs_space, action_space):
        super(PolicyNetwork, self).__init__()
        self.fc = nn.Linear(obs_space, 64)
        self.action_head = nn.Linear(64, action_space)

    def forward(self, x):
        x = torch.relu(self.fc(x))
        action_probs = torch.softmax(self.action_head(x), dim=-1)
        return action_probs


def load_policy(agent_idx):
    policy = PolicyNetwork(
        env.observation_space[agent_idx].shape[0], env.action_space[agent_idx].n)
    policy_load_path = f"policy_agent_{agent_idx}.pth"
    policy.load_state_dict(torch.load(policy_load_path))
    policy.eval()
    return policy


# End of preamble.
# From the preamble, verbatim:
env = gym.make("ma_gym:TrafficJunction4-v1")
EPISODES = 10000
logging.basicConfig(filename="infer_log.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


class PolicyNetwork(nn.Module):
    def __init__(self, obs_space, action_space):
        super(PolicyNetwork, self).__init__()
        self.fc = nn.Linear(obs_space, 64)
        self.action_head = nn.Linear(64, action_space)

    def forward(self, x):
        x = torch.relu(self.fc(x))
        action_probs = torch.softmax(self.action_head(x), dim=-1)
        return action_probs


def load_policy(agent_idx):
    policy = PolicyNetwork(
        env.observation_space[agent_idx].shape[0], env.action_space[agent_idx].n)
    policy_load_path = f"policy_agent_{agent_idx}.pth"
    policy.load_state_dict(torch.load(policy_load_path))
    policy.eval()
    return policy


# End of preamble.
# From the preamble, verbatim:
env = gym.make("ma_gym:TrafficJunction4-v1")
EPISODES = 100000
logging.basicConfig(filename="infer_log.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


class PolicyNetwork(nn.Module):
    def __init__(self, obs_space, action_space):
        super(PolicyNetwork, self).__init__()
        self.fc = nn.Linear(obs_space, 64)
        self.action_head = nn.Linear(64, action_space)

    def forward(self, x):
        x = torch.relu(self.fc(x))
        action_probs = torch.softmax(self.action_head(x), dim=-1)
        return action_probs


def load_policy(agent_idx):
    policy = PolicyNetwork(
        env.observation_space[agent_idx].shape[0], env.action_space[agent_idx].n)
    policy_load_path = f"policy_agent_{agent_idx}.pth"
    policy.load_state_dict(torch.load(policy_load_path))
    policy.eval()
    return policy
# End of preamble.


# Python class for reactor _trafficv4_main
class __trafficv4_main:

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
        self.agent_idx = None
        self.policy = None

    @property
    def bank_index(self):
        return self._bank_index  # pylint: disable=no-member

    def reaction_function_0(self):

        self.agent_idx = self._bank_index
        self.policy = load_policy(self.agent_idx)
        return 0

    def reaction_function_1(self, global_parameters, updated_parameters):

        val = global_parameters.value

        state = torch.from_numpy(
            np.array(val[self.agent_idx])).float().unsqueeze(0)
        with torch.no_grad():
            probs = self.policy(state)
        action = torch.argmax(probs, dim=-1)

        updated_parameters.set(action.item())
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
        self.actions = None
        self.round_num = None
        self.start_time = None

    @property
    def bank_index(self):
        return self._bank_index  # pylint: disable=no-member

    def reaction_function_0(self, global_parameters):

        self.env = env
        self.round_num = 0
        self.actions = [()] * 4
        self.total_reward = 0
        state_n = self.env.reset()
        self.done_n = [False] * 4

        global_parameters.set(state_n)
        return 0

    def reaction_function_1(self, updated_parameters, global_parameters):

        if all(self.done_n):
            self.env.reset()
            self.total_reward = 0

        for i in range(4):
            self.actions[i] = updated_parameters[i].value

        next_state_n, rewards, done_n, _ = self.env.step(self.actions)
        state_n = next_state_n

        self.total_reward += sum(rewards)

        # Log the time every 10,000 episodes
        if self.round_num % 10000 == 0 and self.round_num != 0:
            logging.info(
                f"Episode: {i}, Elapsed Time: {time.time() - self.start_time:.2f} seconds")

        # first round
        if self.round_num == EPISODES:
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
        print("Reward: " + str(self.total_reward) + " \n")
        global_parameters.set(state_n)
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
trafficv4_main_lf = [None] * 1
trafficv4_client_lf = [None] * 4
trafficv4_server_lf = [None] * 1
trafficv4_delay_lf = [None] * 1
# Start initializing trafficv4 of class _trafficv4_main
for trafficv4_main_i in range(1):
    bank_index = trafficv4_main_i
    trafficv4_main_lf[0] = __trafficv4_main(
        _bank_index=0,
    )
    # Start initializing trafficv4.client of class _clientreactor
    for trafficv4_client_i in range(4):
        bank_index = trafficv4_client_i
        trafficv4_client_lf[trafficv4_client_i] = __clientreactor(
            _bank_index=trafficv4_client_i,
        )
    # Start initializing trafficv4.server of class _serverreactor
    for trafficv4_server_i in range(1):
        bank_index = trafficv4_server_i
        trafficv4_server_lf[0] = __serverreactor(
            _bank_index=0,
        )
    # Start initializing trafficv4.delay of class __lf_gendelay_0
    for trafficv4_delay_i in range(1):
        bank_index = trafficv4_delay_i
        trafficv4_delay_lf[0] = ___lf_gendelay_0(
            _bank_index=trafficv4_delay_i,
            _delay=0,
        )


# The main function
def main(argv):
    start(argv)


# As is customary in Python programs, the main() function
# should only be executed if the main module is active.
if __name__ == "__main__":
    main(sys.argv)
