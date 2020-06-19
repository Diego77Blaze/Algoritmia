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
                if len(primerElem.intersection(set(grupo))) != 0:
                    primerElem.update(grupo)
                else:
                    restoGrupos2.append(grupo)
            restoGrupos = restoGrupos2
        resFinal.append(primerElem)
        grupos = restoGrupos
    file.write("Numero de grupos: ")
    file.write(str(len(resFinal)))
    file.write("\n")
    file.write("Los grupos de usuarios son: \n\n")
    for i in range(len(resFinal)):
        file.write("- Grupo ")
        file.write(str(i+1))
        file.write(": ")
        file.write(str(resFinal[i]))
        file.write("\n")
    file.write("\n")



    gradoConexion = len(resFinal)/len(listaUsuarios)
    return gradoConexion

archivo = open("ejemplo_voraz.txt").read()
usuarios = {}
lineasArchivo = archivo.split('\n')
for linea in lineasArchivo:
    separacion = linea.split(":")
    key = separacion[0]
    value = []
    for elem in separacion[1].split(","):
        if(elem)!='':
            value.append(elem)
    usuarios[key] = value

f = open("resultado_voraz.txt", "w")
f.write("")
f.close()
file = open("resultado_voraz.txt", "a")
w = ejer1(usuarios)
file.write("Y, por tanto, este es el grado de conexión: ")
file.write(str(w))