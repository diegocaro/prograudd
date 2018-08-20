# argv contiene los argumentos entregados
# por el usuario en la consola
from sys import argv 
a = int(argv[1])
b = int(argv[2])
if b < a:
    t = b
    b = a
    a = t
print(a)
print(b)