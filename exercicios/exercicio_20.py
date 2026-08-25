pares = list(range(2, 201, 2))


def busca_binaria(lista, valor):
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
    procurado = int(input("Digite um número: "))
    indice = busca_binaria(pares, procurado)
    print(f"Encontrado na posição {indice + 1}." if indice >= 0 else "Número não encontrado.")
