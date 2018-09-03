L = 10000000*[0, -1, 3, 5, 9, 10, 12, 99, 33]
print('len(L):', len(L))

a = False
for e in L:
    if e < 0:
        a = True
print(a)
