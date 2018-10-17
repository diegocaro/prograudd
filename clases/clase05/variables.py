X = 2

def funcion():
    global X
    X = X + 99
    print(X)

print(X)
funcion()
print(X)