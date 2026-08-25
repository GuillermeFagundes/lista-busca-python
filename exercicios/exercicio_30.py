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


def executar_menu():
    valores = []
    ordenada = True
    while True:
        print("\n1-Cadastrar  2-Exibir  3-Ordenar  4-Busca sequencial  5-Busca binária  0-Sair")
        opcao = input("Opção: ").strip()
        if opcao == "0":
            break
        if opcao == "1":
            valores.append(int(input("Valor: ")))
            ordenada = ordenada and (len(valores) < 2 or valores[-2] <= valores[-1])
        elif opcao == "2":
            print("Lista:", valores)
        elif opcao == "3":
            valores.sort()
            ordenada = True
            print("Lista ordenada.")
        elif opcao in ("4", "5"):
            procurado = int(input("Valor procurado: "))
            if opcao == "4":
                indice = busca_sequencial(valores, procurado)
            elif not ordenada:
                print("Ordene a lista antes da busca binária.")
                continue
            else:
                indice = busca_binaria(valores, procurado)
            print(f"Encontrado no índice {indice}." if indice >= 0 else "Valor não encontrado.")
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    executar_menu()
