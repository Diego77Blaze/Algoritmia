def dijkstra(grafo, nodoInicial, nodoMeta):
    nodosRuta = []
    nodosNoVistos = grafo
    distanciaMasCorta = {}
    predecesor = {}
    for nodo in nodosNoVistos:
        distanciaMasCorta[nodo] = 1000000
    distanciaMasCorta[nodoInicial] = 0
    while nodosNoVistos:
        nodoMinimo = None
        for nodo in nodosNoVistos:
            if nodoMinimo is None:
                nodoMinimo = nodo
            elif distanciaMasCorta[nodo] < distanciaMasCorta[nodoMinimo]:
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
        except:
            break
    nodosRuta.insert(0, nodoInicial)
    if distanciaMasCorta[nodoMeta] == 1000000:
        print('No existe ruta posible')
    else:
        print('El coste de la ruta más corta es ' + str(distanciaMasCorta[nodoMeta]))
        print("La ruta más corta de ", nodoInicial, " a ", nodoMeta, " es: ", str(nodosRuta))

grafo = {'A': {'B': 5, 'C': 2}, 'B': {'D': 4, 'E': 2}, 'C': {'B': 8, 'E': 7}, 'D': {'E': 6, 'F': 3}, 'E': {'F': 1},'F': {}}


print("Introduzca el nodo inicial: ")
nodoInicial = input()
print("Introduzca el nodo meta: ")
nodoMeta = input()
if nodoInicial in grafo.keys() and nodoMeta in grafo.keys():
    dijkstra(grafo, nodoInicial, nodoMeta)
elif nodoInicial not in grafo.keys() and nodoMeta not in grafo.keys():
    print("No existe ni el nodo inicial ni el final en el grafo")
elif nodoInicial not in grafo.keys():
    print("El nodo inicial no existe en el grafo")
elif nodoMeta not in grafo.keys():
    print("El nodo final no existe en el grafo")