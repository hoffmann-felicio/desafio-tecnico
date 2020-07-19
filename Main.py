from Familias import Familia
from Parser import Parser as p
from Negocios import Classificador


parser = p("/home/hf/PycharmProjects/desafio-tecnico/DB/*.json")
dados = parser.parse()

lista = []
for f in dados:
    print(f)
    familia = Familia(f)
    renda = familia.get_renda()
    idade = familia.get_idade()
    dependentes = familia.get_dependentes()
    id = familia.id
    status = familia.status
    lista.append({"renda": renda, "idade": idade, "dependentes": dependentes, "id": id, "status": status, "pontuacao": 0, "criterios":0})


classificador = Classificador.Classificador(lista)
lista = classificador.listagem()



print(lista)
