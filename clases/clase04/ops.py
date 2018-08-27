L = [11, 3, 5, 7, 2]
print('L', L)

if 5 in L:
    print('cinco está en L')

# Actualizar elemento
L[4] = 9999
print('L[4]=9999', L)

# Agregar elemento a listas
L.append(100) #modifica lista
print('L.append(100)', L)

# Concatenar lista
L2 = L + [19, 17, 13] # crea lista nueva
print('L+[19, 17, 13]', L2)

# Sublista
L3 = L[2:5] # Elementos 2,3 y 4
print('L[2:5]', L3)