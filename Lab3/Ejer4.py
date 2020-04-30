listacorchos = [1,3,9,7,5,4,8,2,6]
listabotellas = [6,9,8,7,4,1,2,3,5]

def particion(arr, low, high):
    indice = (low - 1)
    pivote = arr[high]
    for i in range(low, high):
        if arr[i] <= pivote:
            indice = indice + 1
            arr[indice], arr[i] = arr[i], arr[indice]
    arr[indice + 1], arr[high] = arr[high], arr[indice + 1]
    return (indice + 1)

def quickSort(arr, low, high):
    if low < high:
        part = particion(arr, low, high)
        quickSort(arr, low, part - 1)
        quickSort(arr, part + 1, high)

def busquedabinaria(arr, elem, izq, der):
    if izq > der:
        return -1
    mid = (izq + der) // 2
    if arr[mid] == elem:
        return arr[mid]
    elif arr[mid] > elem:
        return busquedabinaria(arr, elem, izq, mid - 1)
    else:
        return busquedabinaria(arr, elem, mid + 1, der)


n = len(listabotellas)
quickSort(listabotellas,0,n-1)

for elem in listacorchos:
    print("Corcho: ", elem, ", Botella: " , busquedabinaria(listabotellas,elem,0,n-1))
