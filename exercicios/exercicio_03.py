def busca_sequencial(lista, valor):
    for indice, item in enumerate(lista):
        if item == valor:
            return indice
    return -1


if __name__ == "__main__":
    valores = [12, 4, 8, 19, 7]
    procurado = int(input("Digite o valor procurado: "))
    print("Índice:", busca_sequencial(valores, procurado))
