def primera_letra_repetida(texto):

    texto_minsucula = texto.lower()
    texto_sin_espacios = texto_minsucula.replace(" ", "")
    lista_letras = []
    for letra in texto_sin_espacios:
        if letra in lista_letras:
            return letra
        else:
            lista_letras.append(letra)

    return None



print(primera_letra_repetida("saltar"))  # a
print(primera_letra_repetida("me gusta"))   # None
