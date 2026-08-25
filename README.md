# Lista de exercícios - Algoritmos de busca em Python

Soluções dos 30 exercícios sobre busca sequencial e busca binária. Os algoritmos de busca foram implementados manualmente, sem `list.index()` e sem usar operadores de pertencimento para realizar as buscas.

## Organização

- `exercicios/`: um programa independente para cada questão;
- `algoritmos.py`: funções reutilizáveis de busca implementadas manualmente;
- `testes/`: testes automatizados das funções centrais.

## Como executar

É necessário Python 3.10 ou superior. Na raiz do projeto, execute, por exemplo:

```bash
python exercicios/exercicio_01.py
python exercicios/exercicio_30.py
```

Para rodar os testes:

```bash
python -m unittest discover -s testes -v
```

Observação: as posições mostradas ao usuário começam em 1. Os índices retornados pelas funções começam em 0, seguindo a convenção do Python.

