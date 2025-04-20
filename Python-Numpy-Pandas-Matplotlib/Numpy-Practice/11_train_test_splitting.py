import numpy as np 

data = np.arange(100).reshape(20, 5)  # 20 samples, 5 features
labels = np.random.randint(0, 2, 20)

# Shuffle and split
indices = np.arange(data.shape[0])
np.random.shuffle(indices)

split = int(0.8 * len(data))
train_idx, test_idx = indices[:split], indices[split:]

X_train, X_test = data[train_idx], data[test_idx]
y_train, y_test = labels[train_idx], labels[test_idx]
print("Training data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)
print("Training labels shape:", y_train.shape)
print("Testing labels shape:", y_test.shape)
# Output:
# Training data shape: (16, 5)
# Testing data shape: (4, 5)
# Training labels shape: (16,)
# Testing labels shape: (4,)
# This code snippet demonstrates how to shuffle and split a dataset into training and testing sets.
# The dataset consists of 20 samples with 5 features each.
# The labels are randomly generated binary values (0 or 1).
# The dataset is shuffled and split into 80% training and 20% testing sets.
# The shapes of the training and testing data and labels are printed to confirm the split.
# This is a simple example of how to split a dataset into training and testing sets.
# The code uses NumPy for array manipulation and random number generation.
# The dataset is reshaped into a 2D array with 20 samples and 5 features.
# The labels are generated randomly as binary values (0 or 1).
# The dataset is shuffled using NumPy's random shuffle function.
# The split ratio is set to 80% for training and 20% for testing.    