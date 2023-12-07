import ray
import time
import numpy as np

# Initialize Ray with no logging.
ray.init(configure_logging=False, log_to_driver=False)

# Configuration parameters
num_clients = 4
num_rounds = 1000

@ray.remote
class Client:
    def __init__(self):
        pass
    
    def task(self, global_parameters):
        """Simulate a task by sleeping for a second and returning a copy of the received parameters."""
        time.sleep(0.5)  # Sleep for 0.5 second
        updated_parameters = global_parameters.copy()
        return updated_parameters

# Start timing for benchmarking
benchmark_start_time = None
total_start_time = None

# Prepare a large data structure for testing. Each int in Python 3.8+ is 28 bytes, 
# so we need approximately 3.57 million of them to get to 100MB.
# Python also has overhead for the list object itself.
global_parameters = np.ones(1310720)

# Initialize a list of remote client objects
clients = [Client.remote() for _ in range(num_clients)]

for round_num in range(num_rounds):
    # Train each client remotely using Ray
    results = ray.get([client.task.remote(global_parameters) for client in clients])

    # Check and set the benchmark start time for the first round
    if round_num == 0:
        benchmark_start_time = time.time()
        total_start_time = time.time()

    # Calculate the overhead time difference for the current round and reset the start time for the next round
    current_time = time.time()
    overhead_time = current_time - benchmark_start_time - 0.5
    training_time = current_time - total_start_time
    benchmark_start_time = current_time

    # Print the overhead time and round number
    print(f"Round: {round_num}")
    print(f"Total training time: {training_time:.4f} seconds")
    print(f"Overhead: {overhead_time:.4f} seconds \n")

    # Update the global parameters with the results from the first client for the next round
    global_parameters = results[0].copy()

# Shutdown Ray after all rounds are complete
ray.shutdown()
