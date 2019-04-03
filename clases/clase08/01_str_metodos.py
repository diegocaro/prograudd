cadena = "---programaresmuydivertido---"
print('\n')

# Usando strip() para borrar todos los '-' 
print ( "1. String despues de remover '-' antes y después: ") 
print ( cadena.strip('-') ) 
print('\n')

# Usando lstrip para borrar los '-' anteriores
print ( "2. String después de remover todos '-' anteriores: ") 
print ( cadena.lstrip('-') ) 
print('\n')

# Usando rstrip para borrar los '-' posteriores
print ( "3. String después de remover todos los '-' posteriores: ") 
print ( cadena.rstrip('-') ) 
print('\n')


# Usando split() para separar
x = 'azul,rojo,verde'
print('4. String para separar por comas: ' + x + '\n')

print('5. String para separado por comas: ' + str(x.split(",")))
print(x.split(",", 1))
print('\n')

# Usando replace() para reemplazar
print ( "6. String despues de reemplazar 'divertido' por 'aburrido'") 
print(cadena.replace('divertido', 'aburrido', 1))
