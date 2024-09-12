# imports
import pandas as pd
import openpyxl
import numpy as np
from openpyxl import load_workbook
from sklearn.ensemble import RandomForestRegressor

# import check
print("Check 1")

# suicide dataset (replace with path)
data = pd.read_csv('path_here')

# load prediction data. (replace with path)
testing_data = pd.read_csv('path_here')
workbook1 = load_workbook("path_here")
sheet1 = workbook1.active

# data check
print("Check 2")

X = data.drop('suicides/100k pop', axis=1)
Y = data['suicides/100k pop']

# checking variables
print("Check 3")
print(testing_data.columns)
print(data.columns)

# Input Desired Values Into Prediction File.
# Age(y), Sex (0 = Male and 1 = Female), HDI (0 to 1), GDP per capita ($USD)
# 5-14 years = 0, 15-24 years = 1, 25-34 years = 2, 35-54 years = 3, 55-74 years = 4, 75+ = 5
# G.I. Generation = 0, Silent = 1, Boomers = 2, Generation X = 3, Millenials = 4, Generation Z = 5
# testing dataset is 500 randomly generated points

# input
X_test = testing_data.drop('suicides/100k pop', axis=1)

# random forest (and check)
random_forest = RandomForestRegressor()
random_forest.fit(X, Y)
print("Check 3")

# predictions
rf_pred = random_forest.predict(X_test)

print(rf_pred)

i = 0
error = 0

# replace with amount of prediction datapoints
datapoints = 491
std = 0
maxpred = 0

# calculate error
while (i < datapoints):
    pred = rf_pred[i]
    maxpred = max(maxpred, rf_pred[i])
    exp = sheet1["E" + str(i + 2)].value
    error += (1 / datapoints) * pow((exp - pred), 2)
    i = i + 1

#normalize error and square root
error = pow(error, 0.5) / maxpred
print("Error:", error)
