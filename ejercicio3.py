#Algoritmo QuickSort para ordenar un arreglo de 8 números
lista=[8,3,12,4,2,9,7,1]

def particionado(lista):
    pivote=lista[0]
    nmenores=[]
    nmayores=[]

    for i in range(1, len(lista)):
        if lista[i] < pivote:
            nmenores.append(lista[i])
        else:
            nmayores.append(lista[i])

    return nmenores, pivote, nmayores

def quicksort(lista):
    if len(lista) < 2:
        return lista
    nmenores, pivote, nmayores= particionado(lista)
    return quicksort(nmenores) + [pivote]+ quicksort(nmayores)

print(quicksort(lista))
