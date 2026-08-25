def existe_busca_binaria(lista, valor):
    inicio, fim = 0, len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == valor:
            return True
        if lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    return False


if __name__ == "__main__":
    valores = [2, 8, 14, 20, 26, 32]
    procurado = int(input("Digite o valor: "))
    print(existe_busca_binaria(valores, procurado))
