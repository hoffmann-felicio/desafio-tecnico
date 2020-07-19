import unittest
import Parser as p
import Familias

class TestLista(unittest.TestCase):
    def test_parser(self):
        parser = p.Parser("/home/hf/PycharmProjects/desafio-tecnico/DB/*.json")
        resultado = parser.parse()
        self.assertIsInstance(resultado, list)