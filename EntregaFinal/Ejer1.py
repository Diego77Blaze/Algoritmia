def ejer1(listaUsuarios):
    grupos = []
    firstTime = True
    for key in listaUsuarios:
        unidadGrupo = []
        if firstTime == True:
            grupos.append(unidadGrupo)

        for i in range(len(grupos)):
            firstTime = False
            if key in grupos[i]:#si la llave ya está en los grupos
                for k in range(len(listaUsuarios[key])):
                    if listaUsuarios[key][k] not in grupos[i]:
                        unidadGrupo.append(listaUsuarios[key][k])
            else:#si la llave no está en los grupos
                for k in range(len(listaUsuarios[key])):
                    if listaUsuarios[key][k] not in grupos[i]:#pero si tiene que uno de sus valores si está, lo mete
                        unidadGrupo.append(key)
                        unidadGrupo.append(listaUsuarios[key][k])
                    else: #si no, lo mete a un nuevo grupo
                        unidadGrupo.append(key)
                        for j in range(len(listaUsuarios[key])):
                            unidadGrupo.append(listaUsuarios[key][j])
                    grupos.append(unidadGrupo)


    gradoConexion = len(grupos) / len(listaUsuarios)
    return gradoConexion


usuarios = {'Antonio': ['Bea', 'Carlos', 'Emma'], 'Carlos': ['Antonio', 'Emma'], 'Emma': ['Bea'],
            'Bea': ['Emma', 'Carlos', 'Antonio'], 'David': ['Fernando'], 'Fernando': []}
print(ejer1(usuarios))

