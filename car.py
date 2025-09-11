
# Definição da Classe
class Chave:
    # Método contrutor
    def __init__(self, marca):
        self.marca = marca
        self.ativa = False
    
# Definir a classe
class Carro:
    def __init__(self, modelo, ano, cor, potencia, placa, chave:Chave, velocidade):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.potencia = potencia
        self.placa = placa
        self.ligado = False
        self.aberto = False
        self.chave = chave
        self.velocidade = velocidade


    # Métodos / Ação realizada pela classe
    def AbrirCarro (self, chave):
        if not self.ligado and not self.aberto and self.chave.marca == chave.marca:
            self.aberto = True
            print("O carro está aberto.")
        else:
            print("O carro ja está aberto ou ligado ou a chave está errada.")

    def LigarCarro(self):
        if not self.ligado and self.aberto:
            self.ligado = True
            print("O carro está ligado !")
        else:
            print("O carro não está aberto ou já está ligado.")

    def AceleraCarro(self):
        if self.ligado and self.velocidade >= 0:
            self.velocidade += 5
            print(f"O carro {self.modelo}, velocidade {self.velocidade} KM/h")
        else:
            print(f"O carro {self.modelo}, está desligado.")
