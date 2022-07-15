class Conta:

    def __init__(self, numero, titular, saldo, cheque_especial):
        print("Construindo objeto {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__cheque_especial = cheque_especial

    def set_cheque_especial(self, cheque_especial):
        self.__cheque_especial = cheque_especial

    def get_saldo(self):
        return self.__saldo

    def get_cheque_especial(self):
        return self.__cheque_especial

    def get_saldo_cheque_especial_mais_saldo(self):
        return self.__saldo + self.__cheque_especial

    def extrato(self):
        print("Titular: {} | Conta: {} | Saldo: {}".format(self.__titular, self.__numero, self.__saldo))

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__realizar_saque_conta(valor) if self.valida_saque(valor) else False

    def transferir(self, conta_destino, valor):
        self.sacar(valor)
        conta_destino.depositar(valor)
        print("Valor transferido com sucesso.")

    def valida_saque(self, valor):
        if valor > self.get_saldo_cheque_especial_mais_saldo():
            return False
        return True

    def __realizar_saque_conta(self, valor):
        if valor > self.get_saldo():
            valor_total_disponivel = self.__saldo + self.__cheque_especial
            valor_total_disponivel -= valor
            self.__saldo -= self.__saldo
            self.__cheque_especial = valor_total_disponivel
        else:
            self.__saldo -= valor
