from random import randrange
TRAJES = ['Picas', 'Diamantes', 'Treboles', 'Corazones']
VALORES = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
         'Jota', 'Reina', 'Rey', 'As']

mazo = []
for traje in TRAJES:
    for valor in VALORES:
        mazo.append(valor + ' de ' + traje)

print(mazo)