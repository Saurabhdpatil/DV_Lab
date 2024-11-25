# Program to demonstrate area plots and how to create them with Matplotlib.

# Importing libraries
import numpy as np
import matplotlib.pyplot as plt

# Create data
x = range(1, 6)
y = [1, 4, 6, 8, 4]

# Area plot
plt.fill_between(x, y, color="purple")

# Display plot
plt.show()



histogram 

# Generate random data for the histogram
data = np.random.randn(1000)

# Plotting a basic histogram
plt.hist(data, bins=30, color="skyblue", edgecolor="black")

# Adding labels and titles
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Basic Histogram")

# Display the plot
plt.show()
