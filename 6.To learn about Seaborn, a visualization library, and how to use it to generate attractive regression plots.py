# Importing necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the built-in 'tips' dataset
dataset = sns.load_dataset('tips')

# Setting the style for the plots
sns.set_style('whitegrid')

# 1. Creating a simple regression plot
sns.lmplot(x='total_bill', y='tip', data=dataset)

# 2. Customizing the plot with 'hue' to show different categories for 'sex'
sns.lmplot(x='total_bill', y='tip', data=dataset, hue='sex', markers=['o', 'v'])

# 3. Customizing further with marker size and color palette
sns.lmplot(x='total_bill', y='tip', data=dataset, hue='sex', markers=['o', 'v'], 
           scatter_kws={'s': 200}, palette='plasma')

# Display all plots
plt.show()
