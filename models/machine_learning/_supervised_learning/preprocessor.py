# This python code is for preprocessing data in preparation for predicting house prices
import numpy as np
from sklearn import preprocessing

data = np.array([[1,2,3,4], 
                 [0.5, 1.5,2.5,3.5], 
                 [1,2.2,3.1,4.5]])
print(data)

# Mean removal
data_standardized = preprocessing.scale(data)
print("\nMean =", data_standardized.mean(axis=0))
print("\nStandard Deviation =", data_standardized.std(axis=0))

# Scaling
data_scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
data_scaled = data_scaler.fit_transform(data)
print("\nScaled Data: ", data_scaled)

# Normalization
data_normalized = preprocessing.normalize(data, norm='l1')
print("\nNormalized Data (L1 norm): ", data_normalized)

# Binarization
data_binarized = preprocessing.Binarizer(threshold=2).transform(data)
print("\nBinarized Data: ", data_binarized)

# One Hot Encoding
encoder = preprocessing.OneHotEncoder()
encoder.fit([[0, 1, 3, 14], 
             [1, 3, 5, 5], 
             [2, 4, 6, 9], 
             [2, 3, 4, 5]])
encoded_vector = encoder.transform([[0, 1, 6, 9]]).toarray()
print("\nOne Hot Encoded Vector: ", encoded_vector)
