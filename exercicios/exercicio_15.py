nomes = ["Alice", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda"]


def busca_binaria_nome(lista, nome):
    inicio, fim = 0, len(lista) - 1
    procurado = nome.casefold()
    while inicio <= fim:
        meio = (inicio + fim) // 2
        atual = lista[meio].casefold()
        if atual == procurado:
            return meio
        if atual < procurado:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1


if __name__ == "__main__":
    procurado = input("Digite um nome: ").strip()
    indice = busca_binaria_nome(nomes, procurado)
    print("Nome presente." if indice >= 0 else "Nome não encontrado.")
