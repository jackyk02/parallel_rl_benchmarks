import matplotlib.pyplot as plt
import numpy as np

# Data
num_of_agents = [4, 10]
ray_time = [169.52, 917.03]
lf_time = [71.64, 179.11]

# Plotting
bar_width = 0.2
index = np.arange(len(num_of_agents))

fig, ax = plt.subplots(figsize=(8, 6))
bar1 = ax.bar(index - bar_width/2, ray_time, bar_width, label='Ray')
bar2 = ax.bar(index + bar_width/2, lf_time, bar_width, label='LF')

# Adding labels and title
ax.set_xlabel('Number of agents')
ax.set_ylabel('Time (seconds)')
# ax.set_title('Comparison of Ray_time and LF_time for Different Numbers of Agents')
ax.set_xticks(index)
ax.set_xticklabels(num_of_agents)
ax.legend()

# Display the plot
plt.show()
