class Pessoa:
    _contador = 0

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        Pessoa._contador += 1

    def imprimir(self):
        print(self.nome, ' tem ', self.idade, ' anos ')

    @property #-> facilita o acesso a elementos estáticos
    def contador(self):
        return type(self)._contador


p1 = Pessoa('Carlos', 18)
p2 = Pessoa('Ana', 15)
print(p1.contador) #chama a propriedade
print(Pessoa._contador) #chama a variável

