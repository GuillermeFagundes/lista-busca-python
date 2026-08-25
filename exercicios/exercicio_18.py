def busca_binaria_com_comparacoes(lista, valor):
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
    numeros = [3, 6, 9, 12, 15, 18, 21, 24]
    procurado = int(input("Digite o valor: "))
    indice, comparacoes = busca_binaria_com_comparacoes(numeros, procurado)
    print(f"Índice: {indice}; comparações: {comparacoes}.")
