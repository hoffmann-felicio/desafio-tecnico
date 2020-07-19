class Classificador:
    def __init__(self, lista):
        self.familias = lista
        self.f_valid = []
        for x in self.familias:
            if x.get('status') == "0":
                self.f_valid.append(x)


    def pontuacao(self):
        for x in self.f_valid:
            x['pontuacao'] += self.ponto_renda(x)
            x['pontuacao'] += self.ponto_idade(x)
            x['pontuacao'] += self.ponto_dependentes(x)
    def ponto_renda(self, fam):
        renda = fam.get('renda')
        if renda <= 900:
            return 5
        elif renda <= 1500:
            return 3
        elif renda <= 2000:
            return 1

    def ponto_idade(self, fam):
        idade = fam.get('idade')
        if idade < 30:
            return 1
        elif idade <= 44:
            return 2
        else:
            return 3

    def ponto_dependentes(self, fam):
        dependentes = fam.get('dependentes')
        if dependentes >= 3:
            return 3
        elif dependentes > 0:
            return 2


    def listagem(self):
        self.pontuacao()
        print(self.f_valid)
        self.f_valid.sort(key=lambda k: k['pontuacao'], reverse=True)
        print(self.f_valid)
        return self.f_valid
