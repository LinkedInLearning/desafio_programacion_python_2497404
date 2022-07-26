def es_anagrama(palabra_1, palabra_2):

    letras_palabra_1 = sorted(palabra_1.lower())
    letras_palabra_2 = sorted(palabra_2.lower())

    return letras_palabra_1 == letras_palabra_2


print(es_anagrama("lama", "Mala"))   # True
print(es_anagrama("calor", "coral")) # True
print(es_anagrama("cama", "casa"))   # False
