#pizzas.py
numpizzas = input('Ingrese número de pizzas grandes, medianas y pequeñas:')
pizzas = []
for p in numpizzas.split(','):
    pizzas.append(int(p))
    
print('Número de pizzas grandes:', pizzas[0])
print('Número de pizzas medianas:', pizzas[1])
print('Número de pizzas pequeñas:', pizzas[2])

total = 4600*pizzas[2] + 7850*pizzas[1] + 10750*pizzas[0]
print('Total a pagar:', total)
