def convertirTupla(lado1, lado2, matrizSolucion):
    tupla = []
    for i in range(lado2):
        lineaTupla = []
        for j in range(lado1):
            lineaTupla.append(matrizSolucion[i][j])
        tupla.append(lineaTupla)
    tuplafinal = tuple(tupla)
    return tuplafinal


matriz = [[1,2,3,4],[5,6,7,8]]
lado1 = 4
lado2 = 2

convertirTupla(lado1, lado2, matriz)