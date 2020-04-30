def TransponerMatriz(matriz):
    anchura = len(matriz)
    mini1 = crearSubMatriz(matriz, 0, int(anchura/2), 0, int(anchura/2))
    mini2 = crearSubMatriz(matriz,int(anchura/2), anchura, 0, int(anchura/2))
    mini3 = crearSubMatriz(matriz,0, int(anchura/2), int(anchura/2), anchura)
    mini4 = crearSubMatriz(matriz,int(anchura/2), anchura, int(anchura/2), anchura)
    mini1 = TransponerSubMatriz(mini1)
    mini2 = TransponerSubMatriz(mini2)
    mini3 = TransponerSubMatriz(mini3)
    mini4 = TransponerSubMatriz(mini4)
    juntarMatriz(matriz, mini1, 0, 0)
    juntarMatriz(matriz, mini2, 0, anchura/2)
    juntarMatriz(matriz, mini3, anchura/2, 0)
    juntarMatriz(matriz, mini4, anchura/2, anchura/2)

def crearSubMatriz(matriz, minX, maxX, minY, maxY):
    subMatriz = []
    for i in range(minX, maxX):
        row = []
        for j in range(minY, maxY):
            row.append(matriz[i][j])
        subMatriz.append(row)
    return subMatriz

def TransponerSubMatriz(subMatriz):
    result = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    for i in range(len(subMatriz)):
        for j in range(len(subMatriz[0])):
            result[j][i] = subMatriz[i][j]
    return result

def juntarMatriz(matriz, miniMatriz, minX, minY):
    anchura = int(len(matriz)/2)
    for i in range(0, anchura):
        for j in range(0, anchura):
            matriz[int(i+minX)][int(j+minY)] = miniMatriz[i][j]


costes = [[0,1,4,2,999,999],
          [3,0,999,4,999,999],
          [3,999,0,999,999,2],
          [999,999,1,0,1,999],
          [1,999,999,999,0,1],
          [7,999,999,3,0,0]]

print("Matriz inicial: ")
for i in costes:
    print(i)

TransponerMatriz(costes)
print("Matriz final: ")
for i in costes:
    print(i)

