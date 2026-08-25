produtos = ["Arroz", "Feijão", "Leite", "Café", "Açúcar"]
precos = [24.90, 8.50, 5.80, 17.40, 4.60]


def localizar_produto(lista, nome):
    for indice, produto in enumerate(lista):
        if produto.casefold() == nome.casefold():
            return indice
    return -1


if __name__ == "__main__":
    procurado = input("Digite o produto: ").strip()
    indice = localizar_produto(produtos, procurado)
    print(f"Preço: R$ {precos[indice]:.2f}" if indice >= 0 else "Produto não encontrado.")
