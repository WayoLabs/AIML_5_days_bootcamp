import numpy as np


#Create Arrays
# 1D array
arr1 = np.array([1,2,3,4])
print(arr1)
# 2D array
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)
# 3D array
arr3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(arr3)
# Array Properties
print("Array 1 shape:", arr1.shape)
print("Array 2 shape:", arr2.shape)
print("Array 3 shape:", arr3.shape)
print("Array 1 size:", arr1.size)
print("Array 2 size:", arr2.size)
print("Array 3 size:", arr3.size)
# Array Data Types
print("Array 1 data type:", arr1.dtype)
print("Array 2 data type:", arr2.dtype)
print("Array 3 data type:", arr3.dtype)
# Array Indexing
print("Element at index 0 of Array 1:", arr1[0])
print("Element at index 1 of Array 2:", arr2[1, 2])
# Array Slicing
print("Elements from index 1 to 3 of Array 1:", arr1[1:4])
print("Elements from index 0 to 1 of Array 2:", arr2[0:2, 1])






baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

np_baseball = np.array(baseball)
print(np_baseball.shape)
print(type(np_baseball))
print('Only second row : ',np_baseball[1,:])
print('Only second column : ',np_baseball[:,1])
print('2nd and 3rd row : ',np_baseball[1:3])


# Array Unique Elements
arr4 = np.array([1, 2, 2, 3, 4])
arr4_unique = np.unique(arr4)
print("Unique elements of Array 4:", arr4_unique)
# Array Boolean Indexing
arr5 = np.array([1, 2, 3, 4, 5])
arr5_bool = arr5 > 2
print("Boolean Indexing of Array 11:", arr5[arr5_bool])

# Array Fancy Indexing
arr6 = np.array([1, 2, 3, 4, 5])
indices = [0, 2, 4]
print("Fancy Indexed Array 6:", arr6[indices])

# Array Conditional Selection
arr7 = np.array([1, 2, 3, 4, 5])
condition = arr7 > 2
arr8 = np.where(condition, arr7, 0)
print("Conditional Selection of Array 8:", arr8)



#Reshape and Flatten
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)  # (2, 3)
arr = arr.reshape(3, 2)
print(arr.shape)  # (3, 2)
arr = arr.flatten()
print(arr.shape)  # (6,)
arr = np.array([[1, 2], [3, 4], [5, 6]])
print(arr.shape)  # (3, 2)
arr = arr.reshape(2, 3)
print(arr.shape)  # (2, 3)
arr = arr.flatten()
print(arr.shape)  # (6,)



# Array Iteration
arr20 = np.array([1, 2, 3, 4, 5])
for i in arr20:
    print("Iterated Element of Array 20:", i)


#save array
# Create an array
arr = np.array([[1, 2, 3], [4, 5, 6]])
# Save it to a file
np.save('my_array.npy', arr)
loaded_arr = np.load('my_array.npy')
print(loaded_arr)

