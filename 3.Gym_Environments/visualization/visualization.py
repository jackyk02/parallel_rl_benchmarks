import matplotlib.pyplot as plt
import numpy as np

# Data
frameworks = ["Ray", "LF"]
environments = ["Cartpole", "Blackjack", "Pendulum"]

# Number of games per second for each framework and environment
games_per_second = [
    [3276.539974, 5510.653931, 3223.726628],  # Ray
    [3813.882532, 7466.401195, 3646.086534],  # LF
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
plt.title("Performance Comparison of Ray and LF on OpenAI Environments")
plt.xticks(middle_positions, environments)

# Displaying the legend
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
