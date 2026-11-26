# This is a test file for machine learning visualizations

import matplotlib.pyplot as plt

# Sample data
languages = ['Python', 'Java', 'C++', 'JavaScript']
usage = [80, 65, 50, 70]

# Bar plot
plt.bar(languages, usage)

# Labels and title
plt.xlabel('Programming Languages')
plt.ylabel('Usage Percentage')
plt.title('Programming languages popularity')

# Show plot
plt.show()
# This is a simple bar plot showing the popularity of different programming languages