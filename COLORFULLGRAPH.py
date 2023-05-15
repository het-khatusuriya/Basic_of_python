import matplotlib.pyplot as plt
import numpy as np

# Create x values
x = np.linspace(0, 10, 1000)

# Create y values
y1 = np.sqrt(x)
y2 = x ** 2 / 10
y3 = np.sin(x) + 2

# Create figure and axis objects
fig, ax = plt.subplots()

# Set axis labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Colorful Line Graph')

# Plot lines with different colors
ax.plot(x, y1, color='red', label='y1')
ax.plot(x, y2, color='blue', label='y2')
ax.plot(x, y3, color='green', label='y3')

# Add legend
ax.legend()

# Show the plot
plt.show()
