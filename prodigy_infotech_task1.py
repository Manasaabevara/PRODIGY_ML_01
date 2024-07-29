# -*- coding: utf-8 -*-
"""Prodigy Infotech Task1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xVAzzDOkv_LW5jHvsvUutMKQmz70P1oQ
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the datasets
train_file_path = '/content/train.csv'
test_file_path = '/content/test.csv'

train_df = pd.read_csv(train_file_path)
test_df = pd.read_csv(test_file_path)

# Select features for the model
X = train_df[['GrLivArea', 'BedroomAbvGr', 'FullBath']]
y = train_df['SalePrice']

# Split the data into training and testing sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the validation set
y_pred = model.predict(X_val)

# Evaluate the model
mse = mean_squared_error(y_val, y_pred)
r2 = r2_score(y_val, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

# Visualize the actual vs predicted prices
plt.figure(figsize=(10, 5))
plt.scatter(y_val, y_pred, color='blue')
plt.plot([y_val.min(), y_val.max()], [y_val.min(), y_val.max()], 'k--', lw=2)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs Predicted Prices')
plt.show()

# Make predictions on the test dataset
X_test = test_df[['GrLivArea', 'BedroomAbvGr', 'FullBath']]
test_df['PredictedPrice'] = model.predict(X_test)