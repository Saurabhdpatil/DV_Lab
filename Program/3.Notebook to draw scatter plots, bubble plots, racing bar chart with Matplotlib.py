import matplotlib.pyplot as plt

# Define the data
hours_studied = [1, 2, 3, 4, 5, 6, 7, 8]
test_scores = [50, 55, 60, 65, 70, 75, 80, 85]

# Create a scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(hours_studied, test_scores, color='blue', marker='o')

# Add title and labels
plt.title('Scatter Plot of Hours Studied vs Test Score')
plt.xlabel('Hours Studied')
plt.ylabel('Test Score')

# Show grid
plt.grid(True)

# Display the plot
plt.show()





# Define the data
hours_studied = [1, 2, 3, 4, 5, 6, 7, 8]
test_scores = [50, 55, 60, 65, 70, 75, 80, 85]

# Size of the bubble
bubble_sizes = [100, 200, 300, 400, 500, 600, 700, 800]

# Create a bubble chart
plt.figure(figsize=(10, 8))
plt.scatter(hours_studied, test_scores, s=bubble_sizes, alpha=0.5, c='blue', edgecolors='w')

# Add title and labels
plt.title('Bubble Chart of Hours Studied vs Test Score')
plt.xlabel('Hours Studied')
plt.ylabel('Test Score')

# Display the plot
plt.show()
