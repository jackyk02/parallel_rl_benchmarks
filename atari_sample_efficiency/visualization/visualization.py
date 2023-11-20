import matplotlib.pyplot as plt
import numpy as np

# Data
frameworks = ["Ray", "LF"]
environments = ["Pacman", "Pong", "SpaceInvader"]

# Number of games per second for each framework and environment
games_per_second = [
    [75, 75.86869658, 74.79804528],  # Ray
    [884.4339623, 877.706261, 860.0917431],  # LF
]

# Bar chart settings
bar_width = 0.35
index = np.arange(len(environments))

# Set the style for the plot and the colors
light_blue = "#6699ff"
light_red = "#ff6666"

# Plot the data for each framework
for i, framework in enumerate(frameworks):
    plt.bar(index + i * bar_width,
            games_per_second[i], bar_width, label=framework, alpha=0.7)

middle_positions = index + \
    (bar_width * (len(frameworks) - 1) / 2)  # Adjusted position

# Labeling the axes, giving a title, and adjusting ticks for better visualization
plt.xlabel("Environment")
plt.ylabel("Observations per Second")
plt.title("Throughput of Ray and LF on Atari Environments")
plt.xticks(middle_positions, environments)

# Displaying the legend
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
