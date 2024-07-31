from veiculo import Veiculo
from onibus import Onibus

modelo_carro = Veiculo('fusca', 180, 10)
modelo_carro.toStr()

modelo_onibus = Onibus('Scania', 120, 8)
modelo_onibus.toStr()
modelo_onibus.capacidade_assentos()