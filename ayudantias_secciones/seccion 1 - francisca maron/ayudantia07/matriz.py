#---------------------------------------------------------------------------------------------------------------------------------
# matriz.py
#---------------------------------------------------------------------------------------------------------------------------------

import sys
import random


def creacion(m,n):
#Retorna una matriz de m por n sólo con valores 0

	matriz = m*[0]
	for i in range(m):
		matriz[i] = n*[0]
	return matriz

def creacionrand(m,n):
#Retorna una matriz de m por n sólo con valores enteros random entre 1 y 99

	matriz = creacion(m,n)
	for i in range(m):
		for j in range(n):
			matriz[i][j] = random.randrange(1,100)
	return matriz	

def printmatriz(matriz):
#Imprime cada fila de una matriz, mejorar por que imprima cada elemento por filas. Mejorar función!
	for i in range(len(matriz)):
		print(matriz[i])
	 
def matriztostr(matriz):
#Transforma una matriz de integer o float en un sólo string, retorna un string

def identidad(n):
# Retorna una matriz de identidad n por n

def punto(v1,v2):
#Retorna el producto punto del vector1 y vector2

def traspuesta(m):
#Retorna la matriz traspuesta de m

def sumar(m1, m2):
#Retorna la matriz que suma de las matrices m1 y m2

def resta(m1, m2):
#Retorna la matriz que resta a la matriz m1, m2

def multiplicaciónMM(m1, m2):
#Retorna la matriz que es la multiplicación entre la matriz m1 y m2

def multiplicaciónMV(m, v):
#Retorna el vector que es la multiplicación de m*v

def multiplicaciónVM(v, m):
#Retorna el vector que es la multiplicación de v*m



def main():
	#print(creacionrand(10,20))
	printmatriz(creacionrand(10,20))

if __name__ == '__main__':
    main()

