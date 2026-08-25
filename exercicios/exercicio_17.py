codigos = [1001, 1007, 1015, 1022, 1030, 1048, 1055]


def codigo_cadastrado(lista, codigo):
    inicio, fim = 0, len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == codigo:
            return True
        if lista[meio] < codigo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return False


if __name__ == "__main__":
    procurado = int(input("Digite o código: "))
    print("Código cadastrado." if codigo_cadastrado(codigos, procurado) else "Código não cadastrado.")
