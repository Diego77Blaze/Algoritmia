grafo = {'S':{'B': 5, 'C':2},'B':{'D':4, 'E': 2},'C':{'B':8,'E':7}, 'D':{'E':6,'F':3},'E':{'F':1}} #Creamos el grafo que usaremos de ejemplo


def dijkstra(grafo, nodoInicial, nodoMeta):
    distanciaMasCorta = {}
    predecesor = {}
    nodosNoVistos = grafo
    nodosRuta = []
    for nodo in nodosNoVistos:
        distanciaMasCorta[nodo] = 1000
    distanciaMasCorta[nodoInicial] = 0

    while nodosNoVistos:
        nodoMinimo = None
        for nodo in nodosNoVistos:
            if nodoMinimo is None:
                nodoMinimo = nodo
            elif distanciaMasCorta[nodo]<distanciaMasCorta[nodoMinimo]:
                nodoMinimo = nodo

        for conectado, peso in grafo[nodoMinimo].items():
            if peso + distanciaMasCorta[nodoMinimo] < distanciaMasCorta[conectado]:
                distanciaMasCorta[conectado] = peso + distanciaMasCorta[nodoMinimo]
                predecesor[conectado] = nodoMinimo
            nodosNoVistos.pop(nodoMinimo)

            nodoActual = nodoMeta
            while nodoActual != nodoInicial:
                try:
                    nodosRuta.insert(0, nodoActual)
                    nodoActual = predecesor[nodoActual]
                except KeyError:
                    print('Path not reachable')
                    break
            nodosRuta.insert(0, nodoInicial)
            if distanciaMasCorta[nodoMeta] != 1000:
                print('Shortest distance is ' + str(distanciaMasCorta[nodoMeta]))
                print('And the path is ' + str(nodosRuta))

        dijkstra(grafo, 'a', 'b')


