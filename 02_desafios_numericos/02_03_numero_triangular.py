def numero_triangular(row):

    triangular = 0
    for i in range(1, row + 1):
        triangular += i

    return triangular


print(numero_triangular(2)) # 3
print(numero_triangular(4)) # 10
print(numero_triangular(6)) # 21
