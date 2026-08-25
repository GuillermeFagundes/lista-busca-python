idades = [12, 14, 16, 18, 21, 25, 30, 35, 42, 50]


def buscar_idade(lista, idade):
    inicio, fim, descartados = 0, len(lista) - 1, 0
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == idade:
            return meio, descartados
        if lista[meio] < idade:
            descartados += meio - inicio + 1
            inicio = meio + 1
        else:
            descartados += fim - meio + 1
            fim = meio - 1
    return -1, descartados


if __name__ == "__main__":
    procurada = int(input("Digite a idade: "))
    indice, descartados = buscar_idade(idades, procurada)
    print(f"Índice: {indice}; elementos descartados: {descartados}.")
