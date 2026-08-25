produtos = [(100, "Teclado"), (205, "Mouse"), (310, "Monitor"), (450, "Impressora"), (520, "Webcam")]


def busca_sequencial(lista, codigo):
    comparacoes = 0
    for indice, produto in enumerate(lista):
        comparacoes += 1
        if produto[0] == codigo:
            return indice, comparacoes
    return -1, comparacoes


def busca_binaria(lista, codigo):
    inicio, fim, comparacoes = 0, len(lista) - 1, 0
    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1
        if lista[meio][0] == codigo:
            return meio, comparacoes
        if lista[meio][0] < codigo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1, comparacoes


if __name__ == "__main__":
    procurado = int(input("Digite o código do produto: "))
    indice_seq, comp_seq = busca_sequencial(produtos, procurado)
    indice_bin, comp_bin = busca_binaria(produtos, procurado)
    nome = produtos[indice_seq][1] if indice_seq >= 0 else "não encontrado"
    print(f"Produto: {nome}")
    print(f"Sequencial: índice {indice_seq}, {comp_seq} comparação(ões).")
    print(f"Binária: índice {indice_bin}, {comp_bin} comparação(ões).")
