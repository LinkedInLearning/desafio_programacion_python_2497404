def aplanar_lista(lista):

    nueva_lista = []

    for elemento in lista:

        if type(elemento) is list:
            nueva_lista.extend(elemento)
        else:
            nueva_lista.append(elemento)

    return nueva_lista


print(aplanar_lista([2, 3, 4, [3, 2]])) # [2, 3, 4, 3, 2]
print(aplanar_lista([2, 3, 4, [[2]]])) # [2, 3, 4. [2]]
