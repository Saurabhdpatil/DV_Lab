# Importing necessary libraries
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Sample text data
text = """
Python is a programming language for data analysis and visualization.
Python is used for machine learning, web development, and more.
Python libraries such as NumPy, Pandas, and Matplotlib are essential for data scientists.
"""

# Create a WordCloud object
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the WordCloud using matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Hide the axes
plt.show()
