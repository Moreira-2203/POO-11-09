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

    def AbrirCarro(self, chave):
        if not self.ligado and not self.aberto and self.chave.marca == chave.marca:
            self.aberto = True
            self.chave.ativa = True
            print("O carro está aberto e a chave foi ativada.")
        else:
            print("O carro já está aberto ou ligado ou a chave está errada.")

    def LigarCarro(self):
        if not self.ligado and self.aberto and self.chave.ativa:
            self.ligado = True
            print("O carro está ligado!")
        else:
            print("O carro não pode ser ligado. Verifique se está aberto e a chave ativada.")

    def AceleraCarro(self):
        if self.ligado and self.velocidade >= 0:
            self.velocidade += 5
            print(f"O carro {self.modelo}, velocidade {self.velocidade} KM/h")
        else:
            print(f"O carro {self.modelo}, está desligado.")

    def FreiaCarro(self):
            if self.ligado and self.velocidade > 0:
                self.velocidade -= 5
                if self.velocidade < 0:
                    self.velocidade = 0
                print(f"O carro {self.modelo} reduziu a velocidade para {self.velocidade} KM/h")
            else:
                print(f"O carro {self.modelo} já está parado ou desligado.")

    def DesligarCarro(self):
        if self.ligado and self.velocidade == 0:
            self.ligado = False
            print("O carro foi desligado.")
        elif self.velocidade > 0:
            print("Não é possível desligar o carro em movimento! Reduza a velocidade primeiro.")
        else:
            print("O carro já está desligado.")