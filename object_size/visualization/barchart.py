import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Object sizes
object_sizes = [10, 100, 300, 500]

# New data: mean values for Ray and LF
ray_means = [24.109999999999996, 203.69099999999998, 477.521, 869.3960000000002]
lf_means = [7.144, 145.75588235294118, 307.1792079207921, 511.0306930693069]

# New data: 99% Confidence Interval (we will use half the interval range as the error value)
ray_error = [(24.23744280199811 - 23.98255719800188) / 2,
             (205.85548316884608 - 201.52651683115388) / 2,
             (481.4342689835787 - 473.60773101642123) / 2,
             (875.4730801953023 - 863.318919804698) / 2]
lf_error = [(7.4456198291375595 - 6.842380170862441) / 2,
            (147.1512932873415 - 144.36047141854086) / 2,
            (313.1174147791217 - 301.24100106246254) / 2,
            (515.7217718361071 - 506.3396143025067) / 2]

# Bar chart settings
bar_width = 0.35
index = np.arange(len(object_sizes))

# Set the style for the plot and the colors
sns.set_style("whitegrid")
light_blue = '#6699ff'
light_red = '#ff6666'

# Plot Ray mean values with error bars
plt.bar(index, ray_means, bar_width, yerr=ray_error, label='Ray', color=light_blue, capsize=5)

# Plot LF mean values shifted by `bar_width` with error bars
plt.bar(index + bar_width, lf_means, bar_width, yerr=lf_error, label='LF', color=light_red, capsize=5)

# Labeling the axes, giving a title, and adjusting ticks for better visualization
plt.xlabel('Object Size (MB)')
plt.ylabel('Overhead (millisecond)')
plt.title('Mean Overhead of Broadcast and Gather on 16 actors \n for Ray and LF with 99% CI')
plt.xticks(index + bar_width / 2, object_sizes)  # Centering the X-ticks

# Displaying the legend
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
