def ordenamiento_burbuja(lista):

    for i in range(len(lista)):

        for j in range(0, len(lista) - i - 1):

            if lista[j] > lista[j+1]:
                temporal = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temporal

    return lista

print(ordenamiento_burbuja([3,8,4,1,2])) # [1, 2, 3, 4, 8]
