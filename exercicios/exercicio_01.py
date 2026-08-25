numeros = [7, 14, 3, 22, 9, 18, 5, 30, 11, 2]


def existe(lista, valor):
    for item in lista:
        if item == valor:
            return True
    return False


if __name__ == "__main__":
    procurado = int(input("Digite um número: "))
    print("O número está na lista." if existe(numeros, procurado) else "O número não está na lista.")
