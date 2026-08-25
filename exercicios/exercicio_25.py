codigos_livros = [101, 115, 132, 148, 160, 177, 190, 205]


def localizar_livro(lista, codigo):
    inicio, fim = 0, len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == codigo:
            return meio
        if lista[meio] < codigo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1


if __name__ == "__main__":
    procurado = int(input("Digite o código do livro: "))
    indice = localizar_livro(codigos_livros, procurado)
    print(f"Livro disponível na posição {indice + 1}." if indice >= 0 else "Livro indisponível.")
