cpfs = ["111.111.111-11", "222.222.222-22", "333.333.333-33", "444.444.444-44"]


def buscar_cpf(lista, cpf):
    comparacoes = 0
    for indice, item in enumerate(lista):
        comparacoes += 1
        if item == cpf:
            return indice, comparacoes
    return -1, comparacoes


if __name__ == "__main__":
    procurado = input("Digite o CPF: ").strip()
    indice, comparacoes = buscar_cpf(cpfs, procurado)
    if indice >= 0:
        print(f"CPF cadastrado. Comparações: {comparacoes}.")
    else:
        print(f"CPF não cadastrado. Comparações: {comparacoes}.")
