import matplotlib.pyplot as plt

# Sample data for x and y coordinates
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a new figure and specify the figure size (optional)
plt.figure(figsize=(8, 6))

# Plot the data
plt.plot(x, y, marker='o', linestyle='-', color='blue')

# Set labels for x and y axes
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Set title for the plot
plt.title('Line Plot Example')

# Show the plot
plt.show()
