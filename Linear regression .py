#!/usr/bin/env python
# coding: utf-8

# In[22]:


import numpy as np

# Load the data from "lab6-data.txt"
data = np.loadtxt("lab6-data.txt", dtype=float)
x = data[:, 0]
y = data[:, 1]

# Calculate the mean of x and y
x_mean = np.mean(x)
y_mean = np.mean(y)

# Calculate b1 (slope) using the formula
b1 = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)

# Calculate b0 (intercept) using the formula
b0 = y_mean - b1 * x_mean

# Calculate y_pred (predicted values)
y_pred = b0 + b1 * x

# Calculate SS_res (Sum of Squares of Residuals)
ss_res = np.sum((y - y_pred) ** 2)

# Calculate SS_tot (Total Sum of Squares)
ss_tot = np.sum((y - y_mean) ** 2)

# Calculate R^2 (Coefficient of Determination)
r_squared = 1 - (ss_res / ss_tot)

# Display the results
print("b1 (Slope):", b1)
print("b0 (Intercept):", b0)
print("R^2 (Coefficient of Determination):", r_squared)






# In[ ]:





# In[ ]:




