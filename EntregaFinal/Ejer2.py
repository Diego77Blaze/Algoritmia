def divideYVenceras(listaNotas):
    if len(listaNotas)/2 == 1:
        media = (listaNotas[0]+listaNotas[1])/2
        return media
    else:
        n = len(listaNotas)
        lista1 = listaNotas[0:int(n / 2)]
        lista2 = listaNotas[int(n / 2):n]
        return (divideYVenceras(lista1) + divideYVenceras(lista2))/2


#listaNotas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 1, 2, 10, 9]
listaNotas = [6,3,4,1,2,3,8,10]
print(divideYVenceras(listaNotas))
