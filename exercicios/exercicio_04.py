notas = [7.5, 8.0, 6.5, 8.0, 9.0, 8.0]


def contar_ocorrencias(lista, valor):
    quantidade = 0
    for item in lista:
        if item == valor:
            quantidade += 1
    return quantidade


if __name__ == "__main__":
    procurada = float(input("Digite uma nota: "))
    quantidade = contar_ocorrencias(notas, procurada)
    if quantidade:
        print(f"A nota aparece {quantidade} vez(es).")
    else:
        print("A nota não aparece na lista.")
