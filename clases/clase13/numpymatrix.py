import numpy as np

a = np.array([[5, 0, 3, 3, 7, 9],[1, 1, 1, 1 ,1, 1]])
b = np.array([3, 5, 2, 4, 7, 6])

c = 2 + a # scalar + matrix
print('c:', c)

c = b + a # vector + matrix
print('c:', c)

c = a + a # matrix + matrix
print('c:', c)