import numpy as np

A = np.array([[1, -1, -1],[-100, -200, 0], [0, 200, -300]])
b = np.array([0, -3, 3 + 4])
x = np.linalg.solve(A, b)
print(x)