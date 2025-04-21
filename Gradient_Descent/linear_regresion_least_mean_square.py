import numpy as np
import matplotlib.pyplot as plt

# Sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 6, 5])

# Compute means
n = len(x)
x_mean = np.mean(x)
y_mean = np.mean(y)

# Compute slope (m)
numerator = np.sum((x - x_mean) * (y - y_mean))
denominator = np.sum((x - x_mean) ** 2)
m = numerator / denominator

# Compute intercept (c)
c = y_mean - m * x_mean

# Predicted values
y_pred = m * x + c

# Plotting
plt.scatter(x, y, color='blue', label='Actual data')
plt.plot(x, y_pred, color='red', label='Best fit line')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Least Squares Linear Regression")
plt.legend()
plt.grid(True)
plt.show()

print(f"Best Fit Line: y = {m:.2f}x + {c:.2f}")
