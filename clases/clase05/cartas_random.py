from random import randrange
TRAJES = ['Picas', 'Diamantes', 'Treboles', 'Corazones']
VALORES = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
         'Jota', 'Reina', 'Rey', 'As']
         
valor = randrange(0, len(VALORES))
traje = randrange(0, len(TRAJES))
print(VALORES[valor],'de', TRAJES[traje])
