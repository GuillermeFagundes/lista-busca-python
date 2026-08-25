contatos = [
    ("Alice", "(11) 90000-1001"),
    ("Bruno", "(11) 90000-1002"),
    ("Carla", "(11) 90000-1003"),
    ("Diego", "(11) 90000-1004"),
    ("Elisa", "(11) 90000-1005"),
]


def buscar_contato(lista, nome):
    inicio, fim = 0, len(lista) - 1
    procurado = nome.casefold()
    while inicio <= fim:
        meio = (inicio + fim) // 2
        atual = lista[meio][0].casefold()
        if atual == procurado:
            return meio
        if atual < procurado:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1


if __name__ == "__main__":
    procurado = input("Digite o nome: ").strip()
    indice = buscar_contato(contatos, procurado)
    if indice >= 0:
        print(f"{contatos[indice][0]}: {contatos[indice][1]}")
    else:
        print("Contato não encontrado.")
