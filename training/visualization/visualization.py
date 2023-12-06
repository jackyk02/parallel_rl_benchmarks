import matplotlib.pyplot as plt
import numpy as np

# Data
num_of_agents = [500, 1000, 2000]
ray_time = [136.95, 148.66, 191.55]
lf_time = [94.22, 95.09, 95.97]

# Plotting
bar_width = 0.2
index = np.arange(len(num_of_agents))

fig, ax = plt.subplots(figsize=(8, 6))
bar1 = ax.bar(index - bar_width/2, ray_time, bar_width, label='Ray')
bar2 = ax.bar(index + bar_width/2, lf_time, bar_width, label='LF')

# Adding labels and title
ax.set_xlabel('Mini Batch Size')
ax.set_ylabel('Training Time (seconds)')
# ax.set_title('Comparison of Ray_time and LF_time for Different Numbers of Agents')
ax.set_xticks(index)
ax.set_xticklabels(num_of_agents)
ax.legend()

# Display the plot
plt.show()
