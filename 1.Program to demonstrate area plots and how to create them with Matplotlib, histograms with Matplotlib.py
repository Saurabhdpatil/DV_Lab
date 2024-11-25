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
