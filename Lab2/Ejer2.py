import numpy as np

ficheros = np.random.randint(1,21,6)
peticiones = np.random.randint(1,11,6)
listaArchivos = ""


class Archivo:
    def __init__(self, l, a):
        self.longitud = l
        self.accesos = a
        self.longitudporaccesos = l/a


listaArchivos = []
def crearArray(listaArchivos):
    for i in range(len(ficheros)-1):
        listaArchivos.append(Archivo(ficheros[i], peticiones[i]))
        print(listaArchivos[i].longitud, listaArchivos[i].accesos, listaArchivos[i].longitudporaccesos)
    print()
    return listaArchivos


def bubbleSort(listaArchivos):
    for lon in range(len(listaArchivos)-1, 0, -1):
        for i in range(lon):
            if listaArchivos[i].longitudporaccesos>listaArchivos[i+1].longitudporaccesos:
                temp = listaArchivos[i]
                listaArchivos[i] = listaArchivos[i+1]
                listaArchivos[i+1] = temp


bubbleSort(crearArray(listaArchivos))
for i in range (len(listaArchivos)):
    print(listaArchivos[i].longitud, listaArchivos[i].accesos, listaArchivos[i].longitudporaccesos)






