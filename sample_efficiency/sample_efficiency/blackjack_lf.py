import time
import numpy as np
import gym
import copy
import LinguaFrancasample_efficiency as lf
from LinguaFrancasample_efficiency import (
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

# Configuration parameters
NUM_ENVS = 16
NUM_STEPS = 5000
# End of preamble.
# From the preamble, verbatim:

# Configuration parameters
NUM_ENVS = 16
NUM_STEPS = 5000
# End of preamble.
# From the preamble, verbatim:

# Configuration parameters
NUM_ENVS = 16
NUM_STEPS = 5000
# End of preamble.
# From the preamble, verbatim:

# Configuration parameters
NUM_ENVS = 16
NUM_STEPS = 5000
# End of preamble.
# From the preamble, verbatim:

# Configuration parameters
NUM_ENVS = 16
NUM_STEPS = 5000
# End of preamble.
# From the preamble, verbatim:

# Configuration parameters
NUM_ENVS = 16
NUM_STEPS = 5000
# End of preamble.
# From the preamble, verbatim:

# Configuration parameters
NUM_ENVS = 16
NUM_STEPS = 5000
# End of preamble.
# From the preamble, verbatim:

# Configuration parameters
NUM_ENVS = 16
NUM_STEPS = 10000
os.environ['OPENBLAS_NUM_THREADS'] = '1'
# End of preamble.


# Python class for reactor _sample_efficiency_main
class __sample_efficiency_main:

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
        self.env = gym.make("Blackjack-v1")
        # Define state variables

    @property
    def bank_index(self):
        return self._bank_index  # pylint: disable=no-member

    def reaction_function_0(self):
        self.env.reset(seed=123, options={})
        return 0

    def reaction_function_1(self, seed, infos):

        policy = np.random.default_rng(seed.value)
        result = self.env.step(policy.integers(0, 2))

        if result[2] or result[3]:
            self.env.reset(seed=123, options={})

        infos.set(result)
        return 0

# Python class for reactor _serverreactor


class __serverreactor:

    # Constructor
    def __init__(self, **kwargs):
        # Define parameters and their default values
        # Handle parameters that are set in instantiation
        self.__dict__.update(kwargs)
        # Define state variables
        self.step_num = None
        self.start_time = None

    @property
    def bank_index(self):
        return self._bank_index  # pylint: disable=no-member

    def reaction_function_0(self, seed):

        self.step_num = 0
        seed.set(self.step_num)
        return 0

    def reaction_function_1(self, infos, seed):

        if self.step_num == 1:
            self.start_time = time.time()

        if self.step_num == NUM_STEPS:
            end_time = time.time()
            print(
                f"Total time taken: {end_time - self.start_time:.2f} seconds")
            request_stop()

        # Perform a step in each environment using the current step number as seed
        print(f"Step: {self.step_num + 1}")

        for i in range(16):
            temp = infos[i].value
            print(
                f"Env {i + 1}: Observations={temp[0]}, Reward={temp[1]}, Terminated={temp[2]}")

        print("\n")
        seed.set(self.step_num)
        self.step_num += 1
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
sample_efficiency_main_lf = [None] * 1
sample_efficiency_client_lf = [None] * 16
sample_efficiency_server_lf = [None] * 1
sample_efficiency_delay_lf = [None] * 1
# Start initializing sample_efficiency of class _sample_efficiency_main
for sample_efficiency_main_i in range(1):
    bank_index = sample_efficiency_main_i
    sample_efficiency_main_lf[0] = __sample_efficiency_main(
        _bank_index=0,
    )
    # Start initializing sample_efficiency.client of class _envreactor
    for sample_efficiency_client_i in range(16):
        bank_index = sample_efficiency_client_i
        sample_efficiency_client_lf[sample_efficiency_client_i] = __envreactor(
            _bank_index=sample_efficiency_client_i,
        )
    # Start initializing sample_efficiency.server of class _serverreactor
    for sample_efficiency_server_i in range(1):
        bank_index = sample_efficiency_server_i
        sample_efficiency_server_lf[0] = __serverreactor(
            _bank_index=0,
        )
    # Start initializing sample_efficiency.delay of class __lf_gendelay_0
    for sample_efficiency_delay_i in range(1):
        bank_index = sample_efficiency_delay_i
        sample_efficiency_delay_lf[0] = ___lf_gendelay_0(
            _bank_index=sample_efficiency_delay_i,
            _delay=0,
        )


# The main function
def main(argv):
    start(argv)


# As is customary in Python programs, the main() function
# should only be executed if the main module is active.
if __name__ == "__main__":
    main(sys.argv)
