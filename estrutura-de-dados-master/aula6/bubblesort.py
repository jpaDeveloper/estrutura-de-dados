import unittest
#Tempo: O de n^2
#Memoria: Ode 1


def bubble_sort(seq):
    for x in range(len(seq) -1, 0, -1):
        for i in range(x):
            if seq[i] > seq[i + 1]:
                atul = seq[i]
                seq[i] = seq[i + 1]
                seq[i + 1] = atul
    return seq


class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], bubble_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], bubble_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], bubble_sort([2, 1]))

    def teste_lista_binaria(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], bubble_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()