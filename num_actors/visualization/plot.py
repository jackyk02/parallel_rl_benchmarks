# Ray Data
ray_actors = [2, 4, 8, 16]
ray_means = [0.011724000000000004, 0.01302727272727273, 0.016485, 0.024272000000000002]
ray_ci_lower = [0.011309818863226392, 0.012893083173511666, 0.016332796839022203, 0.02410597209094635]
ray_ci_upper = [0.012138181136773615, 0.013161462281033792, 0.016637203160977797, 0.024438027909053653]

# LF Data
lf_actors = [2, 4, 8, 16]
lf_means = [0.004871, 0.0052190000000000005, 0.005234000000000001, 0.007098]
lf_ci_lower = [0.004688605299065917, 0.004962813898985467, 0.004991922997479416, 0.006847248952776881]
lf_ci_upper = [0.0050533947009340835, 0.005475186101014534, 0.0054760770025205855, 0.007348751047223119]

# Convert means to milliseconds
ray_means = [x * 1000 for x in ray_means]
lf_means = [x * 1000 for x in lf_means]

# Compute errors
ray_error = [(upper - lower) / 2 for upper, lower in zip(ray_ci_upper, ray_ci_lower)]
lf_error = [(upper - lower) / 2 for upper, lower in zip(lf_ci_upper, lf_ci_lower)]

import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for the plot
sns.set_style("whitegrid")

# Plot Ray mean values with error bars
plt.errorbar(ray_actors, ray_means, yerr=ray_error, fmt='-D', label='Ray', color='blue', elinewidth=1.5, capsize=5)

# Plot LF mean values with error bars
plt.errorbar(lf_actors, lf_means, yerr=lf_error, fmt='-o', label='LF', color='red', elinewidth=1.5, capsize=5)

# Labeling the axes and giving a title
plt.xlabel('Number of Actors')
plt.ylabel('Overhead (milliseconds)')
plt.title('Mean Overhead of Broadcast and Gather 10MB Object \n with Different Number of Actors')

# Set Y-axis limits for better visualization of error bars
plt.ylim(0, max(ray_means + lf_means) + 1)  # added +1 for a slight margin above the max value

# Displaying the legend
plt.legend()

# Show the plot
plt.show()
