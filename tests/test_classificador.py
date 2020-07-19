import unittest
from Negocios import Classificador as cl

class TestPontos(unittest.TestCase):
    #pontuação deve ser um valor inteiro
    def test_renda(self):
        dados = {'renda': 700, 'idade': 30, 'dependentes': 0, 'id': '1dac7da3-d742-4e51-95f9-bbb37f522413', 'status': '0', 'pontuacao': 0, 'criterios': 0}
        resultado = cl.Classificador.ponto_renda(self, dados)
        self.assertIsInstance(resultado, int)

    def test_dependentes(self):
        dados = {'renda': 700, 'idade': 30, 'dependentes': 0, 'id': '1dac7da3-d742-4e51-95f9-bbb37f522413',
                 'status': '0', 'pontuacao': 0, 'criterios': 0}
        resultado = cl.Classificador.ponto_dependentes(self, dados)
        self.assertIsInstance(resultado, int)

    def test_idade(self):
        dados = {'renda': 700, 'idade': 30, 'dependentes': 0, 'id': '1dac7da3-d742-4e51-95f9-bbb37f522413', 'status': '0', 'pontuacao': 0, 'criterios': 0}
        resultado = cl.Classificador.ponto_idade(self, dados)
        self.assertIsInstance(resultado, int)
