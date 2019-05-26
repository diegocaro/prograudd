a = [5, 0, 3, 3, 7, 9]
b = [3, 5, 2, 4, 7, 6]
c = [0]*len(a)

# scalar and vector
for i in range(len(a)): c[i] = 2 + a[i]
print('c:', c)

# vector and vector
for i in range(len(a)): c[i] = a[i] + b[i]
print('c:', c)