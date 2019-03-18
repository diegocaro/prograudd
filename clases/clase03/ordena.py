# argv contiene los argumentos entregados
# por el usuario en la consola
from sys import argv 
a = int(argv[1])
b = int(argv[2])
c = int(argv[3])
if b < a:
    a, b = b, a
if c < a:
    a, c = c, a
if c < b:
    c, b = b, c
print(a)
print(b)
print(c)