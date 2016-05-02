
def calcular_frequencias(s):
    if len(s) == 0:
        return {}
    else:
        sequencia = {}
        for procura in s:
            if (procura in sequencia.keys()): sequencia[procura] = sequencia[procura] + 1
            else: sequencia[procura] = 1
    return sequencia

def gerar_arvore_de_huffman(s):
    sequencia = calcular_frequencias(s)
    for a, b in sequencia.items():
        caracter = a
        menor = b
        break
    for a, b in sequencia.items():
        if b <= menor:
            menor = b
            caracter = a
    sequencia.__delitem__(caracter)
    arvore = Arvore(caracter,menor)
    while len(sequencia.keys()) > 0:
        for a, b in sequencia.items():
            caracter = a
            menor = b
            break
        for a, b in sequencia.items():
            if b <= menor:
                caracter = a
                menor = b
        arvore = arvore.fundir(Arvore(caracter,menor))
        sequencia.__delitem__(caracter)
    return arvore

def codificar(cod_dict, s):
    dic = cod_dict
    cod = ""
    for i in s:
        if i in dic.keys():
            cod += dic[i]
    return cod

class Noh:
    def __init__(self, peso, esquerdo = None, direito = None):
        self.peso = peso
        self.esquerdo = esquerdo
        self.direito = direito
        self.nome = "Noh"

    def __hash__(self):
        return hash(self.peso)

    def __eq__(self, other):
        if other is None or not isinstance(other, Noh): return False
        else: return self.peso == other.peso and self.esquerdo == other.esquerdo and self.direito == other.direito

class Folha():
    def __init__(self, char, peso):
        self.char = char
        self.peso = peso
        self.noh = Noh(peso)
        self.nome = "Folha"

    def __hash__(self):
        return hash(self.__dict__)

    def __eq__(self, other):
        if other is None or not isinstance(other, Folha): return False
        else: return self.__dict__ == other.__dict__

class Arvore(object):
    def __init__(self, char = None, peso = None):
        self.char = char
        self.peso = peso

        if self.char: self.raiz = Folha(self.char, self.peso)
        else: self.raiz = None

    def __hash__(self):
        return hash(self.raiz)

    def __eq__(self, other):
        if not(other): return False
        else: return self.raiz == other.raiz

    def fundir(self, arvore):
        if self.peso > arvore.peso:
            maior = self.raiz
            menor = arvore.raiz
        else:
            maior = arvore.raiz
            menor = self.raiz
        peso = self.peso + arvore.peso
        raiz = Noh(peso, maior, menor)
        novaArvore = Arvore(peso = peso)
        novaArvore.raiz = raiz
        return novaArvore

    def cod_dict(self):
        dic = {}
        caminho = []
        visitar = []
        visitar.append(self.raiz)
        while len(visitar) != 0:
            atual = visitar.pop()
            if isinstance(atual, Folha):
                letra = atual.char
                dic[letra] = ''.join(caminho)
                caminho.pop()
                caminho.append('1')
            else:
                visitar.append(atual.direito)
                visitar.append(atual.esquerdo)
                caminho.append('0')
        return dic

    def decodificar(self, caminho):
        letras = []
        atual = self.raiz
        if isinstance(atual, Folha): return atual.char
        else:
            for i in caminho:
                if i == '0': atual = atual.esquerdo
                else: atual = atual.direito
                if isinstance(atual, Folha):
                    letras.append(atual.char)
                    atual = self.raiz
        return ''.join(letras)

import unittest
from unittest import TestCase


class CalcularFrequenciaCarecteresTestes(TestCase):
    def teste_string_vazia(self):
        self.assertDictEqual({}, calcular_frequencias(''))

    def teste_string_nao_vazia(self):
        self.assertDictEqual({'a': 3, 'b': 2, 'c': 1}, calcular_frequencias('aaabbc'))

class NohTestes(TestCase):
    def teste_folha_init(self):
        folha = Folha('a', 3)
        self.assertEqual('a', folha.char)
        self.assertEqual(3, folha.peso)

    def teste_folha_eq(self):
        self.assertEqual(Folha('a', 3), Folha('a', 3))
        self.assertNotEqual(Folha('a', 3), Folha('b', 3))
        self.assertNotEqual(Folha('a', 3), Folha('a', 2))
        self.assertNotEqual(Folha('a', 3), Folha('b', 2))

    def testes_eq_sem_filhos(self):
        self.assertEqual(Noh(2), Noh(2))
        self.assertNotEqual(Noh(2), Noh(3))

    def testes_eq_com_filhos(self):
        noh_com_filho = Noh(2)
        noh_com_filho.esquerdo = Noh(3)
        self.assertNotEqual(Noh(2), noh_com_filho)

    def teste_noh_init(self):
        noh = Noh(3)
        self.assertEqual(3, noh.peso)
        self.assertIsNone(noh.esquerdo)
        self.assertIsNone(noh.direito)


def _gerar_arvore_aaaa_bb_c():
    raiz = Noh(7)
    raiz.esquerdo = Folha('a', 4)
    noh = Noh(3)
    raiz.direito = noh
    noh.esquerdo = Folha('b', 2)
    noh.direito = Folha('c', 1)
    arvore_esperada = Arvore()
    arvore_esperada.raiz = raiz
    return arvore_esperada


class ArvoreTestes(TestCase):
    def teste_init_com_defaults(self):
        arvore = Arvore()
        self.assertIsNone(arvore.raiz)

    def teste_init_sem_defaults(self):
        arvore = Arvore('a', 3)
        self.assertEqual(Folha('a', 3), arvore.raiz)

    def teste_fundir_arvores_iniciais(self):
        raiz = Noh(3)
        raiz.esquerdo = Folha('b', 2)
        raiz.direito = Folha('c', 1)
        arvore_esperada = Arvore()
        arvore_esperada.raiz = raiz

        arvore = Arvore('b', 2)
        arvore2 = Arvore('c', 1)
        arvore_fundida = arvore.fundir(arvore2)
        self.assertEqual(arvore_esperada, arvore_fundida)

    def teste_fundir_arvores_nao_iniciais(self):
        arvore_esperada = _gerar_arvore_aaaa_bb_c()

        arvore = Arvore('b', 2)
        arvore2 = Arvore('c', 1)
        arvore3 = Arvore('a', 4)
        arvore_fundida = arvore.fundir(arvore2)
        arvore_fundida = arvore3.fundir(arvore_fundida)

        self.assertEqual(arvore_esperada, arvore_fundida)

    def teste_gerar_dicionario_de_codificacao(self):
        arvore = _gerar_arvore_aaaa_bb_c()
        self.assertDictEqual({'a': '0', 'b': '10', 'c': '11'}, arvore.cod_dict())

    def teste_decodificar(self):
        arvore = _gerar_arvore_aaaa_bb_c()
        self.assertEqual('aaaabbc', arvore.decodificar('0000101011'))


class TestesDeIntegracao(TestCase):
    def teste_gerar_arvore_de_huffman(self):
        arvore = _gerar_arvore_aaaa_bb_c()
        self.assertEqual(arvore, gerar_arvore_de_huffman('aaaabbc'))

    def teste_codificar(self):
        arvore = gerar_arvore_de_huffman('aaaabbc')
        self.assertEqual('0000101011', codificar(arvore.cod_dict(), 'aaaabbc'))
        self.assertEqual('aaaabbc', arvore.decodificar('0000101011'))

if __name__=='__main__':
    unittest.main()