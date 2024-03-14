class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudar(self):
        print(f'Olá, {self.nome}!')

p1 = Pessoa('Jorge', 20)
p1.saudar()
p2 = Pessoa('Maria', 30)
p2.saudar()


class Estudante(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def estudar(self):
        print(f'{self.nome} está estudando!')

e1 = Estudante('Jorge', 20, 'matricula123')
e1.saudar()
e1.estudar()

class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def consultarSaldo(self):
        print(f'Saldo: {self.__saldo}')

c1 = ContaBancaria(1000)
c1.depositar(500)
c1.consultarSaldo()
c1.sacar(200)
c1.consultarSaldo()