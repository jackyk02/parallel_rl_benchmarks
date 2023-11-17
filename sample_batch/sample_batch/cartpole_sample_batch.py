import time
import numpy as np
import gym
import copy
import LinguaFrancasample_batch as lf
from LinguaFrancasample_batch import (
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

NUM_EPISODES = 10000
# End of preamble.
# From the preamble, verbatim:

NUM_EPISODES = 10000
# End of preamble.
# From the preamble, verbatim:

NUM_EPISODES = 10000
# End of preamble.
# From the preamble, verbatim:

NUM_EPISODES = 10000
# End of preamble.
# From the preamble, verbatim:

NUM_EPISODES = 10000
# End of preamble.
# From the preamble, verbatim:

NUM_EPISODES = 10000
# End of preamble.
# From the preamble, verbatim:

NUM_EPISODES = 10000
# End of preamble.
# From the preamble, verbatim:

NUM_EPISODES = 5000
# End of preamble.


# Python class for reactor _sample_batch_main
class __sample_batch_main:

    # Constructor
    def __init__(self, **kwargs):
        # Define parameters and their default values
        # Handle parameters that are set in instantiation
        self.__dict__.update(kwargs)
        # Define state variables

    @property
    def bank_index(self):
        return self._bank_index  # pylint: disable=no-member


# Python class for reactor _envreactor
class __envreactor:

    # Constructor
    def __init__(self, **kwargs):
        # Define parameters and their default values
        # Handle parameters that are set in instantiation
        self.__dict__.update(kwargs)
        self.env = gym.make("CartPole-v1")
        # Define state variables

    @property
    def bank_index(self):
        return self._bank_index  # pylint: disable=no-member

    def reaction_function_0(self):
        self.env.reset(seed=123, options={})
        return 0

    def reaction_function_1(self, seed, infos):
        start_time = time.time()
        policy = np.random.default_rng(seed.value)
        observations, rewards, terminations = [], [], []

        terminated = False
        while not terminated:
            action = policy.integers(0, 2)
            obs, reward, terminated, truncated, _ = self.env.step(action)
            observations.append(obs)
            rewards.append(reward)
            terminations.append(terminated)

        self.env.reset(seed=123, options={})
        end_time = time.time()
        infos.set((observations, rewards, terminations))
        print(f"Time taken: {(end_time - start_time)*1000:.4f} ms")
        return 0

# Python class for reactor _serverreactor


class __serverreactor:

    # Constructor
    def __init__(self, **kwargs):
        # Define parameters and their default values
        # Handle parameters that are set in instantiation
        self.__dict__.update(kwargs)
        # Define state variables
        self.episode_num = None
        self.start_time = None

    @property
    def bank_index(self):
        return self._bank_index  # pylint: disable=no-member

    def reaction_function_0(self, seed):

        self.episode_num = 0
        seed.set(self.episode_num)
        return 0

    def reaction_function_1(self, infos, seed):

        if self.episode_num == 1:
            self.start_time = time.time()

        if self.episode_num == NUM_EPISODES:
            end_time = time.time()
            print(
                f"Total time taken: {end_time - self.start_time:.2f} seconds")
            request_stop()

        # Perform a step in each environment using the current step number as seed
        print(f"Episode: {self.episode_num + 1}")

        for i in range(30):
            observations = infos[i].value[0]
            print(f"Env {i + 1}: Number of Observations = {len(observations)}")

        print("\n")

        seed.set(self.episode_num)
        self.episode_num += 1
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
sample_batch_main_lf = [None] * 1
sample_batch_client_lf = [None] * 30
sample_batch_server_lf = [None] * 1
sample_batch_delay_lf = [None] * 1
# Start initializing sample_batch of class _sample_batch_main
for sample_batch_main_i in range(1):
    bank_index = sample_batch_main_i
    sample_batch_main_lf[0] = __sample_batch_main(
        _bank_index=0,
    )
    # Start initializing sample_batch.client of class _envreactor
    for sample_batch_client_i in range(30):
        bank_index = sample_batch_client_i
        sample_batch_client_lf[sample_batch_client_i] = __envreactor(
            _bank_index=sample_batch_client_i,
        )
    # Start initializing sample_batch.server of class _serverreactor
    for sample_batch_server_i in range(1):
        bank_index = sample_batch_server_i
        sample_batch_server_lf[0] = __serverreactor(
            _bank_index=0,
        )
    # Start initializing sample_batch.delay of class __lf_gendelay_0
    for sample_batch_delay_i in range(1):
        bank_index = sample_batch_delay_i
        sample_batch_delay_lf[0] = ___lf_gendelay_0(
            _bank_index=sample_batch_delay_i,
            _delay=0,
        )


# The main function
def main(argv):
    start(argv)


# As is customary in Python programs, the main() function
# should only be executed if the main module is active.
if __name__ == "__main__":
    main(sys.argv)
