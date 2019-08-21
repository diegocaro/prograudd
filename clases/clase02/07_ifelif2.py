a = int(input('ingrese a: '))
b = int(input('ingrese b: '))
if a > b:
    # cuando la condición se cumple
    print('a es mayor que b')
else:
    if a < b:
        # cuando la condición se cumple
        print('a es menor o igual que b')
    else:
        # cuando ni la primera, ni la segunda
        # condición se cumple
        print('a es igual a b')
