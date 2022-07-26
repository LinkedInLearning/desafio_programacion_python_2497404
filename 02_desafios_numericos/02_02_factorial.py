def calcular_factorial(numero):

    factorial = 1
    for i in range(1, numero+1):
        factorial = factorial * i

    return factorial


print(calcular_factorial(0)) # 1
print(calcular_factorial(3)) # 6
print(calcular_factorial(4)) # 24
print(calcular_factorial(5)) # 120


def calcular_factorial_recursivo(numero):

    if numero == 0 or numero == 1:
        return 1

    return numero * calcular_factorial_recursivo(numero-1)


print(calcular_factorial_recursivo(0)) # 1
print(calcular_factorial_recursivo(3)) # 6
print(calcular_factorial_recursivo(4)) # 24
print(calcular_factorial_recursivo(5)) # 120
