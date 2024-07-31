from contas import Conta
from clientes import Cliente

cliente1 = Cliente(123, 'Joao', 'Rua 1')
cliente2 = Cliente(345, 'Maria', 'Rua 2')
cliente3 = Cliente(678, 'Julia', 'Rua 3')
cliente4 = Cliente(100, 'Marcos', 'Rua 4')

conta1 = Conta([cliente1, cliente2], 1, 0)
print(f'A conta 1 possui dois clientes: {conta1.clientes[0].nome} e {conta1.clientes[1].nome}')
conta1.gerarsaldo()
conta1.depositar(1500)
conta1.sacar(500)
conta1.gerarsaldo()

conta2 = Conta([cliente3, cliente4], 2, 500)
print(f'Os endereços dos clientes da conta 2 são: {conta2.clientes[0].endereco} e {conta2.clientes[1].endereco}')
conta2.gerarsaldo()
conta2.depositar(1500)
conta2.sacar(500)
conta2.gerarsaldo()
