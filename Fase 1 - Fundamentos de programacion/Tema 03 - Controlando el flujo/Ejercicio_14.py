
matriz = [
    [8,  7,  0],
    [34, 2, -1],
    [5, -5, 12]
]

for i, filas in enumerate(matriz):
    for j, columnas in enumerate(filas):
        if(matriz[i][j] % 2 == 0):
            matriz[i][j] = 0
        else:
            matriz[i][j] = 1
        print(matriz[i][j], end = " ")
    print()

