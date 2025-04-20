import numpy as np 
from numpy.random import default_rng


print("zeros 2,3 =",np.zeros((2,3)))        # 2x3 matrix of 0s
print("ones 2,2 =",np.ones((2,2)))         # 2x2 matrix of 1s
print("eye 3=",np.eye(3))              # Identity matrix
print("in range =",np.arange(0, 10, 2))    # [0, 2, 4, 6, 8]
print("evenly spaced =",np.linspace(0, 1, 5))   # 5 numbers evenly spaced from 0 to 1
print("rand 2,3",np.random.rand(2, 3))   # 2x3 matrix of random numbers
print("rand norma dist 2,3",np.random.randn(2, 3))  # 2x3 matrix of random numbers from standard normal distribution
print("rand int 2,3",np.random.randint(0, 10, (2, 3)))  # 2x3 matrix of random integers from 0 to 10






rng = default_rng()

# Random floats (0.0 to 1.0)
print(rng.random(5))          # [0.65, 0.19, 0.87...]

# Random integers
print(rng.integers(1, 100, 5))  # [12 76 54 29 67]

# Random from normal distribution
print(rng.normal(0, 1, 5))     # mean=0, std=1

# Set seed for reproducibility
rng = default_rng(seed=42)
print(rng.random(5))          # [0.25, 0.78, 0.87...]
# Random choice from a list
choices = ['apple', 'banana', 'cherry']
print(rng.choice(choices, 2))  # ['banana', 'apple']
# Random permutation of an array
arr = np.array([1, 2, 3, 4, 5])
print(rng.permutation(arr))    # [3, 1, 5, 2, 4]
# Random sample from a population
population = np.arange(10)
sample_size = 3
sample = rng.choice(population, sample_size, replace=False)
print(sample)                # [7, 2, 5]
# Random seed for reproducibility
rng = default_rng(seed=123)
print(rng.random(5))          # [0.52, 0.85, 0.11...]
# Random floats (0.0 to 1.0)
print(rng.random(5))          # [0.52, 0.85, 0.11...]
# Random integers
print(rng.integers(1, 100, 5))  # [12 76 54 29 67]
# Random from normal distribution
print(rng.normal(0, 1, 5))     # mean=0, std=1      
# Random choice from a list
choices = ['apple', 'banana', 'cherry']
print(rng.choice(choices, 2))  # ['banana', 'apple']
# Random permutation of an array
arr = np.array([1, 2, 3, 4, 5])
print(rng.permutation(arr))    # [3, 1, 5, 2, 4]
# Random sample from a population
population = np.arange(10)
sample_size = 3
sample = rng.choice(population, sample_size, replace=False)
print(sample)                # [7, 2, 5]
# Random seed for reproducibility
rng = default_rng(seed=123)
print(rng.random(5))          # [0.52, 0.85, 0.11...]
# Random floats (0.0 to 1.0)
print(rng.random(5))          # [0.52, 0.85, 0.11...]       






