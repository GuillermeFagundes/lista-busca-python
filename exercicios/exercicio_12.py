valores = [10, 35, 8, 21, 4, 50]


def busca_com_parada(lista, valor):
    comparacoes = 0
    for indice, item in enumerate(lista):
        comparacoes += 1
        if item == valor:
            return indice, comparacoes
    return -1, comparacoes


if __name__ == "__main__":
    procurado = int(input("Digite o valor procurado: "))
    indice, comparacoes = busca_com_parada(valores, procurado)
    if indice >= 0:
        print(f"Valor {procurado} encontrado na posição {indice + 1}; comparações: {comparacoes}.")
    else:
        print(f"Valor não encontrado após {comparacoes} comparações.")
