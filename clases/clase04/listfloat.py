# calcula producto punto
x = [0.30, 0.60, 0.10]
y = [0.50, 0.10, 0.40]
total = 0.0
for i in range(len(x)):
    total += x[i]*y[i]
print(total)