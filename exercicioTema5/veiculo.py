class Veiculo:
    def __init__(self, nome, velocidade_max, quilometro_litro):
        self.nome = nome
        self.velocidade_max = velocidade_max
        self.quilometro_litro = quilometro_litro

    def capacidade_assentos(self, capacidade):
        print(f'A capacidade máxima de assentos do veículo {self.nome} é {capacidade}')

    def toStr(self):
        print(f'nome = {self.nome}')
        print(f'velocidade maxima = {self.velocidade_max}')
        print(f'Quilometros percorridos por litro = {self.quilometro_litro}')