numeros = list(range(5, 105, 5))


def busca_binaria_detalhada(lista, valor):
    inicio, fim = 0, len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        print(f"inicio={inicio}, fim={fim}, meio={meio}")
        if lista[meio] == valor:
            return meio
        if lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1


if __name__ == "__main__":
    procurado = int(input("Digite um número: "))
    indice = busca_binaria_detalhada(numeros, procurado)
    print(f"Encontrado no índice {indice}." if indice >= 0 else "Não encontrado.")
