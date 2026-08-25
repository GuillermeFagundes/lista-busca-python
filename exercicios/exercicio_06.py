numeros = [17, 3, 42, 9, 28, 35, 6]


def maior_valor(lista):
    if not lista:
        raise ValueError("A lista não pode estar vazia.")
    maior = lista[0]
    for numero in lista[1:]:
        if numero > maior:
            maior = numero
    return maior


if __name__ == "__main__":
    print("Maior valor:", maior_valor(numeros))
