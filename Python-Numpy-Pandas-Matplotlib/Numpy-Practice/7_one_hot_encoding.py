import numpy as np 
# One-hot encoding example
# Sample labels
labels = np.array([0, 2, 1, 2])

# Manual one-hot
n_classes = 3
one_hot = np.zeros((labels.size, n_classes))
one_hot[np.arange(labels.size), labels] = 1

print(one_hot)
