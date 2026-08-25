palavras = ["casa", "computador", "sol", "programação", "livro"]


def palavra_mais_longa(lista):
    if not lista:
        raise ValueError("A lista não pode estar vazia.")
    maior = lista[0]
    for palavra in lista[1:]:
        if len(palavra) > len(maior):
            maior = palavra
    return maior


if __name__ == "__main__":
    print("Palavra com mais caracteres:", palavra_mais_longa(palavras))
