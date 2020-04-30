def main(matriz):
    anchura = len(matriz)
    if (anchura == 2) or (anchura % 2 != 0):
        matriz = transponerSubMatriz(matriz)
    else:
        mini1 = crearSubMatriz(matriz, 0, int(anchura / 2), 0, int(anchura / 2))
        mini2 = crearSubMatriz(matriz, int(anchura / 2), anchura, 0, int(anchura / 2))
        mini3 = crearSubMatriz(matriz, 0, int(anchura / 2), int(anchura / 2), anchura)
        mini4 = crearSubMatriz(matriz, int(anchura / 2), anchura, int(anchura / 2), anchura)
        mini1 = main(mini1)
        mini2 = main(mini2)
        mini3 = main(mini3)
        mini4 = main(mini4)
        matriz = juntarMatriz(mini1, mini3, mini2, mini4)
    return matriz

def crearSubMatriz(matriz, minX, maxX, minY, maxY):
    subMatriz = []
    for i in range(minX, maxX):
        row = []
        for j in range(minY, maxY):
            row.append(matriz[i][j])
        subMatriz.append(row)
    return subMatriz

def transponerSubMatriz(subMatriz):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(0,len(subMatriz)):
        for j in range(0,len(subMatriz)):
            result[j][i] = subMatriz[i][j]
    return result


def juntarMatriz(mini1, mini2, mini3, mini4):
    matriz = []
    for i in range (0, int(len(mini1)*2)):
        row = []
        if i < int(len(mini1)):
            for j in range(0, int(len(mini1)*2)):
                if j < int(len(mini1)):
                    row.append(mini1[i][j])
                else:
                    row.append(mini2[i][j-int(len(mini2))])
            matriz.append(row)
        else:
            for j in range(0, int(len(mini3)*2)):
                if j < int(len(mini3)):
                    row.append(mini3[i-int(len(mini3))][j])
                else:
                    row.append(mini4[i-int(len(mini4))][j-int(len(mini4))])
            matriz.append(row)
    return matriz


costes = [[0,1,4,2,999,999],
          [3,0,999,4,999,999],
          [3,999,0,999,999,2],
          [999,999,1,0,1,999],
          [1,999,999,999,0,1],
          [7,999,999,3,0,0]]

print("Matriz inicial: ")
for i in costes:
    print(i)

costes = main(costes)
print("Matriz final: ")
for i in costes:
    print(i)











