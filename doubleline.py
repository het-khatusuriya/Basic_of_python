import matplotlib.pyplot as plt

# Create data
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

# Create figure and axis objects
fig, ax = plt.subplots()

# Plot the data
ax.plot(x, y1, color='blue', label='Line 1')
ax.plot(x, y2, color='red', label='Line 2')

# Set the x and y axis labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Set the title of the graph
ax.set_title('Simple Line Graph with Colors')

# Add legend to the graph
ax.legend()

# Display the graph
plt.show()
