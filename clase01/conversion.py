amigos = input('Cuantos amigues tienes en facebook? ')
comun = input('Cuantos amigues tienes en comun con tu mejor amigue? ')

num_amigos = int(amigos)
num_comun = int(comun)
porcentaje = num_comun/num_amigos*100
print('Wow, tienes', porcentaje, '% de amigues en comun con tu mejor amigue!')

print('tipo variable amigos:', type(amigos))
print('tipo variable num_amigos:', type(num_amigos))