s = "Hola mundo!"
print('tamaño s', len(s))

# concatenar
s1 = 'Hola'
s2 = 'Chao'
s3 = s1 + s2
print(s3)

# acceso, la primera posición comienza en 0
print(s1[3]) # imprime el 4to element

# substring
s4 = s[1:6]
print('s[1:6] = ', s4)

# actualizar string: concatenar
nuevo = "m" + s[1:]
print(nuevo)

# actualizar string: reemplazar
nuevo2 = "m{}".format(s[1:])
print(nuevo2)