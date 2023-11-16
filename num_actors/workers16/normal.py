import time
start_time = time.time()
number = 150000
result = 1
for i in range(1, number + 1):
    result *= i
end_time = time.time()
print(f"Time taken: {(end_time - start_time)*1000:.4f} ms")
