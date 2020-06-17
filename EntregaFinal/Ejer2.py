def divideYVenceras(listaNotas):
    if len(listaNotas) % 2 == 0:
        if len(listaNotas) / 2 == 1:
            media = (listaNotas[0] + listaNotas[1]) / 2
            return media
        else:
            n = len(listaNotas)
            lista1 = listaNotas[0:int(n / 2)]
            lista2 = listaNotas[int(n / 2):n]
            return (divideYVenceras(lista1) + divideYVenceras(lista2)) / 2

def divideYVenceras2(listaNotas):
    if len(listaNotas) == 1:
        return listaNotas[0]
    elif len(listaNotas) == 2:
        suma = listaNotas[0] + listaNotas[1]
        return suma
    else:
        n = len(listaNotas)
        lista1 = listaNotas[0:int(n / 2)]
        lista2 = listaNotas[int(n / 2):n]
        sumaTotal = divideYVenceras2(lista1) + divideYVenceras2(lista2)
        return sumaTotal


notasAsignaturasPar = [6, 3, 4, 1, 2, 3, 8, 10]
notasAsignaturasImpar = [6, 3, 4, 1, 2, 3, 8, 10, 1]
print("Media para n potencia de dos:", divideYVenceras(notasAsignaturasPar))
print("Media para n que no sea potencia de dos:", divideYVenceras2(notasAsignaturasImpar)/len(notasAsignaturasImpar))
