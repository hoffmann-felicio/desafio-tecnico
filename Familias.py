import datetime
from dateutil.relativedelta import relativedelta


class Familia:
    def __init__(self,dados):
        self.id = dados.get("id")
        self.status = dados.get("status")
        self.pessoas = dados.get("pessoas")
        self.rendas = dados.get("rendas")

    def get_renda(self):
        renda = 0
        for x in self.rendas:
            renda += x.get('valor')
        return renda

    def get_idade(self):
        for x in self.pessoas:
            if x.get('tipo') == 'Pretendente':
                data = x.get('dataDeNascimento')
                break
        year, month, day = map(int,data.split('-'))
        nascimento = datetime.datetime(year, month, day)
        hoje = datetime.datetime.now()
        idade = relativedelta(hoje,nascimento).years
        return idade

    def get_dependentes(self):
        dependentes = 0
        for x in self.pessoas:
            if x.get('tipo') == "Dependente":
                data = x.get('dataDeNascimento')
                year, month, day = map(int, data.split('-'))
                nascimento = datetime.datetime(year, month, day)
                hoje = datetime.datetime.now()
                idade = relativedelta(hoje, nascimento).years
                if idade <= 18:
                    dependentes += 1
        return dependentes

