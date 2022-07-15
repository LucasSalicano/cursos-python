from unittest import TestCase
from conta import Conta
import unittest


class TestConta(TestCase):

    def setUp(self) -> None:
        self.conta = Conta("1234", "Salicano", 50, 1000)
        self.conta_2 = Conta("4321", "Lucas", 0, 2000)

    def test_depositar(self):
        self.conta.depositar(20)
        assert 70 == self.conta.get_saldo()
        assert self.conta.get_saldo() is not None

    def test_transferir(self):
        self.conta.transferir(self.conta_2, 25)
        assert self.conta_2.get_saldo() == 25
        assert self.conta.get_saldo() == 25

    def test_saque_conta(self):
        conta_saque = Conta("1234", "Lucas", 100, 200)
        conta_saque.sacar(50)
        assert conta_saque.get_saldo() == 50
        assert conta_saque.get_cheque_especial() == 200

    def test_saque_com_cheque_especial(self):
        conta_cheque_especial = Conta("1234", "Lucas", 100, 200)
        conta_cheque_especial.sacar(300)
        assert conta_cheque_especial.get_saldo() == 0
        assert conta_cheque_especial.get_cheque_especial() == 0

    def test_saque_com_saldo_no_cheque_especial(self):
        conta_cheque_especial = Conta("1234", "Lucas", 100, 300)
        conta_cheque_especial.sacar(300)
        assert conta_cheque_especial.get_cheque_especial() == 100

    def test_saque_sem_saldo(self):
        self.assertFalse(self.conta.valida_saque(5000))
