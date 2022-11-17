#confesso que tentei fazer algo parecido com a 4 com uma ajuda do stackoverflow, so q n deu muito certo
#entao peço que corriga de maneira mais atenciosa e com mais carinho às outras questões <3 com amor andré <3


matriz = []

def cria_matriz(num_linhas, num_colunas):

    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = int(input("Digite o elemento [" + str(i) + "][" + str(j) + "]"))
            linha.append(valor)

        matriz.append(linha)
    return matriz


def le_matriz():
    lin = int(input("Digite o número de linhas da matriz: "))
    col = int(input("Digite o número de colunas da matriz: "))
    return cria_matriz(lin, col)

m = le_matriz()

def imprime_matriz(matriz):

    linhas = len(matriz)
    colunas = len(matriz[0])

    for i in range(linhas):
        for j in range(colunas):
            if(j == colunas - 1):
                print("%d" %matriz[i][j])
            else:
                print("%d" %matriz[i][j], end = " ")
    print(matriz)


imprime_matriz(matriz)
