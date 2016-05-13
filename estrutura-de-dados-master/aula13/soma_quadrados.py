
from collections import Counter

def soma_quadrados(n):

    resultados = {0: [0]}
    quadrados = []
    num = 1
    if n == 0:
        return [0]
    else:
        while num**2 <= n:
            quadrados.append(num**2)
            num += 1
        while len(quadrados) > 0:
            valor = n
            quadrado = quadrados.copy()
            aux = quadrado.pop()
            resposta=[]
            while valor > 0:
                if valor in resultados.keys() and valor is not n:
                    resposta = resposta + resultados[valor]
                    valor = 0
                else:
                    if len(quadrado) > 0:
                        aux2 = valor - aux
                        if aux2 < 0: aux = quadrado.pop()
                        else:
                            valor = valor-aux
                            resposta.append(aux)
                    else:
                        valor = valor - aux
                        resposta.append(aux)
            if n not in resultados.keys() and n != 0:
                resultados[n] = resposta.copy()
            elif len(resposta) < len(resultados[n]): resultados[n] = resposta.copy()
            quadrados.pop()

        return resultados[n]


import unittest


class SomaQuadradosPerfeitosTestes(unittest.TestCase):
    def teste_0(self):
        self.assert_possui_mesmo_elementos([0], soma_quadrados(0))

    def teste_1(self):
        self.assert_possui_mesmo_elementos([1], soma_quadrados(1))

    def teste_2(self):
        self.assert_possui_mesmo_elementos([1, 1], soma_quadrados(2))

    def teste_3(self):
        self.assert_possui_mesmo_elementos([1, 1, 1], soma_quadrados(3))

    def teste_4(self):
        self.assert_possui_mesmo_elementos([4], soma_quadrados(4))

    def teste_5(self):
        self.assert_possui_mesmo_elementos([4, 1], soma_quadrados(5))

    def teste_11(self):
        self.assert_possui_mesmo_elementos([9, 1, 1], soma_quadrados(11))

    def teste_12(self):
        self.assert_possui_mesmo_elementos([4, 4, 4], soma_quadrados(12))

    def assert_possui_mesmo_elementos(self, esperado, resultado):
        self.assertEqual(Counter(esperado), Counter(resultado))