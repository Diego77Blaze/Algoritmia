def cambiarCaracter(car1, car2, listaCadena, pos):
    char = car1+car2
    M = {
        "aa": "b",
        "ab": "b",
        "ac": "a",
        "ad": "d",
        "ba": "c",
        "bb": "a",
        "bc": "d",
        "bd": "a",
        "ca": "b",
        "cb": "a",
        "cc": "c",
        "cd": "c",
        "da": "d",
        "db": "c",
        "dc": "d",
        "dd": "b"
    }
    posibLista = listaCadena.copy()
    posibLista[pos] = M.get(char)
    print("Reemplazados", car1,car2, "->", posibLista[pos])
    posibLista.pop(pos+1)
    return posibLista

def backtrackingCadena(cad, letraRes):
    print(cad)
    if(len(cad)==0):
        print("La lista está vacía, inserte una lista no vacía para comprobar la funcionalidad del programa.")
    elif(len(cad)==1):
        if cad[0] == letraRes:
            print("Encontrada: ", cad[0])
    else:
        for i in range(len(cad)-1):
            posibleCad = cambiarCaracter(cad[i], cad[i+1],cad, i)
            backtrackingCadena(posibleCad, letraRes)

cadena = "acabada"
caracter = 'd'
lista = list(cadena)
backtrackingCadena(lista, caracter)
