n = int(input('ingrese n: '))
if n <= 0: 
    print('Debe ingresar un número mayor a cero')
for i in range(n):
    if i % 2 == 1:
        print(i)