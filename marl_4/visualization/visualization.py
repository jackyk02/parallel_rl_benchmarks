import matplotlib.pyplot as plt
import numpy as np

# Data
frameworks = ["Ray", "LF"]
environment = "TrafficJunction4"

# Time taken for each framework for 100,000 episodes
time_taken = [167.93, 74.46]  # in seconds

# Calculating games per second for each framework
games_per_second = [100000 / time for time in time_taken]

# Bar chart settings
bar_width = 0.1
index = np.array([0])

# Set the colors
light_blue = "#6699ff"
light_red = "#ff6666"


# Plot the data for each framework
plt.figure(figsize=(8, 6))  # Adjusting figure size for clarity
for i, framework in enumerate(frameworks):
    plt.bar(index + i * bar_width,
            time_taken[i], bar_width, label=framework, alpha=0.7, color=[light_blue, light_red][i])

# Adjusting the x-ticks position
middle_positions = index + (bar_width * (len(frameworks) - 1) / 2)

# Labeling the axes, giving a title, and adjusting ticks for better visualization
plt.xlabel("Framework")
plt.ylabel("Time Taken (Seconds)")
plt.title("Time Taken for Inference Task on TrafficJunction4 Environment")
plt.xticks(middle_positions, [environment])

# Displaying the legend
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
# Show the plot
plt.tight_layout()
plt.show()
