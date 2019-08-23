#cuenta los pares
numero = int(input("Ingrese un numero: "))
i=1

contador = 0

while i <= numero:
    if i % 2 == 0:
        print(i, 'es par')
        contador += 1
    i += 1
print('Numeros de pares entre 1 y ' + str(numero) + ':', contador)
