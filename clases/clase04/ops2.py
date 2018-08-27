# lista con valores desde teclado
L = [] #lista vacía
for i in range(N):
    v = int(input())
    L.append(v)

# imprimir elementos en lista
for elem in L:
    print(elem)
    
# imprimir elementos en lista (otra forma)
for i in range(N):
    print(L[i])

# encontrar el máximo 
maxi = L[0]
for elem in L:
    if elem > maxi:
        maxi = elem
print(maxi)


# encontrar el mínimo
mani = L[0]
for elem in L:
    if elem < mini:
        mini = elem
print(mini)

# promedio
suma = 0.0
for elem in L:
    suma = suma + elem
prom = suma/N

# copiar lista
L2 = []
for elem in L:
    L2.append(elem)

# invertir elementos de la lista
for i in range(N):
    temp = L[i]
    L[i] = L[N-i-1]
    L[N-i-1] = temp

# insertar elemento al final
L.append(33)
