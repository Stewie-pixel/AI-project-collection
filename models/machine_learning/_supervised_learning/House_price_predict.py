import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.metrics import mean_squared_error, explained_variance_score
from sklearn.utils import shuffle
import matplotlib.pyplot as plt

# Load the Boston Housing dataset from datasets
Columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

housing_data = pd.read_csv('housing.csv', header=None, sep=r"\s+", names=Columns)

print(housing_data.head())

housing_data.describe()
'''
X, y = shuffle(housing_data.data, housing_data.target, random_state=7)

len_training = int(0.8 * len(X))
X_train, y_train = X[:len_training], y[:len_training]
X_test, y_test = X[len_training:], y[len_training:]

# Createa Decision Tree Regressor
dt_regressor  =DecisionTreeRegressor(max_depth=4)
dt_regressor.fit(X_train, y_train)

# Create an Adaboost Regressor
ada_regressor = AdaBoostRegressor(DecisionTreeRegressor(max_depth=4), n_estimators=400, random_state=7)
ada_regressor.fit(X_train, y_train)

# Evaluate Decision Tree Regressor Performance
y_predict_dt = dt_regressor.predict(X_test)
mse = mean_squared_error(y_test, y_predict_dt)
evs = explained_variance_score(y_test, y_predict_dt)
#print("\nDecision Tree Performance")
#print("Mean Squared Error = ", round(mse, 2))
#print("Explained Variance Score = ", round(evs, 2))

# Evaluate Adaboost Regressor Performance
y_predict_ada = ada_regressor.predict(X_test)
mse = mean_squared_error(y_test, y_predict_ada)
evs = explained_variance_score(y_test, y_predict_ada)
#print("\nAdaboost Regressor Performance")
#print("Mean Squared Error = ", round(mse, 2))
#print("Explained Variance Score = ", round(evs, 2))
'''