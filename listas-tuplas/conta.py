from abc import ABC, abstractmethod
from functools import total_ordering


@total_ordering
class Conta:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod
    def juros(self):
        pass

    def __eq__(self, other):
        if type(other) != type(self):
            return False

        return self._codigo == other._codigo

    def __str__(self):
        return "[Codigo {}, Saldo {}]".format(self._codigo, self._saldo)

    def __lt__(self, other):
        return self._saldo < other._saldo
