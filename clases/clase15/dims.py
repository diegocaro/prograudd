import numpy as np
np.random.seed(0)  # seed for reproducibility

# One-dimensional array (vector)
x1 = np.random.randint(10, size=6)  

# Two-dimensional array (matrix)
x2 = np.random.randint(10, size=(3, 4))

print(x1)
print(x2)

print("x2 ndim: ", x2.ndim)
print("x2 shape:", x2.shape)
print("x2 size: ", x2.size)
print("dtype:", x2.dtype)

print('x1[0]:', x1[0])
print('x1[4]:', x1[4])
print('x1[-1]:', x1[-1])

print('x2[0, 0]:',x2[0, 0])
print('x2[2, -1]:',x2[2, -1])

x2[0, 0] = 99
print('x2[0, 0]:',x2[0, 0])