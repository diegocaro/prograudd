num_amigos = input('Cuantos amigues tienes en facebook? ')
num_comun = input('Cuantos amigues tienes en comun con tu mejor amigue? ')

porcentaje = num_comun/num_amigos*100
print('Wow, tienes', porcentaje, '% de amigues en comun con tu mejor amigue!')

print('tipo variable amigos:', type(amigos))
print('tipo variable num_amigos:', type(num_amigos))