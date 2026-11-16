# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 10:49:58 2026

@author: Admin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

dataset = pd.read_csv(r'C:\My-Drive\Learning\repositories\ai-learning\AI-Naresh-IT\purchased_data.csv')

x = dataset.iloc[:,:-1].values
y = dataset.iloc[:, 3].values

from sklearn.impute import SimpleImputer

imputer = SimpleImputer()