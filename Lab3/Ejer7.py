import numpy as np

matriz = [0,1,4,2,999,999,
          3,0,999,4,999,999,
          3,999,0,999,999,2,
          999,999,1,0,1,999,
          1,999,999,999,0,1,
          7,999,999,3,0,0]

resultadofinal = []

def divisorMatriz (matriz):
    cuadrante1 = []
    cuadrante2 = []
    cuadrante3 = []
    cuadrante4 = []
    anch = len(matriz) ** (1 / 2)
    for i in range(len(matriz)):
        if i % anch == 0 or i % anch == 1 or i % anch == 2:
            if i < ((anch ** 2) / 2):
                cuadrante1.append(matriz[i])
            else:
                cuadrante3.append(matriz[i])
        else:
            if i < ((anch ** 2) / 2):
                cuadrante2.append(matriz[i])
            else:
                cuadrante4.append(matriz[i])
    transponerMatriz(cuadrante1)
    transponerMatriz(cuadrante2)
    transponerMatriz(cuadrante3)
    transponerMatriz(cuadrante4)

def transponerMatriz (matriz):

    if len(matriz)>4 and len(matriz)%4==0:
        divisorMatriz(matriz)
    else:
        data = np.array(matriz)
        anch = int(len(matriz) ** (1 / 2))
        shape = (anch, anch)
        matriz = data.reshape(shape)
        resultado = matriz.transpose()
        data2 = np.array(resultado)
        shape = (1, anch**2)
        resultado = data2.reshape(shape)
        resultadofinal.append(resultado.tolist())

transponerMatriz(matriz)

def imprimirMatrizTranspuesta(matriz):
    print(matriz[0][0][0], matriz[0][0][1], matriz[0][0][2], matriz[2][0][0], matriz[2][0][1], matriz[2][0][2])
    print(matriz[0][0][3], matriz[0][0][4], matriz[0][0][5], matriz[2][0][3], matriz[2][0][4], matriz[2][0][5])
    print(matriz[0][0][6], matriz[0][0][7], matriz[0][0][8], matriz[2][0][6], matriz[2][0][7], matriz[2][0][8])
    print(matriz[1][0][0], matriz[1][0][1], matriz[1][0][2], matriz[3][0][0], matriz[3][0][1], matriz[3][0][2])
    print(matriz[1][0][3], matriz[1][0][4], matriz[1][0][5], matriz[3][0][3], matriz[3][0][4], matriz[3][0][5])
    print(matriz[1][0][6], matriz[1][0][7], matriz[1][0][8], matriz[3][0][6], matriz[3][0][7], matriz[3][0][8])

imprimirMatrizTranspuesta(resultadofinal)





