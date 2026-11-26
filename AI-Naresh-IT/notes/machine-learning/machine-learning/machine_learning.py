# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 09:55:26 2026

@author: Admin
"""

import matplotlib.pyplot as plt

# Data
languages = ['Python', 'Java', 'C++', 'JavaScript']
usage = [80,65,50,70]
#Bar plot
plt.bar(languages,usage)

# Lables and titles
plt.xlabel('Programming Languages')
plt.ylabel('Usage Percentage')
plt.title('Programming languages popularity')
    
# Show plot
plt.show()
# This is a simple bar plot showing the popularity of different programming languages
