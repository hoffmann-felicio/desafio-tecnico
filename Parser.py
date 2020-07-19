import json
import glob


class Parser:
    def __init__(self, path):
        self.path = path
        self.lista = []

    def parse(self):
        files = glob.glob(self.path)
        for nome in files:
            with open(nome) as f:
                dados = f.read()
                f.close()
                familia = json.loads(dados)
            self.lista.append(familia)
        return self.lista
