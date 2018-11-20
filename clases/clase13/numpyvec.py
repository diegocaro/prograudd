import numpy as np

a = np.array([5, 0, 3, 3, 7, 9])
b = np.array([3, 5, 2, 4, 7, 6])

c = 2 + a # scalar + vector
print('c:', c)

c = a + b # vector + vector (also -,/,*,%)
print('c:', c)