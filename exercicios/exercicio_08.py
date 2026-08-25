def numero_existe(lista, numero):
    for item in lista:
        if item == numero:
            return True
    return False


if __name__ == "__main__":
    valores = [5, 10, 15, 20, 25]
    procurado = int(input("Digite um número: "))
    print(numero_existe(valores, procurado))
