nomes = ["Ana", "Bruno", "Carla", "Diego", "Elisa"]


def localizar_nome(lista, nome):
    for indice, item in enumerate(lista):
        if item.casefold() == nome.casefold():
            return indice
    return -1


if __name__ == "__main__":
    procurado = input("Digite um nome: ").strip()
    indice = localizar_nome(nomes, procurado)
    print(f"Nome encontrado na posição {indice + 1}." if indice >= 0 else "Nome não encontrado.")
