import numpy as np 


#statistics
arr = np.array([[1,2,3],[4,5,6]])
print(np.min(arr))          # 1
print(np.max(arr))          # 6
print(np.mean(arr))         # 3.5
print(np.sum(arr, axis=0))  # [5 7 9]

# mean
print(np.mean(arr))  # Mean of Array 1
# median
print(np.median(arr))  # Median of Array 1
# standard deviation
print(np.std(arr))  # Standard Deviation of Array 1
# variance
print(np.var(arr))  # Variance of Array 1

# histogram
hist, bins = np.histogram(arr, bins=5)
print("Histogram of Array 1:", hist)


# Array Sorting
arr9 = np.array([3, 1, 2])
arr9.sort()
print("Sorted Array 9:", arr9)


