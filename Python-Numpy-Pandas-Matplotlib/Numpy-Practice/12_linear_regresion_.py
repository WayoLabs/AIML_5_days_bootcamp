import numpy as np # y = mx + c
x = np.array([1, 2, 3, 4])
y = np.array([3, 5, 7, 9])

# Fit line: m = slope, c = intercept
m, c = np.polyfit(x, y, 1)
print(f"Slope: {m}, Intercept: {c}")

# Predict
y_pred = m * x + c
print(f"Predicted y: {y_pred}")     
# Calculate R-squared
ss = np.sum((y - y_pred) ** 2)
ss_total = np.sum((y - np.mean(y)) ** 2)
r_squared = 1 - (ss / ss_total)
print(f"R-squared: {r_squared}")


# Display results
#import matplotlib.pyplot as plt
#plt.scatter(x, y, label='Data Points')
#plt.plot(x, y_pred, color='red', label='Fitted Line')
#plt.xlabel('x')
#plt.ylabel('y')
#plt.title('Linear Regression')
#plt.legend()
#plt.show()
