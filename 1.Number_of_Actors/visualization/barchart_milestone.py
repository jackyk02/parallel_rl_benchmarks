import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Data
actors = [2, 4, 8, 16]

# Convert means to milliseconds
ray_means = [x * 1000 for x in [0.011724000000000004, 0.01302727272727273, 0.016485, 0.024272000000000002]]
lf_means = [x * 1000 for x in [0.004871, 0.0052190000000000005, 0.005234000000000001, 0.007098]]

# Compute errors for 99% CI
ray_error = [(upper - lower) / 2 * 1000 for upper, lower in zip(
    [0.012138181136773615, 0.013161462281033792, 0.016637203160977797, 0.024438027909053653],
    [0.011309818863226392, 0.012893083173511666, 0.016332796839022203, 0.02410597209094635])]

lf_error = [(upper - lower) / 2 * 1000 for upper, lower in zip(
    [0.0050533947009340835, 0.005475186101014534, 0.0054760770025205855, 0.007348751047223119],
    [0.004688605299065917, 0.004962813898985467, 0.004991922997479416, 0.006847248952776881])]

# Bar chart settings
bar_width = 0.35
index = np.arange(len(actors))

# Set the style for the plot and the colors
sns.set_style("whitegrid")
light_blue = '#6699ff'
light_red = '#ff6666'

# Plot Ray mean values with error bars
plt.bar(index, ray_means, bar_width, yerr=ray_error, label='Ray', color=light_blue, capsize=5)

# Plot LF mean values shifted by `bar_width` with error bars
plt.bar(index + bar_width, lf_means, bar_width, yerr=lf_error, label='LF', color=light_red, capsize=5)

# Labeling the axes, giving a title, and adjusting ticks for better visualization
plt.xlabel('Number of Actors')
plt.ylabel('Overhead (milliseconds)')
plt.title('Mean Overhead of Parameter Server \n with Different Number of Actors')
plt.xticks(index + bar_width / 2, actors)  # Centering the X-ticks

# Displaying the legend
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
