#Multiplicacion de matrices 3x3

#MATRIZ 1
print('\n---------MATRIZ 1---------')
fila1=int(input("Numero de filas: "))
columna1=int(input("Numero de columnas: "))
print('\n')

#MATRIZ 2
print('---------MATRIZ 2---------')
fila2=int(input("Numero de filas: "))
columna2=int(input("Numero de columnas: "))
print('\n')

if(columna1==fila2):

    #MATRIZ 1
    matriz1=[]
    for i in range(fila1):
        matriz1.append([0]*columna1)

    print('---------MATRIZ 1---------')
    for i in range(fila1):
        for j in range(columna1):
            matriz1[i][j]=int(input('Componente (%d,%d): '%(i,j)))
    print('\n')

    #MATRIZ 2
    matriz2=[]
    for i in range(fila2):
        matriz2.append([0]*columna2)
    print('---------MATRIZ 2---------')

    for i in range(fila2):
        for j in range(columna2):
            matriz2[i][j]=int(input('Componente (%d,%d): '%(i,j)))
    print('\n')

    #Imprimir matrices
    print('MATRIZ 1')
    for i in range(fila1):
        print(matriz1[i])
    print('\n')

    print('MATRIZ 2')
    for i in range(fila2):
        print(matriz2[i])
    print('\n')

    #Se crea la matriz resultante
    matrizR=[]
    for i in range(fila1):
        matrizR.append([0]*columna2)

    #MULTIPLICACIÓN
    for i in range(fila1):
        for j in range(columna2):
            for k in range(fila2):
                matrizR[i][j] += matriz1[i][k] * matriz2[k][j]

    #Matriz resultante
    print('La matriz resultante es:')
    print(matrizR)
