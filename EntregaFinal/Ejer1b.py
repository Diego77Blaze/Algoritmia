def ejer1(listaUsuarios):
    grupos = []
    for key in listaUsuarios:
        unidadGrupo = [key]
        for i in range(len(listaUsuarios[key])):
            unidadGrupo.append(listaUsuarios[key][i])
        grupos.append(unidadGrupo)
    resFinal = []
    while len(grupos) > 0:
        primerElem = grupos[0]
        restoGrupos = grupos[1:]
        primerElem = set(primerElem)
        numElemsPrimero = -1
        while len(primerElem) > numElemsPrimero:
            numElemsPrimero = len(primerElem)
            restoGrupos2 = []
            for grupo in restoGrupos:
                if len(primerElem.intersection(set(grupo))) != 0: #hay elementos en común
                    primerElem.update(grupo) #return set s with elements added from t
                else:
                    restoGrupos2.append(grupo)
            restoGrupos = restoGrupos2
        resFinal.append(primerElem)
        grupos = restoGrupos
    gradoConexion = len(resFinal)/len(listaUsuarios)
    return gradoConexion


usuarios = {'Carlos': ['Antonio', 'Emma'], 'Emma': ['Bea'], 'Antonio': ['Bea', 'Carlos', 'Emma'],
            'Bea': ['Emma', 'Carlos', 'Antonio'], 'David': ['Fernando'], 'Fernando': []}

print(ejer1(usuarios))