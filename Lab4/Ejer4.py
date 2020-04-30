def getResultValue(maxfila, lista, maxAlforja, weightUsed, result):
    if maxfila >= 0:
        if lista[maxfila][2] == 0 and maxAlforja >= weightUsed + lista[maxfila][0]:
            resultAux = getResultValue(maxfila - 1, lista, maxAlforja, weightUsed + lista[maxfila][0],
                                       result + lista[maxfila][1])
        else:
            resultAux = getResultValue(maxfila - 1, lista, maxAlforja, weightUsed, result)
    else:
        resultAux = result
    return resultAux

def posicionesTablaUsadas(maxfila, lista, maxAlforja, weightUsed, result):
    fila = []
    if maxfila >= 0:
        if lista[maxfila][2] == 0 and maxAlforja >= weightUsed + lista[maxfila][0]:
            listaAux = lista
            fila.append(lista[maxfila][0])
            fila.append(lista[maxfila][1])
            fila.append(1)
            listaAux.pop(maxfila)
            listaAux.insert(maxfila, fila)
            listaAux = posicionesTablaUsadas(maxfila - 1, lista, maxAlforja, weightUsed + lista[maxfila][0],
                                             result + lista[maxfila][1])
        else:
            listaAux = posicionesTablaUsadas(maxfila - 1, lista, maxAlforja, weightUsed, result)
    else:
        listaAux = lista
    return listaAux


def createtabla(max1, max2, lista):
    tabla = []
    fila = []

    for i in range(len(lista)):
        for j in range(max(max1, max2)+1):
            listaAux = []
            for k in range(len(lista)):
                listaAux.append(lista[k])
            if max1 >= j:
                value1 = getResultValue(i, listaAux, j, 0, 0)
                listaAux = posicionesTablaUsadas(i, listaAux, j, 0, 0)
                if max2 >= j:
                    value2 = getResultValue(i, listaAux, j, 0, 0)
                else:
                    value2 = getResultValue(i, listaAux, max2, 0, 0)
            else:
                value1 = getResultValue(i, listaAux, max1, 0, 0)
                listaAux = posicionesTablaUsadas(i, listaAux, max1, 0, 0)
                if max2 >= 0:
                    value2 = getResultValue(i, listaAux, j, 0, 0)
                else:
                    value2 = getResultValue(i, listaAux, max2, 0, 0)
            if i == 0:
                fila.append(value1 + value2)
            else:
                if value1 + value2 > tabla[i - 1][j]:
                    fila.append(value1 + value2)
                elif value1+value2<tabla[i-1][j] and len(tabla)>0 and tabla[i - 1][j] < fila[len(fila) - 1]:
                    fila.append(fila[len(fila) - 1])
                else:
                    fila.append(tabla[i - 1][j])
        tabla.append(fila)
        fila = []
    return tabla



lista1 = [[1, 6, 0], [2, 7, 0], [4, 15, 0], [5, 13, 0]]
pesoMaximoAlforja1 = 3
pesoMaximoAlforja2 = 11

tabla1 = createtabla(pesoMaximoAlforja1, pesoMaximoAlforja2, lista1)
tabla2 = createtabla(pesoMaximoAlforja2, pesoMaximoAlforja1, lista1)
print("tabla 1:")
for i in range(len(tabla1)):
    for j in range(len(tabla1[0])):
        print(tabla1[i][j], end=" ")
    print("\n")

print("tabla 2:")
for i in range(len(tabla2)):
    for j in range(len(tabla1[0])):
        print(tabla2[i][j], end=" ")
    print("\n")

if tabla1[len(tabla1) - 1][max(pesoMaximoAlforja1, pesoMaximoAlforja2) - 1] >= tabla2[len(tabla2) - 1][
    max(pesoMaximoAlforja1, pesoMaximoAlforja2) - 1]:
    print("Resultado: ", tabla1[len(tabla1) - 1][max(pesoMaximoAlforja2, pesoMaximoAlforja1)])
else:
    print("Resultado: ", tabla2[len(tabla1) - 1][max(pesoMaximoAlforja2, pesoMaximoAlforja1)])
