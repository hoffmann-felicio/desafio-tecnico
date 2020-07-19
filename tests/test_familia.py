import unittest
import Familias as f

class TestFamilia(unittest.TestCase):
    def test_renda(self):
        dados = {'id': '1dac7da3-d742-4e51-95f9-bbb37f522413', 'pessoas': [{'id': '5e65eea1-aa72-407e-9a67-88045c07b5de', 'nome': 'João', 'tipo': 'Pretendente', 'dataDeNascimento': '1989-12-30'}, {'id': 'd467781a-8f06-45ba-be6f-879cf32a9f7e', 'nome': 'Maria', 'tipo': 'Cônjuge', 'dataDeNascimento': '1989-12-30'}, {'id': '79820382-a181-42d2-bfae-6c012489e65e', 'nome': 'José', 'tipo': 'Dependente', 'dataDeNascimento': '2000-12-30'}, {'id': '80fa071e-17fb-4b87-99db-a7db0bfc23c2', 'nome': 'Angela', 'tipo': 'Dependente', 'dataDeNascimento': '2000-12-30'}], 'rendas': [{'pessoaId': '5e65eea1-aa72-407e-9a67-88045c07b5de', 'valor': 1000}, {'pessoaId': 'd467781a-8f06-45ba-be6f-879cf32a9f7e', 'valor': 700}], 'status': '0'}
        fam = f.Familia(dados)
        resultado = fam.get_renda()
        self.assertIsInstance(resultado, int)

    def test_idade(self):
        dados = {'id': '1dac7da3-d742-4e51-95f9-bbb37f522413', 'pessoas': [{'id': '5e65eea1-aa72-407e-9a67-88045c07b5de', 'nome': 'João', 'tipo': 'Pretendente', 'dataDeNascimento': '1989-12-30'}, {'id': 'd467781a-8f06-45ba-be6f-879cf32a9f7e', 'nome': 'Maria', 'tipo': 'Cônjuge', 'dataDeNascimento': '1989-12-30'}, {'id': '79820382-a181-42d2-bfae-6c012489e65e', 'nome': 'José', 'tipo': 'Dependente', 'dataDeNascimento': '2000-12-30'}, {'id': '80fa071e-17fb-4b87-99db-a7db0bfc23c2', 'nome': 'Angela', 'tipo': 'Dependente', 'dataDeNascimento': '2000-12-30'}], 'rendas': [{'pessoaId': '5e65eea1-aa72-407e-9a67-88045c07b5de', 'valor': 1000}, {'pessoaId': 'd467781a-8f06-45ba-be6f-879cf32a9f7e', 'valor': 700}], 'status': '0'}
        fam = f.Familia(dados)
        resultado = fam.get_idade()
        self.assertIsInstance(resultado, int)

    def test_dependentes(self):
        dados = {'id': '1dac7da3-d742-4e51-95f9-bbb37f522413', 'pessoas': [{'id': '5e65eea1-aa72-407e-9a67-88045c07b5de', 'nome': 'João', 'tipo': 'Pretendente', 'dataDeNascimento': '1989-12-30'}, {'id': 'd467781a-8f06-45ba-be6f-879cf32a9f7e', 'nome': 'Maria', 'tipo': 'Cônjuge', 'dataDeNascimento': '1989-12-30'}, {'id': '79820382-a181-42d2-bfae-6c012489e65e', 'nome': 'José', 'tipo': 'Dependente', 'dataDeNascimento': '2000-12-30'}, {'id': '80fa071e-17fb-4b87-99db-a7db0bfc23c2', 'nome': 'Angela', 'tipo': 'Dependente', 'dataDeNascimento': '2000-12-30'}], 'rendas': [{'pessoaId': '5e65eea1-aa72-407e-9a67-88045c07b5de', 'valor': 1000}, {'pessoaId': 'd467781a-8f06-45ba-be6f-879cf32a9f7e', 'valor': 700}], 'status': '0'}
        fam = f.Familia(dados)
        resultado = fam.get_dependentes()
        self.assertIsInstance(resultado, int)