n = int(input('ingrese n: '))
if n <= 0: 
    print('Debe ingresar un número mayor a cero')
i = 0
while i < n:
    if i % 2 == 1:
        print(i)
    i = i+1