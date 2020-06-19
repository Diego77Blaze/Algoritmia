def camionBacktracking(mapa, numFilas, numColumnas, movimientos, actX, actY, orientacion, giros, minGiros, posFinal):
    if (mapa[actX][actY] == '2'):
        posFinal.append(actX)
        posFinal.append(actY)
        posFinal.append(orientacion)
        if minGiros[0] == -1:
            minGiros[0] = giros
        else:
            if giros < minGiros[0]:
                minGiros[0] = giros
        datos = []
        datos.append(giros)
        caminosTupla = convertirCaminoTupla(caminos)
        datos.append(caminosTupla)
        sols.append(datos)
        return True
    else:
        for value in list(conteoCasillas.values()):
            if value > 3:
                return False
        for i in range(2):
            testOrientacion = movimientos[orientacion][i][0]
            testX = actX + movimientos[orientacion][i][1]
            testY = actY + movimientos[orientacion][i][2]
            if i == 1:
                giros = giros + 1
            if (0 <= testX < numColumnas and 0 <= testY < numFilas and (
                    mapa[testX][testY] == '0' or mapa[testX][testY] == '*' or mapa[testX][testY] == '2')):
                if mapa[testX][testY] != "2":
                    mapa[testX][testY] = '*'
                    posicion = [testX, testY, testOrientacion]
                    caminos.append(posicion)
                    casillaKey = str(testX) + str(testY)
                    if casillaKey not in conteoCasillas:
                        conteoCasillas[casillaKey] = 1
                    else:
                        conteoCasillas[casillaKey] = conteoCasillas.get(casillaKey) + 1
                if not camionBacktracking(mapa, numFilas, numColumnas, movimientos, testX, testY, testOrientacion,
                                          giros, minGiros, posFinal):
                    casillaKey = str(testX) + str(testY)
                    mapa[testX][testY] = '0'
                    if len(caminos) != 0:
                        caminos.pop()
                    if casillaKey in conteoCasillas:
                        conteoCasillas[casillaKey] = conteoCasillas.get(casillaKey) - 1
    return False


def convertirCaminoTupla(caminos):
    tupla = []
    for i in range(len(caminos)):
        lineaTupla = []
        for j in range(3):
            lineaTupla.append(caminos[i][j])
        tupla.append(lineaTupla)
    tuplafinal = tuple(tupla)
    return tuplafinal


archivo = open("ejemplo_backtracking.txt").read()
lista = archivo.split('\n')
lado1 = int(lista[1][0])
lado2 = int(lista[0][0])
matriz = []
for i in range(2, lado2 + 2):
    linea = lista[i].split()
    lineaMatriz = []
    for elem in linea:
        lineaMatriz.append(elem)
    matriz.append(lineaMatriz)
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == '1':
            posInicioX = i
            posInicioY = j
movimientosXY = {
    'u': [['u', -1, 0], ['r', 0, 1]],
    'r': [['r', 0, 1], ['d', 1, 0]],
    'd': [['d', 1, 0], ['l', 0, -1]],
    'l': [['l', 0, -1], ['u', -1, 0]]
}
posFinal = []
minGiros = [-1]
sols = []
caminos = []
conteoCasillas = {}
dirIni = 'l'
f = open("resultado_backtracking.txt", "w")
f.write("")
f.close()
res = camionBacktracking(matriz, lado1, lado2, movimientosXY, posInicioX, posInicioY, dirIni, 0, minGiros, posFinal)
f = f = open("resultado_backtracking.txt", "a")
for i in range(len(sols)):
    f.write("Solución " + str(i + 1) + "\n")
    mapaTupla = tuple(matriz)
    for j in range(lado2):
        for k in range(lado1):
            for elem in sols[i][1]:
                if j == elem[0] and k == elem[1]:
                    mapaTupla[j][k] = '*'
    for l in range(lado2):
        for m in range(lado1):
            f.write(str(mapaTupla[l][m]) + " ")
        f.write("\n")
    f.write("[" + str(posInicioX) + ", " + str(posInicioY) + ", " + dirIni + "], ")
    for w in range(len(sols[i][1]) - 1):
        f.write("[" + str(sols[i][1][w][0]) + ", " + str(sols[i][1][w][1]) + ", " + sols[i][1][w + 1][2] + "], ")
    f.write("[" + str(sols[i][1][len(sols[i][1]) - 1][0]) + ", " + str(sols[i][1][len(sols[i][1]) - 1][1]) + ", " + posFinal[2 + (3 * i)] + "], [" + str(posFinal[0 + (3 * i)]) + ", " + str(posFinal[1 + (3 * i)]) + ", FINISHED]")
    if sols[i][0] == minGiros[0]:
        f.write("\nEsta solución es óptima dado que tiene " + str(minGiros[0]) + " giros")
    f.write("\n\n")
