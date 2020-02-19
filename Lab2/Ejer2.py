import numpy as np

ficheros = np.random.randint(1,21,6)
peticiones = np.random.randint(1,11,6)
listaArchivos = ""


class Archivo:
    def __init__(self, l, a):
        self.longitud = l
        self.accesos = a


listaArchivos = []

def ordenarArchivos(listaArchivos):
    for i in range(6):
        listaArchivos.append(Archivo(ficheros[i], peticiones[i]))




