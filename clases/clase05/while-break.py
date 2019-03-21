L = 10000000*[0, -1, 3, 5, 9, 10, 12, 99, 33]
print('len(L):', len(L))

a = False
i = 0
while i < len(L):
    if L[i] < 0:
        a = True
        break
    i += 1
print(a)
