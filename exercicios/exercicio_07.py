import random


def todas_as_posicoes(lista, valor):
    posicoes = []
    for indice, item in enumerate(lista):
        if item == valor:
            posicoes.append(indice)
    return posicoes


if __name__ == "__main__":
    numeros = [random.randint(1, 10) for _ in range(20)]
    print("Lista:", numeros)
    procurado = int(input("Digite um valor entre 1 e 10: "))
    posicoes = todas_as_posicoes(numeros, procurado)
    if posicoes:
        print("Posições (começando em 1):", [indice + 1 for indice in posicoes])
    else:
        print("Valor não encontrado.")
