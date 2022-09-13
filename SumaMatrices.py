#Suma de 2 matrices
Filas=int(input("Numero de filas: "))
Columnas=int(input("Numero de columnas: "))

#MATRIZ 1
print('---------MATRIZ 1---------')
matriz1=[]
for i in range(Filas):
    matriz1.append([0]*Columnas)

for i in range(Filas):
    for j in range(Columnas):
        matriz1[i][j]=int(input('Coordenada (%d,%d): '%(i,j)))

#MATRIZ 2
print('---------MATRIZ 2---------')
matriz2=[]
for i in range(Filas):
    matriz2.append([0]*Columnas)

for i in range(Filas):
    for j in range(Columnas):
        matriz2[i][j]=int(input('Coordenada (%d,%d): '%(i,j)))

#Se imprimen las matrices
print('MATRIZ 1:')
for i in range(Filas):
    print(matriz1[i])

print('MATRIZ 2')
for i in range(Filas):
    print(matriz2[i])

#Matriz resultante
matrizR=[]
for i in range(Filas):
    matrizR.append([0]*Columnas)

#SUMA
for i in range(Filas):
    for j in range(Columnas):
        matrizR[i][j]=matriz1[i][j] + matriz2[i][j]

#Impresion de la matriz resultante
print('MATRIZ RESULTANTE')
for i in range(Filas):
    print(matrizR[i])