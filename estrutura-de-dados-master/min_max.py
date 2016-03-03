# A função min_max deverá rodar em O(n) e o código não pode usar nenhuma
# lib do Python (sort, min, max e etc)
# Não pode usar qualquer laço (while, for), a função deve ser recursiva
# Ou delegar a solução para uma função puramente recursiva
import unittest
import time

G = False
contN = None
M = None
m = None

def min_max(seq, contador = contN, maior = M, menor = m ):
    global G  #Variavel global para controle da estrutura de decisão
    '''
    :param seq: uma sequencia
    :return: (min, max)
    Retorna tupla cujo primeiro valor mínimo (min) é o valor
    mínimo da sequencia seq.
    O segundo é o valor máximo (max) da sequencia
    A função max_min é O(n) por causa que seu tempo de processamento esta diretamente ligado a sua entrada, pois o numero numero de elementos na lista que
    determina a quantidade de vezes que a resursão sera utilizada
    e também após uma analise feita com a função time acoplada em cada caso de teste, foi constatado o tempo aproximado consequentemente calculado suas diferenças.
    Tempo com lista 500 elementos  em mili segundos 0.0010001659393310547
    '''
    if G == True:
        max = maior
        min = menor
        if contador == len(seq):#Se a variavel contador for igual ao numero de elementos da lista
            G = False
            return min, max
        if max < seq[contador]:
            max = seq[contador]
        if min > seq[contador]:
            min = seq[contador]
        return min_max(seq, contador + 1, max, min)
    else:
        if len(seq) == 0:
            return None, None
        elif len(seq) == 1:
            return seq[0], seq[0]
        if len(seq) > 1:
            contN = 1
            M = seq[0]
            m = seq[0]
            G = True
            return min_max(seq, contN, M, m)


class MinMaxTestes(unittest.TestCase):
    def test_lista_vazia(self):
        self.assertTupleEqual((None, None), min_max([]))


    def test_lista_len_1(self):
        self.assertTupleEqual((1, 1), min_max([1]))


    def test_lista_consecutivos(self):
        self.assertTupleEqual((0, 500), min_max(list(range(501))))


if __name__ == '__main__':
    unittest.main()
