def promedio(lista):
    s = 0
    for e in lista:
        s += e
    return s/len(lista)
    
L = [1,2,3,4]
print(promedio(L))

L2 = [44,55,66,77]
print(promedio(L2))
