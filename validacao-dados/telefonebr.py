import docbr


class Telefonebr:

    def __init__(self, telefone):
        self._telefone = telefone

    def validate(self):
        tel = docbr.validate(self._telefone, doctype="tfone")

        if not tel:
            raise ValueError("Tel is not valid!")

        print("valid")