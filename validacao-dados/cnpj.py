from docbr import api


class Cnpj:

    def __init__(self, cnpj):
        self._cnpj = cnpj

    def validate(self):
        result = api.validate(self._cnpj, doctype="cnpj")

        if not result:
            raise ValueError("CNPJ is not valid!")

        print("CNPJ is valid!")

    def __str__(self):
        return self._cnpj