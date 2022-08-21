from cliente import Cliente
from conta import Conta

cliente1 = Cliente('gui', '123.123.123-10', 27)
print(cliente1)
conta1 = Conta(cliente1, 100)

conta1.depositar(100)
print(conta1.consultar_saldo())
