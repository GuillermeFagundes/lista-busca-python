def primeira_ocorrencia(lista, valor):
    inicio, fim, resposta = 0, len(lista) - 1, -1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == valor:
            resposta = meio
            fim = meio - 1
        elif lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    return resposta


if __name__ == "__main__":
    valores = [1, 3, 3, 3, 5, 8, 8]
    procurado = int(input("Digite o valor: "))
    print("Índice da primeira ocorrência:", primeira_ocorrencia(valores, procurado))
