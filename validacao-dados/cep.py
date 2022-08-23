import requests


class Cep:

    def __init__(self, cep):
        self._cep = cep

    def consultar(self):
        url = "https://viacep.com.br/ws/{}/json".format(self._cep)
        response = requests.get(url)

        if response.text.find("erro") < 1:
            raise Exception("CEP inválido.")

        return response.text
