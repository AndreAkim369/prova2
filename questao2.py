import random

dado = [1, 2, 3, 4, 5, 6]

op = 0

jogador1 = []
jogador2 = []

dadojogado = 1

def jogo():
    print("1- jogar")
    print("2- sair")
    op = int(input("escolha uma opcao: "))
    if op == 1:
        jogar()
    if op == 2:
        sair()

def jogar():
    global dadojogado
    jogada = random.choice(dado)
    if jogada / 2 != 0:
        jogador1.append(jogada)
        dadojogado += 1
    if jogada / 2 == 0:
        jogador2.append(jogada)
        dadojogado += 1   
    return jogo()     

def sair():
    print("RESULTADOS:")
    print("jogadas do jogador 1: ", jogador1)
    print("jogadas do jogador 2: ", jogador2)
    print("soma dos valores do jogador 1: ", sum(jogador1))
    print("soma dos valores do jogador 2: ", sum(jogador2))
    if jogador1 > jogador2:
        print("jogador 1 venceu")
    else:
        print("jogador 2 venceu") 

jogo()

   
        
