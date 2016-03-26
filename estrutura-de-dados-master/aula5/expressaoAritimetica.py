# Exercício de avaliação de expressão aritmética.
# Só podem ser usadas as estruturas Pilha e Fila implementadas em aulas anteriores.
# Deve ter análise de tempo e espaço para função avaliação
from collections import deque


#Complexidade: Tempo O(n) Espaço: O(n)

from aula5.fila import Fila
from aula4.pilha import Pilha

class FilaVaziaErro(Exception):
    pass



class ErroLexico(Exception):
    pass


class ErroSintatico(Exception):
    pass


def analise_lexica(expressao):
    fila = Fila()
    especiais = '{[()]}+-*/.'
    quant = ''
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    sequenciaNumerica = '0123456789'
    for caracter in expressao:
        if caracter in especiais:
            if len(quant):
                fila.enfileirar(quant)
                quant = ''
            fila.enfileirar(caracter)
        if caracter in set(sequenciaNumerica):
            quant = quant + caracter
        if caracter in set(alfabeto) or caracter == '':
            raise ErroLexico('')
    if len(quant):
        fila.enfileirar(quant)
    return fila


def analise_sintatica(fila):
    especiais = '+-*/(){}[]'
    filaObjeto = Fila()
    caracter = ''
    if not(len(fila)): raise ErroSintatico('')
    while len(fila):
        atual = fila.desenfileirar()
        if atual in especiais:
            if len(caracter):#Verificanto se é int ou float
                if '.' not in caracter:
                    filaObjeto.enfileirar(int(caracter))
                else: filaObjeto.enfileirar(float(caracter))
                caracter = ''
            filaObjeto.enfileirar(atual)
        else: caracter += atual
    if len(caracter):
        if '.' not in caracter: caracter = int(caracter)
        else: caracter = float(caracter)
        filaObjeto.enfileirar(caracter)
    return filaObjeto


def avaliar(expressao):
    pilha = Pilha()
    analise = analise_sintatica(analise_lexica(expressao))
    especiais = '{[()]}'
    matematicos = '+-*/'
    for atual in analise:
        pilha.empilhar(atual)
        if len(pilha) >= 3:
            p1, p2, p3 = pilha.desempilhar(), pilha.desempilhar(), pilha.desempilhar()
            if str(p1) not in especiais and str(p3) not in especiais and str(p2) in matematicos:
                if p2 == '+': controle = p3 + p1
                elif p2 == '-': controle = p3 - p1
                elif p2 == '*': controle = p3 * p1
                else: controle = p3 / p1
                pilha.empilhar(controle)
            else:
                pilha.empilhar(p3)
                pilha.empilhar(p2)
                pilha.empilhar(p1)
        if str(atual) in ')]}':
            pilha.desempilhar()
            controle = pilha.desempilhar()
            pilha.desempilhar()
            pilha.empilhar(controle)
            if len(pilha) >= 3:
                p1, p2, p3 = pilha.desempilhar(), pilha.desempilhar(), pilha.desempilhar()
                if str(p1) not in especiais and str(p3) not in especiais and str(p2) in matematicos:
                    if p2 == '+': controle = p3 + p1
                    elif p2 == '-': controle = p3 - p1
                    elif p2 == '*': controle = p3 * p1
                    else: controle = p3 / p1
                    pilha.empilhar(controle)
                else:
                    pilha.empilhar(p3)
                    pilha.empilhar(p2)
                    pilha.empilhar(p1)
    return pilha.desempilhar()


import unittest


class AnaliseLexicaTestes(unittest.TestCase):
    def test_expressao_vazia(self):
        fila = analise_lexica('')
        self.assertTrue(fila.vazia())

    def test_caracter_estranho(self):
        self.assertRaises(ErroLexico, analise_lexica, 'a')
        self.assertRaises(ErroLexico, analise_lexica, 'ab')

    def test_inteiro_com_um_algarismo(self):
        fila = analise_lexica('1')
        self.assertEqual('1', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_inteiro_com_vários_algarismos(self):
        fila = analise_lexica('1234567890')
        self.assertEqual('1234567890', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_float(self):
        fila = analise_lexica('1234567890.34')
        self.assertEqual('1234567890', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('34', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_parenteses(self):
        fila = analise_lexica('(1)')
        self.assertEqual('(', fila.desenfileirar())
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual(')', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_chaves(self):
        fila = analise_lexica('{(1)}')
        self.assertEqual('{', fila.desenfileirar())
        self.assertEqual('(', fila.desenfileirar())
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual(')', fila.desenfileirar())
        self.assertEqual('}', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_colchetes(self):
        fila = analise_lexica('[{(1.0)}]')
        self.assertEqual('[', fila.desenfileirar())
        self.assertEqual('{', fila.desenfileirar())
        self.assertEqual('(', fila.desenfileirar())
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertEqual(')', fila.desenfileirar())
        self.assertEqual('}', fila.desenfileirar())
        self.assertEqual(']', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_adicao(self):
        fila = analise_lexica('1+2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('+', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_subtracao(self):
        fila = analise_lexica('1-2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('-', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_multiplicacao(self):
        fila = analise_lexica('1*2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('*', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_divisao(self):
        fila = analise_lexica('1/2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('/', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_expresao_com_todos_simbolos(self):
        expressao = '1/{2.0+3*[7-(5-3)]}'
        fila = analise_lexica(expressao)
        self.assertListEqual(list(expressao), [e for e in fila])
        self.assertTrue(fila.vazia())


class AnaliseSintaticaTestes(unittest.TestCase):
    def test_fila_vazia(self):
        fila = Fila()
        self.assertRaises(ErroSintatico, analise_sintatica, fila)

    def test_int(self):
        fila = Fila()
        fila.enfileirar('1234567890')
        fila_sintatica = analise_sintatica(fila)
        self.assertEqual(1234567890, fila_sintatica.desenfileirar())
        self.assertTrue(fila_sintatica.vazia())

    def test_float(self):
        fila = Fila()
        fila.enfileirar('1234567890')
        fila.enfileirar('.')
        fila.enfileirar('4')
        fila_sintatica = analise_sintatica(fila)
        self.assertEqual(1234567890.4, fila_sintatica.desenfileirar())
        self.assertTrue(fila_sintatica.vazia())

    def test_expressao_com_todos_elementos(self):
        fila = analise_lexica('1000/{222.125+3*[7-(5-3)]}')
        fila_sintatica = analise_sintatica(fila)
        self.assertListEqual([1000, '/', '{', 222.125, '+', 3, '*', '[', 7, '-', '(', 5, '-', 3, ')', ']', '}'],
                             [e for e in fila_sintatica])


class AvaliacaoTestes(unittest.TestCase):
    def test_expressao_vazia(self):
        self.assertRaises(ErroSintatico, avaliar, '')

    def test_inteiro(self):
        self.assert_avaliacao('1')

    def test_float(self):
        self.assert_avaliacao('2.1')

    def test_soma(self):
        self.assert_avaliacao('2+1')

    def test_subtracao_e_parenteses(self):
        self.assert_avaliacao('(2-1)')

    def test_expressao_com_todos_elementos(self):
        self.assertEqual(1.0, avaliar('2.0/[4*3+1-{15-(1+3)}]'))

    def assert_avaliacao(self, expressao):
        self.assertEqual(eval(expressao), avaliar(expressao))


if __name__ == '__main__':
    unittest.main()