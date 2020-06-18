def camionBacktracking(mapa, numFilas, numColumnas, movimientos,actX, actY, orientacion, giros, minGiros):
    #añadir cota para si se ha pasado varias veces por la misma casilla con un if()
    if(mapa[actX][actY]=='2'):
        if minGiros[0]==-1:
            minGiros[0]=giros
            datos = []
            datos.append(mapa)
            datos.append(giros)
            datos.append(caminos)
            sols.append(datos)
            return True
        else:
            if(giros<minGiros[0]):
                minGiros[0] = giros
                datos = []
                datos.append(mapa)
                datos.append(giros)
                datos.append(caminos)
                sols.append(datos)
                return True
            else:
                return False
    else:
        for i in range(2):
            testOrientacion = movimientos[orientacion][i][0]
            testX = actX + movimientos[orientacion][i][1]
            testY = actY + movimientos[orientacion][i][2]
            if i ==1:
                giros = giros+1
            if(0<=testX<numColumnas and 0<=testY<numFilas and (mapa[testX][testY]=='0' or mapa[testX][testY]=='*' or mapa[testX][testY]=='2')):
                if mapa[testX][testY] !="2":
                    mapa[testX][testY] = '*'
                    posicion = []
                    posicion.append(testX)
                    posicion.append(testY)
                    caminos.append(posicion)
                if not camionBacktracking(mapa, numFilas, numColumnas, movimientos,testX,testY,testOrientacion, giros, minGiros):
                    mapa[testX][testY] = '0'
                    caminos.pop()

    return False

def printear(mapa):
    for i in range(lado2):
        for j in range(lado1):
            print(mapa[i][j], end=' ')
        print()
    print()

archivo = open("ejemplo_backtracking.txt").read()
lista = archivo.split('\n')
lado1 = int(lista[0][0])
lado2 = int(lista[1][0])
print(lado1, lado2)
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
sols = []
caminos = []
minGiros = [-1]
#diccionario de casillas
res = camionBacktracking(matriz, lado1, lado2, movimientosXY, posInicioX, posInicioY,'l', 0, minGiros)
if res == True:
    for result in sols:
        printear(result)

