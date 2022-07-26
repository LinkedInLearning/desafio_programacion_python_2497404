def encontrar_duplicados(lista):

    elementos_lista = []
    duplicados = []

    for elemento in lista:

        if elemento in elementos_lista:
            duplicados.append(elemento)
        else:
            elementos_lista.append(elemento)

    return duplicados


print(encontrar_duplicados(["ana", "paco", "paco", "emilio", "javier", "ana"])) # ["paco", "ana"]
