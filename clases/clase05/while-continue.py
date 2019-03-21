L = [0, -1, 3, 5, 9, 10, 12, 99, 33]
t = 0
i = 0
while i < len(L)
    e = L[i]
    i += 1
    if e < 0:
        continue
    t += e
print(t)
