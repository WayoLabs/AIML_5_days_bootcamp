import numpy as np 

#array Math operation

# Array Linear Algebra
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr3 = np.dot(arr1, arr2)
print("Dot product of Array 1 and Array 2:", arr3)
# Array Broadcasting
arr4 = np.array([[1], [2]])
arr5 = np.array([[3, 4], [5, 6]])
arr6 = arr4 + arr5
print("Broadcasted Array 6:", arr6)
# Array Broadcasting with Scalars
arr7 = np.array([[1, 2], [3, 4]])
arr8 = arr7 + 5
print("Broadcasted Array 8 with Scalar:", arr8)




a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)       # [5 7 9]
print(a * b)       # [4 10 18]
print(a ** 2)      # [1 4 9]
print(np.dot(a, b))  # 32 (dot product)
print(np.cross(a, b))  # [-3 6 -3] (cross product)
print(np.linalg.norm(a))  # 3.7416573867739413 (Euclidean norm)
print(np.linalg.inv(np.array([[1, 2], [3, 4]])))  # Inverse of a matrix
print(np.linalg.det(np.array([[1, 2], [3, 4]])))  # Determinant of a matrix
print(np.linalg.eig(np.array([[1, 2], [3, 4]])))  # Eigenvalues and eigenvectors
print(np.linalg.svd(np.array([[1, 2], [3, 4]])))  # Singular Value Decomposition
print(np.linalg.qr(np.array([[1, 2], [3, 4]])))  # QR Decomposition
print(np.linalg.cholesky(np.array([[4, 2], [2, 3]])))  # Cholesky Decomposition
print(np.linalg.pinv(np.array([[1, 2], [3, 4]])))  # Pseudo-inverse of a matrix
print(np.linalg.solve(np.array([[1, 2], [3, 4]]), np.array([5, 6])))  # Solve linear equations
print(np.linalg.lstsq(np.array([[1, 2], [3, 4]]), np.array([5, 6]), rcond=None))  # Least squares solution
print(np.linalg.matrix_rank(np.array([[1, 2], [3, 4]])))  # Rank of a matrix
print(np.linalg.norm(np.array([[1, 2], [3, 4]]), ord=1))  # L1 norm of a matrix
print(np.linalg.norm(np.array([[1, 2], [3, 4]]), ord=np.inf))  # L∞ norm of a matrix
print(np.linalg.norm(np.array([[1, 2], [3, 4]]), ord='fro'))  # Frobenius norm of a matrix
print(np.linalg.matrix_power(np.array([[1, 2], [3, 4]]), 2))  # Matrix power
print(np.linalg.matrix_rank(np.array([[1, 2], [3, 4]])))  # Rank of a matrix
print(np.linalg.svd(np.array([[1, 2], [3, 4]])))  # Singular Value Decomposition
print(np.linalg.qr(np.array([[1, 2], [3, 4]])))  # QR Decomposition
print(np.linalg.cholesky(np.array([[4, 2], [2, 3]])))  # Cholesky Decomposition
print(np.linalg.pinv(np.array([[1, 2], [3, 4]])))  # Pseudo-inverse of a matrix
print(np.linalg.solve(np.array([[1, 2], [3, 4]]), np.array([5, 6])))  # Solve linear equations
print(np.linalg.lstsq(np.array([[1, 2], [3, 4]]), np.array([5, 6]), rcond=None))  # Least squares solution
print(np.linalg.matrix_rank(np.array([[1, 2], [3, 4]])))  # Rank of a matrix
print(np.linalg.norm(np.array([[1, 2], [3, 4]]), ord=1))  # L1 norm of a matrix
print(np.linalg.norm(np.array([[1, 2], [3, 4]]), ord=np.inf))  # L∞ norm of a matrix
print(np.linalg.norm(np.array([[1, 2], [3, 4]]), ord='fro'))  # Frobenius norm of a matrix



#Matrix Multiplication
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(np.dot(A, B))
print(A @ B)  # Same as above



