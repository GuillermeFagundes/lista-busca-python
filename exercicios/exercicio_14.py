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
    numeros = [1, 4, 7, 10, 13, 16, 19]
    procurado = int(input("Digite o valor: "))
    print("Índice:", busca_binaria(numeros, procurado))
