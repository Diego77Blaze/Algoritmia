def esPotenciaDos(num):
    if num == 0:
        return False
    while num != 1:
        if num % 2 != 0:
            return False
        num = num // 2
    return True


def divideYVenceras(listaNotas):
    if len(listaNotas) / 2 == 1:
        media = (listaNotas[0] + listaNotas[1]) / 2
        f.write("Valor medio de " + str(listaNotas[0]) + " " + str(listaNotas[1]) + " = " + str(media) + "\n")
        return media
    else:
        n = len(listaNotas)
        lista1 = listaNotas[0:int(n / 2)]
        lista2 = listaNotas[int(n / 2):n]
        media = (divideYVenceras(lista1) + divideYVenceras(lista2)) / 2
        f.write("Valor medio de " + str(lista1) + " " + str(lista2) + " = " + str(media) + "\n")
        return media


def divideYVenceras2(listaNotas):
    if len(listaNotas) == 1:
        f.write("Valor medio de " + str(listaNotas[0]) + " = " + str(listaNotas[0]) + "\n")
        return listaNotas[0]
    elif len(listaNotas) == 2:
        suma = listaNotas[0] + listaNotas[1]
        f.write("Valor medio de " + str(listaNotas[0]) + " " + str(listaNotas[1]) + " = " + str((listaNotas[0] + listaNotas[1])/2) + "\n")
        return suma
    else:
        n = len(listaNotas)
        lista1 = listaNotas[0:int(n / 2)]
        lista2 = listaNotas[int(n / 2):n]
        sumaTotal = divideYVenceras2(lista1) + divideYVenceras2(lista2)
        f.write("Valor medio de " + str(lista1) + " " + str(lista2) + " = " + str(sumaTotal/n) + "\n")
        return sumaTotal


archivo = open("ejemplo_dyv.txt").read()
notasAsignaturas = []
lineasArchivo = archivo.split('\n')
for linea in lineasArchivo:
    if linea != "":
        notasAsignaturas.append(int(linea))
f = open("resultado_dyv.txt", "w")
f.write("Notas de las asignaturas: " + str(notasAsignaturas) + "\n")
f.close()
if esPotenciaDos(len(notasAsignaturas)):
    f = f = open("resultado_dyv.txt", "a")
    f.write("El tamaño del array es potencia de dos\n")
    w = divideYVenceras(notasAsignaturas)
    f.write("--> Resultado = " + str(w))
else:
    f = open("resultado_dyv.txt", "a")
    f.write("El tamaño del array no es potencia de dos\n")
    l = len(notasAsignaturas)
    w = divideYVenceras2(notasAsignaturas)
    f.write(str(w) + "/" + str(l) + "--> Resultado = " + str(w/l))

