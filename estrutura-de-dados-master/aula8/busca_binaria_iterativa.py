def busca_binaria(seq, procurado):
    """
    Deve retornar o índice onde o elemento deveriar ser inserido em lista ordenada
    :param procurado: elemento a ser procurado
    :param seq: sequencia a ser pesquisada
    :return: int
    """
    # Memória: O de 1
    #Tempo: O log n
    if len(seq) == 0: return 0
    inicio = 0
    final = len(seq)
    meio = 0
    while inicio < final:
        meio = ((inicio+final)//2)
        if seq[meio] < procurado: inicio += 1
        else: final -= 1
    if procurado > seq[meio]: return meio + 1
    return meio

import unittest


class BuscaBinariaTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertEqual(0, busca_binaria([], 1))
        self.assertEqual(0, busca_binaria([], 2))
        self.assertEqual(0, busca_binaria([], 3))

    def teste_lista_unitaria(self):
        self.assertEqual(0, busca_binaria([1], 0))
        self.assertEqual(0, busca_binaria([1], 1))
        self.assertEqual(1, busca_binaria([1], 2))
        self.assertEqual(1, busca_binaria([1], 3))
        self.assertEqual(1, busca_binaria([1], 4))

    def teste_lista_nao_unitaria(self):
        lista = list(range(10))
        self.assertEqual(0, busca_binaria(lista, -2))
        self.assertEqual(0, busca_binaria(lista, -1))
        for i in lista:
            self.assertEqual(i, busca_binaria(lista, i))
        self.assertEqual(10, busca_binaria(lista, 10))
        self.assertEqual(10, busca_binaria(lista, 11))
        self.assertEqual(10, busca_binaria(lista, 12))

    def teste_lista_elementos_repetidos(self):
        lista = [1, 1, 1, 2, 2, 2]
        self.assertEqual(0, busca_binaria(lista, 1))
        self.assertEqual(3, busca_binaria(lista, 2))