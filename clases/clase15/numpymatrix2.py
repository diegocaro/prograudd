import numpy as np
np.random.seed(0)  # seed for reproducibility

# Two-dimensional array (matrix)
x2 = np.random.randint(10, size=(3, 4))
print('x2[:2, :3]:', x2[:2, :3])  # two rows, three columns

print('x2[:, 0]:', x2[:, 0])  # first column of x2

print('x2[0, :]:', x2[0, :])  # first row of x2

x2_sub = x2[:2, :2]
print('x2[:2, :2]:',x2_sub)

# update the array
x2_sub[0, 0] = 99
print('x2_sub:', x2_sub)
print('x2:',x2)

x2_sub_copy = x2[:2, :2].copy()
print('x2_sub_copy:', x2_sub_copy)

x2_sub_copy[0, 0] = 42
print('x2_sub_copy:', x2_sub_copy)
print('x2', x2)