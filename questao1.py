lista = int(input("digite um tamanho para a lista: "))
lista1 = []

def createlista(lista):
    for i in range(lista):
        lista1.append(0)

for i in range(lista):
    valor = int(input("digite numeros inteiros: "))
    lista1.append(valor)


print(lista1)
print(sorted(lista1))
print(sum(lista1))
print(max(lista1))
