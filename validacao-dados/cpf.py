# import re
from docbr import api


class Cpf:

    def __init__(self, cpf):
        self._cpf = cpf

    def validate(self):
        # cpf_mask = "[0-9]{3}[.][0-9]{3}[.][0-9]{3}[-][0-9]{2}"
        # recompile_mask = re.compile(cpf_mask)
        # result = recompile_mask.search(self._cpf)
        result = api.validate(self._cpf, doctype="cpf")

        if not result:
            raise ValueError("CPF is not valid!")

        print("CPF is valid!")

    def __str__(self):
        return self._cpf
