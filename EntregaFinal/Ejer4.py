archivo = open("Ejer4Input.txt").read()
lista = archivo.split('\n')
lado1 = int(lista[0][0])
lado2 = int(lista[1][0])
print(lado1, lado2)
matriz = []
for i in range(2, lado2+1):
    linea = lista[i].split()
    lineaMatriz = []
    for elem in linea:
        lineaMatriz.append(elem)
    matriz.append(lineaMatriz)
print(matriz)








