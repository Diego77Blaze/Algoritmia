def backtrackingCaballo(tab, ladoTab1, ladoTab2, numMov, posibX, posibY, actX, actY):
    if (numMov==ladoTab1*ladoTab2+1):
        return True
    for i in range(len(posibX)):
        testX = actX + posibX[i]
        testY = actY + posibY[i]
        if 0 <= testX < ladoTab2 and 0 <= testY < ladoTab1 and tab[testX][testY] == "-":
            tab[testX][testY] = numMov
            if backtrackingCaballo(tab, ladoTab1, ladoTab2, numMov + 1, posibX, posibY, testX, testY):
                return True
            else:
                tab[testX][testY] = "-"
    return False

print("Cuántas casillas quieres que tenga el lado del tablero?")
lado1 = int(input())
print("Cuántas casillas quieres que tenga el lado del tablero?")
lado2 = int(input())
tablero = [["-" for i in range(lado1)] for i in range(lado2)]
movimientosX = [2, 1, -1, -2, -2, -1, 1, 2]
movimientosY = [1, 2, 2, 1, -1, -2, -2, -1]
tablero[0][0] = 1
res = backtrackingCaballo(tablero, lado1, lado2, 2, movimientosX, movimientosY, 0, 0)
if res == True:
    for i in range(lado2):
        for j in range(lado1):
            print(tablero[i][j], end=' ')
        print()
else:
    print("No se ha podido encontrar solución")
