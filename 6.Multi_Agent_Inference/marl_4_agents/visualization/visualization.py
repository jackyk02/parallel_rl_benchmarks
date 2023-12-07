import matplotlib.pyplot as plt
#from pingouin import partial_corr


episode = [10000 * i for i in range(1, 11)]
ray_time = [17.79, 34.48, 51.11, 67.97, 84.68, 101.88, 118.74, 135.64, 152.96, 169.52]
lf_time = [7.46, 14.88, 22.32, 29.48, 36.54, 43.63, 50.65, 57.64, 64.64, 71.64]
plt.plot(episode, ray_time, marker='o', label='Ray')
plt.plot(episode, lf_time, marker='s', label='LF')

# Adding labels and title
plt.xlabel('Episode')
plt.ylabel('Time (seconds)')
plt.xticks(episode)
#plt.title('Comparison of training time between Ray and LF')
plt.legend()

# Display the plot
plt.show()