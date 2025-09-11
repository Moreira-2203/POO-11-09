from car import Chave
from car import Carro


ch = Chave ("FIAT")
ch1 = Chave ("VW")

car1 = Carro ("Uno", "1998", "Branco", 1.0, "SQ007", ch, 0)

car1.AbrirCarro(ch)

car1.LigarCarro()

for i in range(5):
    car1.AceleraCarro()

print(car1.chave.marca)

# O carro tem que desligar, mas não pode desligar acelerado
# tem que ter um método de freiar de 5 em 5
# e tem que ter a inserção da ativação da chave assim que o
# método abrir for TRUE

