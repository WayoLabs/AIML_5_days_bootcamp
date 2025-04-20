import numpy as np
import time
import sys

SIZE = 1000000
l1 = range(SIZE)
l2 = range(SIZE)

# numpy array
a1=np.arange(SIZE)
a2=np.arange(SIZE)

# python list
start = time.time()
result = [(x+y) for x,y in zip(l1,l2)]
print("python list took: ",(time.time()-start)*1000)


# numpy array
start= time.time()
result = a1 + a2
print("numpy took: ", (time.time()-start)*1000)






SIZE = 200  # Keep it reasonable for nested loop performance

# Python native matrix multiplication
def python_matrix_mult(A, B):
    result = [[0] * SIZE for _ in range(SIZE)]
    for i in range(SIZE):
        for j in range(SIZE):
            for k in range(SIZE):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Create matrices
A = [[i for i in range(SIZE)] for _ in range(SIZE)]
B = [[i for i in range(SIZE)] for _ in range(SIZE)]

# NumPy matrices
A_np = np.array(A)
B_np = np.array(B)

# ⏱ Python
start = time.time()
python_result = python_matrix_mult(A, B)
print("Python nested loop took:", round((time.time() - start)*1000, 2), "ms")

# ⏱ NumPy
start = time.time()
numpy_result = A_np @ B_np  # or use np.dot(A_np, B_np)
print("NumPy matrix mult took:", round((time.time() - start)*1000, 2), "ms")