import os
import sys
sys.path.append(os.path.dirname(__file__))
# List imported names, but do not use pylint's --extension-pkg-allow-list option
# so that these names will be assumed present without having to compile and install.
# pylint: disable=no-name-in-module, import-error
from LinguaFrancaworkers16 import (
    Tag, action_capsule_t, port_capsule, request_stop, schedule_copy, start
)
# pylint: disable=c-extension-no-member
import LinguaFrancaworkers16 as lf
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
import copy

# From the preamble, verbatim:
import time
import numpy as np
# End of preamble.
# From the preamble, verbatim:
import time
import numpy as np
# End of preamble.
# From the preamble, verbatim:
import time
import numpy as np
# End of preamble.
# From the preamble, verbatim:
import time
import numpy as np
# End of preamble.
# From the preamble, verbatim:
import time
import numpy as np
# End of preamble.
# From the preamble, verbatim:
import time
import numpy as np
# End of preamble.
# From the preamble, verbatim:
import time
import numpy as np
# End of preamble.
# From the preamble, verbatim:
import time
import numpy as np
# End of preamble.


# Python class for reactor _workers16_main
class __workers16_main:

    # Constructor
    def __init__(self, **kwargs):
        # Define parameters and their default values
        # Handle parameters that are set in instantiation
        self.__dict__.update(kwargs)
        # Define state variables
    
    @property
    def bank_index(self):
        return self._bank_index # pylint: disable=no-member
    
    



# Python class for reactor _clientreactor
class __clientreactor:

    # Constructor
    def __init__(self, **kwargs):
        # Define parameters and their default values
        # Handle parameters that are set in instantiation
        self.__dict__.update(kwargs)
        # Define state variables
    
    @property
    def bank_index(self):
        return self._bank_index # pylint: disable=no-member
    
    

    def reaction_function_0(self):
    
        
        return 0
    def reaction_function_1(self, global_parameters, updated_parameters):
    
        time.sleep(0.5)
        new_parameter = global_parameters.value.copy()
        updated_parameters.set(new_parameter)
        return 0

# Python class for reactor _serverreactor
class __serverreactor:

    # Constructor
    def __init__(self, **kwargs):
        # Define parameters and their default values
        # Handle parameters that are set in instantiation
        self.__dict__.update(kwargs)
        # Define state variables
        self.round_num = None
        self.benchmark_start_time = None
        self.total_start_time = None
    
    @property
    def bank_index(self):
        return self._bank_index # pylint: disable=no-member
    
    

    def reaction_function_0(self, global_parameters):
    
        self.round_num = 0
        self.results = [0] * 16
        self.benchmark_start_time = None
        self.total_start_time = None
        val = np.ones(33107200)
        global_parameters.set(val)
        return 0
    def reaction_function_1(self, updated_parameters, global_parameters):
    
        # Retrieve value from each client
        for i in range(16):
          self.results[i] = updated_parameters[i].value
        
        # Check and set the benchmark start time for the first round
        if self.round_num == 0:
            self.benchmark_start_time = time.time()
            self.total_start_time = time.time()
        
        if self.round_num == 1000:
            request_stop()
        
        # Calculate the overhead time difference for the current round and reset the start time for the next round
        current_time = time.time()
        overhead_time = current_time - self.benchmark_start_time - 0.5
        training_time = current_time - self.total_start_time
        self.benchmark_start_time = current_time
        
        # Print the overhead time and round number
        print(f"Round: {self.round_num}")
        print(f"Total training time: {training_time:.4f} seconds")
        print(f"Overhead: {overhead_time:.4f} seconds \n")
        
        self.round_num += 1
        
        # Update the global parameters with the results from the first client for the next round
        global_parameters.set(self.results[0].copy())
        return 0

# Python class for reactor __lf_gendelay_0
class ___lf_gendelay_0:

    # Constructor
    def __init__(self, **kwargs):
        # Define parameters and their default values
        self._delay:interval_t = 0
        # Handle parameters that are set in instantiation
        self.__dict__.update(kwargs)
        # Define state variables
    
    @property
    def delay(self):
        return self._delay # pylint: disable=no-member
    
    
    @property
    def bank_index(self):
        return self._bank_index # pylint: disable=no-member
    
    

    
    



# Instantiate classes
workers16_main_lf = [None] * 1
workers16_client_lf = [None] * 16
workers16_server_lf = [None] * 1
workers16_delay_lf = [None] * 1
# Start initializing workers16 of class _workers16_main
for workers16_main_i in range(1):
    bank_index = workers16_main_i
    workers16_main_lf[0] = __workers16_main(
        _bank_index = 0,
    )
    # Start initializing workers16.client of class _clientreactor
    for workers16_client_i in range(16):
        bank_index = workers16_client_i
        workers16_client_lf[workers16_client_i] = __clientreactor(
            _bank_index = workers16_client_i,
        )
    # Start initializing workers16.server of class _serverreactor
    for workers16_server_i in range(1):
        bank_index = workers16_server_i
        workers16_server_lf[0] = __serverreactor(
            _bank_index = 0,
        )
    # Start initializing workers16.delay of class __lf_gendelay_0
    for workers16_delay_i in range(1):
        bank_index = workers16_delay_i
        workers16_delay_lf[0] = ___lf_gendelay_0(
            _bank_index = workers16_delay_i,
            _delay=0,
        )


# The main function
def main(argv):
    start(argv)

# As is customary in Python programs, the main() function
# should only be executed if the main module is active.
if __name__=="__main__":
    main(sys.argv)
