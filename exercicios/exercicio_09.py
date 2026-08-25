matriculas = [2024101, 2024107, 2024112, 2024120, 2024135]


def aluno_cadastrado(lista, matricula):
    for item in lista:
        if item == matricula:
            return True
    return False


if __name__ == "__main__":
    procurada = int(input("Digite a matrícula: "))
    print("Aluno cadastrado." if aluno_cadastrado(matriculas, procurada) else "Matrícula não cadastrada.")
