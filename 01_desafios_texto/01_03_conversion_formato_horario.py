def convertir_horario(hora):

    hora_lista = hora.split(":")
    if hora[-2:].lower() == "pm":
        if hora_lista[0] != "12":
            hora_lista[0] = str(int(hora_lista[0]) + 12)
    else:
        if hora_lista[0] == "12":
            hora_lista[0] = "00"

    hora_convertida = ":".join(hora_lista)

    return hora_convertida[:-2]

print(convertir_horario("12:40AM")) # 00:40
print(convertir_horario("04:59pm")) # 16:59
print(convertir_horario("10:00:00PM")) # 22:00
