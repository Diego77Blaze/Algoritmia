def backtrackingCaballo(tab, ladoTab, numMov, posibX, posibY, actX, actY):
    if (numMov==ladoTab**2+1):
        return True
    for i in range(len(posibX)):
        testX = actX + posibX[i]
        testY = actY + posibY[i]
        if 0 <= testX < lado and testY >= 0 and testY < lado and tab[testX][testY] == "-":
            tab[testX][testY] = numMov
            if backtrackingCaballo(tab, ladoTab, numMov + 1, posibX, posibY, testX, testY):
                return True
            else:
                tab[testX][testY] = "-"
    return False

print("Cuántas casillas quieres que tenga el lado del tablero?")
lado = int(input())
tablero = [["-" for i in range(lado)] for i in range(lado)]
movimientosX = [2, 1, -1, -2, -2, -1, 1, 2]
movimientosY = [1, 2, 2, 1, -1, -2, -2, -1]
tablero[0][0] = 1
res = backtrackingCaballo(tablero, lado, 2, movimientosX, movimientosY, 0, 0)
if res == True:
    for i in range(lado):
        for j in range(lado):
            print(tablero[i][j], end=' ')
        print()
else:
    print("No se ha podido encontrar solución")