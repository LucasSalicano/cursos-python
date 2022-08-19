import re


class ExtratorCep:

    def __init__(self, endereco):
        self.endereco = endereco

    def extrair_cep(self):
        padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
        busca = padrao.search(self.endereco)

        if not busca:
            return "CEP não encontrado."

        return busca.group()
