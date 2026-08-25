"""Algoritmos de busca implementados manualmente."""


def busca_sequencial(lista, valor):
    for indice, item in enumerate(lista):
        if item == valor:
            return indice
    return -1


def busca_sequencial_com_comparacoes(lista, valor):
    comparacoes = 0
    for indice, item in enumerate(lista):
        comparacoes += 1
        if item == valor:
            return indice, comparacoes
    return -1, comparacoes


def busca_binaria(lista, valor):
    inicio, fim = 0, len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == valor:
            return meio
        if lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1


def busca_binaria_com_comparacoes(lista, valor):
    inicio, fim, comparacoes = 0, len(lista) - 1, 0
    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1
        if lista[meio] == valor:
            return meio, comparacoes
        if lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1, comparacoes


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


def ultima_ocorrencia(lista, valor):
    inicio, fim, resposta = 0, len(lista) - 1, -1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == valor:
            resposta = meio
            inicio = meio + 1
        elif lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    return resposta
