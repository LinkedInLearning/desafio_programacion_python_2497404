def parentesis_balanceados(texto):

    apertura = 0

    for parentesis in texto:
        if parentesis == "(":
            apertura += 1
        elif parentesis == ")":
            apertura -= 1

            if apertura < 0:
                return False

    return apertura == 0


print(parentesis_balanceados("((()))()"))
print(parentesis_balanceados(")(()"))
print(parentesis_balanceados("(()"))
