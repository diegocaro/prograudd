#Sumo numeros desde 1 a n
#Cuento numeros desde 1 a n
n = int(input("Ingrese un numero: "))
suma = 0 #acumulador
contador = 0 #contador

while contador <= n:
  suma = suma + contador
  contador =  contador + 1

print('Suma', suma)
print('Contador', contador-1) #Si no cuento uno más
