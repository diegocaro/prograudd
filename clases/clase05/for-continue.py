L = [0, -1, 3, 5, 9, 10, 12, 99, 33]
t = 0
for e in L:
    if e < 0:
        continue
    t += e
print(t)
