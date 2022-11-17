

matriz2 = [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
]

def imprime_matriz(matriz2):

    linhas = len(matriz2)
    colunas = len(matriz2[0])

    for i in range(linhas):
        for j in range(colunas):
            matriz2[i][j]
    for id in range(5):
        print(matriz2[id])
    print()

imprime_matriz(matriz2)