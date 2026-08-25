matriculas = [2024050, 2024012, 2024091, 2024033, 2024074]


def busca_sequencial(lista, valor):
    for indice, item in enumerate(lista):
        if item == valor:
            return indice
    return -1


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
    procurada = int(input("Digite a matrícula: "))
    opcao = input("Escolha S (sequencial) ou B (binária): ").strip().upper()
    if opcao == "S":
        indice = busca_sequencial(matriculas, procurada)
    elif opcao == "B":
        lista_ordenada = sorted(matriculas)
        indice = busca_binaria(lista_ordenada, procurada)
        matriculas = lista_ordenada
    else:
        raise SystemExit("Opção inválida.")
    print(f"Encontrada na posição {indice + 1}." if indice >= 0 else "Matrícula não encontrada.")
