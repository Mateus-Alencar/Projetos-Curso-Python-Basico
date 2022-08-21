class Conta:
    def __init__(self, cliente, saldo):
        self.cliente = cliente
        self.saldo = saldo
    def depositar(self, quant):
        if quant > 0:
            self.saldo += quant
        else:
            print('Erro no depósito')

    def consultar_saldo(self):
        return self.saldo