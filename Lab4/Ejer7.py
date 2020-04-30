def posMaximo(maximo, tabla):
    pos = -1
    iterador = 0
    existe = False
    while not existe and iterador < len(tabla[len(tabla) - 1]):
        if tabla[len(tabla) - 1][iterador] == maximo:
            pos = iterador
            existe = True
        iterador = iterador + 1
    return pos


def maximaSubsecuencia(tabla):
    resultado = 0
    for i in range(len(tabla[len(tabla) - 1])):
        if tabla[len(tabla) - 1][i] > resultado:
            resultado = tabla[len(tabla) - 1][i]
    return resultado


def numPosicionesContiguas(cadena1, cadena2, num1, num2):
    if num2 < len(cadena2) and num1 < len(cadena1) and cadena1[num1] == cadena2[num2]:
        resultado = 1 + numPosicionesContiguas(cadena1, cadena2, num1 + 1, num2 + 1)
    else:
        resultado = 0
    return resultado


def subsecuenciaComun(tabla, secuenciaBits):
    pos = posMaximo(maximaSubsecuencia(tabla), tabla)
    valorPos = tabla[len(tabla) - 1][pos]
    subcadena = []
    for i in range(pos, pos + valorPos):
        subcadena.append(secuenciaBits[i])
    return subcadena


def crearTablaSecuencias(cadena1, cadena2):
    tabla = []
    for i in range(len(cadena1)):
        fila = []
        for j in range(len(cadena2)):
            if i == 0:
                if cadena1[i] == cadena2[j]:
                    fila.append(1)
                else:
                    fila.append(0)
            else:
                if tabla[i - 1][j] >= 0:
                    if j + tabla[i - 1][j] < len(tabla[i - 1]) and cadena1[i] == cadena2[j + tabla[i - 1][j]]:
                        fila.append(tabla[i - 1][j] + 1)
                    else:
                        if abs(tabla[i - 1][j]) < numPosicionesContiguas(cadena1, cadena2, i, j):
                            fila.append(1)
                        else:
                            fila.append(- tabla[i - 1][j])
                else:
                    if abs(tabla[i - 1][j]) < numPosicionesContiguas(cadena1, cadena2, i, j):
                        fila.append(1)
                    else:
                        fila.append(tabla[i - 1][j])
        tabla.append(fila)
    aux = []
    for i in range(len(tabla)):
        fila = []
        for j in range(len(tabla[i])):
            fila.append(abs(tabla[i][j]))
        aux.append(fila)
    return aux


cadena1 = "01101010"
cadena2 = "101001001"
tabla = crearTablaSecuencias(cadena1, cadena2)
for i in range(len(tabla)):
    for j in range(len(tabla[i])):
        print(tabla[i][j], end=" ")
    print("\n")
print("Longitud de la subcadena más larga: ", maximaSubsecuencia(tabla))
subcadena = subsecuenciaComun(tabla, cadena2)
print("Esta es una de las posibilidades: ", end="")
for i in range(len(subcadena)):
    print(subcadena[i], end=" ")
exit()