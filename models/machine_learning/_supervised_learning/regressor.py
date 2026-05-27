import sys
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

# Build a linear regressor
filename = sys.argv[1]
X = []
Y = []

try:
    with open(filename, 'r') as file:
        for line in file.readlines():
            line = line.strip()
            if not line:
                continue  # skip empty lines
            try:
                xt, yt = [float(i) for i in line.split(',')]
                X.append(xt)
                Y.append(yt)
            except ValueError:
                print(f"Skipping invalid line: {line}")
except FileNotFoundError:
    print(f"File not found: {filename}")
    sys.exit(1)

print("X:", X)
print("Y:", Y)

print(f"Total samples loaded: {len(X)}")
if len(X) == 0:
    print("No valid data found in file. Exiting.")
    sys.exit(1)
# Split data into training and testing sets
training_data = int(0.8 * len(X))
testing_data = len(X) - training_data

X_train = np.array(X[:training_data]).reshape(training_data, 1)
Y_train = np.array(Y[:training_data])

X_test = np.array(X[training_data:]).reshape(testing_data, 1)
Y_test = np.array(Y[training_data:])

linear_regressor = linear_model.LinearRegression()

linear_regressor.fit(X_train, Y_train)

# Plot training data
Y_train_predict = linear_regressor.predict(X_train)
plt.figure()
plt.scatter(X_train, Y_train, color='blue')
plt.plot(X_train, Y_train_predict, color='red')
plt.title('Training Data')
plt.show()

#  Plot testing data
Y_test_predict = linear_regressor.predict(X_test)
plt.figure()
plt.scatter(X_test, Y_test, color='green')
plt.plot(X_test, Y_test_predict, color='orange')
plt.title("Testing Data")
plt.show()

import sklearn.metrics as sm

# Measure performance
print("\nLINEAR:")
print("Mean absolute error =", round(sm.mean_absolute_error(Y_test, Y_test_predict), 2))
print("Mean squared error =", round(sm.mean_squared_error(Y_test, Y_test_predict), 2))
print("Median absolute error =", round(sm.median_absolute_error(Y_test, Y_test_predict), 2))
print("Explained variance score =", round(sm.explained_variance_score(Y_test, Y_test_predict), 2))
print("R2 score =", round(sm.r2_score(Y_test, Y_test_predict), 2))

# Achieving model persistence
import pickle

output_file_model = 'loaded_model.pkl'

with open(output_file_model, 'wb') as file:
    pickle.dump(linear_regressor, file)
    print(f"\nModel saved to {output_file_model}")

with open(output_file_model, 'rb') as file:
    loaded_model = pickle.load(file)
    print("\nModel loaded successfully.")

New_Y_test_predict = loaded_model.predict(X_test)
print("\nNew mean absolute error = ", round(sm.mean_absolute_error(Y_test, New_Y_test_predict), 2))
