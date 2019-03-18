while True:
    print('Escoge una dificultad: ')
    print('a) fácil\nb) difícil\nc) hardcore')
    opc = input()
    if opc == 'a':
        print('Escogíste fácil')
        break
    elif opc == 'b':
        print('Ahahaha... es tu opción ir por el camino difícil')
        break
    elif opc == 'c':
        print('Es cosa tuya perder el tiempo...')
        s = input('estás segure? Si/No: ')
        if s == 'S' or s == 'Si':
            break
        else: 
            print('Todos nos podemos arrepentir. Inténtalo otra vez.\n')
    else:
        print('Esa opción no existe... intenta otra vez.\n')