import unittest

#Tempo: O de n^2
#Memoria: O de 1

def insertion_sort(seq):
    for i in range(1, len(seq)):
        corrente = seq[i]
        atul = i
        while atul > 0 and seq[atul - 1] > corrente:
            seq[atul] = seq[atul - 1]
            atul = atul - 1
        seq[atul] = corrente
    return seq


class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], insertion_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], insertion_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], insertion_sort([2, 1]))

    def teste_lista_binaria(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], insertion_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()