import sys
from concurrent.futures import ThreadPoolExecutor
import time

# Define the constant
FIB_NUMBER = 36

print(f"nogil={getattr(sys.flags, 'nogil', False)}")


def fib(n):
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)


def timed_fib(n):
    start_time = time.time()
    result = fib(n)
    end_time = time.time()
    print(f"Fib({n}) took {(end_time - start_time)*1000:.4f} ms")
    return result


start_time = time.time()

threads = 8
if len(sys.argv) > 1:
    threads = int(sys.argv[1])

with ThreadPoolExecutor(max_workers=threads) as executor:
    futures = [executor.submit(timed_fib, FIB_NUMBER) for _ in range(threads)]

# Wait for all threads to complete and gather results
results = [future.result() for future in futures]

total_end_time = time.time()
print(
    f"Total time taken for all threads: {(total_end_time - start_time)*1000:.4f} ms")
