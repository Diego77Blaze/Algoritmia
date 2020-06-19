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
        f.write(str(media))
        f.write("  ")
        return media
    else:
        n = len(listaNotas)
        lista1 = listaNotas[0:int(n / 2)]
        lista2 = listaNotas[int(n / 2):n]
        return (divideYVenceras(lista1) + divideYVenceras(lista2)) / 2


def divideYVenceras2(listaNotas):
    if len(listaNotas) == 1:
        f.write(str(listaNotas[0]))
        f.write("  ")
        return listaNotas[0]
    elif len(listaNotas) == 2:
        suma = listaNotas[0] + listaNotas[1]
        f.write(str(suma))
        f.write("  ")
        return suma
    else:
        n = len(listaNotas)
        lista1 = listaNotas[0:int(n / 2)]
        lista2 = listaNotas[int(n / 2):n]
        sumaTotal = divideYVenceras2(lista1) + divideYVenceras2(lista2)
        return sumaTotal


archivo = open("ejemplo_dyv.txt").read()
notasAsignaturas = []
lineasArchivo = archivo.split('\n')
for linea in lineasArchivo:
    notasAsignaturas.append(int(linea))
f = open("resultado_dyv.txt", "w")
f.write("")
f.close()
if esPotenciaDos(len(notasAsignaturas)):
    f = f = open("resultado_dyv.txt", "a")
    w = divideYVenceras(notasAsignaturas)
    f.write("--> Resultado = ")
    f.write(str(w))
else:
    f = open("resultado_dyv.txt", "a")
    l = len(notasAsignaturas)
    w = divideYVenceras2(notasAsignaturas)
    f.write(str(w))
    f.write("/")
    f.write(str(l))
    f.write("--> Resultado = ")
    f.write(str(w/l))
