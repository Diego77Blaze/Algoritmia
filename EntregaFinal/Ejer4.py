def camionBacktracking(mapa, numFilas, numColumnas, movimientos,actX, actY, orientacion):
    #añadir cota para si se ha pasado varias veces por la misma casilla con un if()
    if(mapa[actX][actY]=='2'):
        printear(mapa)
        sols.append(mapa)
        return True
    for posibleMov in movimientos[orientacion]:
        testOrientacion = posibleMov[0]
        testX = actX + posibleMov[1]
        testY = actY + posibleMov[2]
        if(0<=testX<numColumnas and 0<=testY<numFilas and (mapa[testX][testY]=='0' or mapa[testX][testY]=='*' or mapa[testX][testY]=='2')):
            if mapa[testX][testY] !="2":
                mapa[testX][testY] = '*'
            if camionBacktracking(mapa, numFilas, numColumnas, movimientos,testX,testY,testOrientacion):
                return True
            else:
                mapa[testX][testY] = '0'
    return False

def printear(mapa):
    for i in range(lado2):
        for j in range(lado1):
            print(mapa[i][j], end=' ')
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
print(posInicioX, posInicioY)
movimientosXY = {
                'u': [['u', -1, 0], ['r', 0, 1]],
                'r': [['r', 0, 1], ['d', 1, 0]],
                'd': [['d', 1, 0], ['l', 0, -1]],
                'l': [['l', 0, -1], ['u', -1, 0]]
                }
sols = []
res = camionBacktracking(matriz, lado1, lado2, movimientosXY, posInicioX, posInicioY,'l')
if res == True:
    for result in sols:
        printear(result)

