import numpy as np
m = np.array([[1, -2, 3],
                 [4, 5, -6]])
# matrix transpuesta
print('m.T:', m.T)

# dot product
print('m.dot(m.T):', m.dot(m.T))

# inverse matrix
a = np.array([[1., 2.], [3., 4.]])
ainv = np.linalg.inv(a)
print('ainv:', ainv)
print('a * ainv:', a.dot(ainv))