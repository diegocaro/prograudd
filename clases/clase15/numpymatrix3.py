import numpy as np
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
c = np.concatenate([x, y])
print('c:', c)

grid = np.array([[1, 2, 3],
                 [4, 5, 6]])
                 
# concatenate along the first axis
print('axis=0:',np.concatenate([grid, grid]))

# concatenate along the second axis (zero-indexed)
print('axis=1:',np.concatenate([grid, grid], axis=1))

