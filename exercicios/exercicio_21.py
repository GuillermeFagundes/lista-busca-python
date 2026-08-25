valores = [2, 4, 4, 4, 7, 9, 9, 12]


def localizar_ocorrencia(lista, valor):
    inicio, fim = 0, len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == valor:
            return meio
        if lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1


if __name__ == "__main__":
    procurado = int(input("Digite o valor: "))
    indice = localizar_ocorrencia(valores, procurado)
    print(f"Ocorrência encontrada no índice {indice}." if indice >= 0 else "Valor não encontrado.")
