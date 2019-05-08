def crear(m,n):
    #Retorna una matriz de ceros con m filas por n columnas
    matriz = []
    for i in range(m):
        matriz.append([0]*n)
    return matriz

def imprimir(matriz):
    #Imprime cada fila de una matriz
    for fila in matriz:
        for elem in fila:
            print(elem, end=' ')
        print()

def asignar(matriz, i,j,v):
    matriz[i][j] = v

def str(matriz):
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

def multiplicacionMM(m1, m2):
#Retorna la matriz que es la multiplicación entre la matriz m1 y m2

def multiplicacionMV(m, v):
#Retorna el vector que es la multiplicación de m*v

def multiplicacionVM(v, m):
#Retorna el vector que es la multiplicación de v*m




def main():
    print(crear(10,20))

if __name__ == '__main__':
    main()
