import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Data
categories = ['Mean CPU Usage', 'Mean Memory Usage']
rays_means = [16.17, 3.24]
lfs_means = [8.61, 4.44]
rays_intervals = [(10.54, 21.80), (3.05, 3.44)]
lfs_intervals = [(3.98, 13.24), (4.07, 4.80)]

light_blue = '#6699ff'
light_red = '#ff6666'

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Calculate errors for Ray
rays_errors = [(rays_means[i] - rays_intervals[i][0], rays_intervals[i][1] - rays_means[i]) for i in range(2)]

# Calculate errors for LF
lfs_errors = [(lfs_means[i] - lfs_intervals[i][0], lfs_intervals[i][1] - lfs_means[i]) for i in range(2)]

# Bar widths
width = 0.35

# Position of bars
r1 = np.arange(len(rays_means))
r2 = [x + width for x in r1]

# Bars for Ray
plt.bar(r1, rays_means, width=width, color=light_blue, label='Ray', yerr=[[err[0] for err in rays_errors], [err[1] for err in rays_errors]], capsize=7)

# Bars for LF
plt.bar(r2, lfs_means, width=width, color=light_red, label='LF', yerr=[[err[0] for err in lfs_errors], [err[1] for err in lfs_errors]], capsize=7)

# Setting the title and labels
plt.title('Resource Utilization Comparison')
plt.ylabel('% Usage')
plt.xlabel('Resource Type')
plt.xticks([r + width/2 for r in range(len(rays_means))], categories)  # Positioning the labels in the middle of grouped bars
plt.legend()

plt.tight_layout()
plt.show()
