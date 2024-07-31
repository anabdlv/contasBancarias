class NomeCompleto:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    @classmethod #padrao de fabrica
    def fromstring(cls, texto):
        nome, sobrenome = map(str, texto.split(' '))
        objeto = cls(nome, sobrenome)
        return objeto

    @staticmethod
    def isvalid(texto):
        nomes = texto.split(' ')
        return len(nomes) > 1

registro1 = NomeCompleto.fromstring('Luiz Braga')


