# ingresa tres números enteros por teclado
# separados por un espacio
a = int(input())
b = int(input())
c = int(input())
if b < a:
    a, b = b, a
if c < a:
    a, c = c, a
if c < b:
    c, b = b, c
print(a)
print(b)
print(c)