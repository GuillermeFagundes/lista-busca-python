import unittest

from algoritmos import (
    busca_binaria,
    busca_binaria_com_comparacoes,
    busca_sequencial,
    busca_sequencial_com_comparacoes,
    primeira_ocorrencia,
    ultima_ocorrencia,
)
from exercicios.exercicio_06 import maior_valor
from exercicios.exercicio_07 import todas_as_posicoes
from exercicios.exercicio_10 import palavra_mais_longa
from exercicios.exercicio_24 import buscar_idade
from exercicios.exercicio_26 import busca_binaria as busca_binaria_produto
from exercicios.exercicio_26 import busca_sequencial as busca_sequencial_produto


class TestesBusca(unittest.TestCase):
    def test_busca_sequencial_encontra_e_falha(self):
        self.assertEqual(busca_sequencial([8, 3, 5], 3), 1)
        self.assertEqual(busca_sequencial([8, 3, 5], 9), -1)

    def test_busca_sequencial_conta_comparacoes(self):
        self.assertEqual(busca_sequencial_com_comparacoes([2, 4, 6], 6), (2, 3))
        self.assertEqual(busca_sequencial_com_comparacoes([2, 4, 6], 7), (-1, 3))

    def test_busca_binaria_encontra_extremos_e_falha(self):
        lista = [1, 4, 7, 10, 13]
        self.assertEqual(busca_binaria(lista, 1), 0)
        self.assertEqual(busca_binaria(lista, 13), 4)
        self.assertEqual(busca_binaria(lista, 8), -1)

    def test_busca_binaria_conta_comparacoes(self):
        indice, comparacoes = busca_binaria_com_comparacoes(list(range(1, 1001)), 1000)
        self.assertEqual(indice, 999)
        self.assertLessEqual(comparacoes, 10)

    def test_primeira_e_ultima_ocorrencias(self):
        lista = [1, 3, 3, 3, 5]
        self.assertEqual(primeira_ocorrencia(lista, 3), 1)
        self.assertEqual(ultima_ocorrencia(lista, 3), 3)
        self.assertEqual(primeira_ocorrencia(lista, 2), -1)

    def test_solucoes_sequenciais_aplicadas(self):
        self.assertEqual(maior_valor([-5, -1, -9]), -1)
        self.assertEqual(todas_as_posicoes([4, 1, 4, 4], 4), [0, 2, 3])
        self.assertEqual(palavra_mais_longa(["a", "abcd", "xy"]), "abcd")

    def test_elementos_descartados(self):
        indice, descartados = buscar_idade([10, 20, 30, 40, 50], 40)
        self.assertEqual(indice, 3)
        self.assertEqual(descartados, 3)

    def test_estoque_duas_buscas(self):
        produtos = [(10, "A"), (20, "B"), (30, "C"), (40, "D")]
        self.assertEqual(busca_sequencial_produto(produtos, 30)[0], 2)
        self.assertEqual(busca_binaria_produto(produtos, 30)[0], 2)


if __name__ == "__main__":
    unittest.main()
