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

def main():
    print(crear(10,20))

if __name__ == '__main__':
    main()
