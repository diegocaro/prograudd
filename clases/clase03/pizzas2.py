# pizzas2.py
i = int(input('¿Cuántas pizzas individuales desea?: '))
m = int(input('¿Cuántas pizzas mediandas desea?: '))
f = int(input('¿Cuántas pizzas familiares desea?: '))

if i < 0 or m < 0 or f < 0:
    print('Error en el número de pizzas')
else:
    total = 4600*i + 7850*m + 10750*f
    print('Total a pagar:', total)

total = 4600*i + 7850*m + 10750*f
print('Total a pagar:', total)