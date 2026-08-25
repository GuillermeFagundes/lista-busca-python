def busca_sequencial(lista, valor):
    comparacoes = 0
    for indice, item in enumerate(lista):
        comparacoes += 1
        if item == valor:
            return indice, comparacoes
    return -1, comparacoes


def busca_binaria(lista, valor):
    inicio, fim, comparacoes = 0, len(lista) - 1, 0
    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1
        if lista[meio] == valor:
            return meio, comparacoes
        if lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1, comparacoes


if __name__ == "__main__":
    numeros = list(range(1, 1001))
    procurado = numeros[-1]
    _, comparacoes_seq = busca_sequencial(numeros, procurado)
    _, comparacoes_bin = busca_binaria(numeros, procurado)
    print(f"Busca sequencial: {comparacoes_seq} comparações.")
    print(f"Busca binária: {comparacoes_bin} comparações.")
    print("Conclusão: em uma lista grande e ordenada, a busca binária exige muito menos comparações.")
