import re
import numpy as np
import scipy.stats as stats

data = """
  CPU: 12.8%
 CPU: 9.1%
 CPU: 13.6%
 CPU: 10.7%
 CPU: 11.8%
 CPU: 17.1%
 CPU: 11.7%
 CPU: 9.3%
 CPU: 11.8%
 CPU: 14.3%
 CPU: 13.8%
 CPU: 11%
 CPU: 11.8%
 CPU: 10.8%
 CPU: 8.9%
 CPU: 8.3%
 CPU: 9.4%
 CPU: 6.9%
 CPU: 15.3%
 CPU: 11.4%
 CPU: 13.3%
 CPU: 11.5%
 CPU: 8.7%
 CPU: 10.6%
 CPU: 13.3%
 CPU: 8.3%
 CPU: 8.5%
 CPU: 15%
 CPU: 12.3%
 CPU: 9.6%
 CPU: 8.6%
 CPU: 8.4%
 CPU: 6.9%
 CPU: 11%
 CPU: 9.8%
 CPU: 7.8%
 CPU: 13.6%
 CPU: 12.2%
 CPU: 10.9%
 CPU: 6.5%
 CPU: 10.9%
 CPU: 9%
 CPU: 10.5%
 CPU: 12.1%
 CPU: 10.9%
 CPU: 13.2%
 CPU: 10.5%
 CPU: 11.4%
 CPU: 12.4%
 CPU: 12.1%
 CPU: 7.3%
 CPU: 12.8%
 CPU: 12.7%
 CPU: 15%
 CPU: 12.3%
 CPU: 12.9%
 CPU: 7.9%
 CPU: 10.1%
 CPU: 10.6%
 CPU: 6.3%
 CPU: 13.9%
 CPU: 14.5%
 CPU: 11.3%
 CPU: 13.9%
 CPU: 12.9%
 CPU: 9.5%
 CPU: 11.9%
 CPU: 13.5%
 CPU: 15%
 CPU: 15%
 CPU: 9.5%
 CPU: 15.7%
 CPU: 12.5%
 CPU: 10.8%
 CPU: 12.4%
 CPU: 6.1%
 CPU: 10.9%
 CPU: 11.8%
 CPU: 8.7%
 CPU: 11.8%
 CPU: 10%
 CPU: 10.8%
 CPU: 12.2%
 CPU: 8.9%
 CPU: 10.3%
 CPU: 9.1%
 CPU: 7.9%
 CPU: 11.6%
 CPU: 10.4%
 CPU: 13.9%
 CPU: 9.8%
 CPU: 10.4%
 CPU: 8.9%
 CPU: 14%
 CPU: 10.2%
 CPU: 11.8%
 CPU: 11.1%
 CPU: 11.1%
 CPU: 12.8%
 CPU: 12.4%
 CPU: 9.9%
 CPU: 11.9%
 CPU: 13.7%
 CPU: 11.5%
 CPU: 13.6%
 CPU: 11.1%
 CPU: 12.3%
 CPU: 13.1%
 CPU: 13.8%
 CPU: 11.5%
 CPU: 13.3%
 CPU: 8.2%
 CPU: 8.5%
 CPU: 8.7%
 CPU: 7.5%
 CPU: 6.7%
 CPU: 9.3%
 CPU: 10.6%
 CPU: 10.2%
 CPU: 10.2%
 CPU: 15.3%
 CPU: 6.6%
 CPU: 11.2%
 CPU: 11.8%
 CPU: 10.1%
 CPU: 10.7%
 CPU: 10.7%
 CPU: 16.4%
"""

# Extract CPU and Memory usage using regex
cpu_usages = np.array([float(value) for value in re.findall(r'CPU: (\d+\.\d+)%', data)])
#memory_usages = np.array([float(value) for value in re.findall(r'Memory: (\d+\.\d+)%', data)])

# Calculate the mean
mean_cpu = np.mean(cpu_usages)
#mean_memory = np.mean(memory_usages)

# Calculate the standard deviation
std_cpu = np.std(cpu_usages)
#std_memory = np.std(memory_usages)

# Calculate the 99% confidence interval
conf_int_cpu = stats.norm.interval(0.99, loc=mean_cpu, scale=std_cpu / np.sqrt(len(cpu_usages)))
#conf_int_memory = stats.norm.interval(0.99, loc=mean_memory, scale=std_memory / np.sqrt(len(memory_usages)))

print(f"Mean CPU Usage: {mean_cpu:.2f}%")
#print(f"Mean Memory Usage: {mean_memory:.2f}%")
print(f"99% Confidence Interval for CPU Usage: ({conf_int_cpu[0]:.2f}%, {conf_int_cpu[1]:.2f}%)")
#print(f"99% Confidence Interval for Memory Usage: ({conf_int_memory[0]:.2f}%, {conf_int_memory[1]:.2f}%)")
