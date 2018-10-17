def f(a):
    a[2] = 'a'

x = "hola"
f(x)
print(x)

x = [5, 7, 11, 42]
f(x)
print(x)