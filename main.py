from car import Chave
from car import Carro


ch = Chave ("FIAT")
ch1 = Chave ("VW")

car1 = Carro ("Uno", "1998", "Branco", 1.0, "SQ007", ch, 0)

car1.AbrirCarro(ch1)

car1.AbrirCarro(ch)

car1.LigarCarro()

for i in range(5):
    car1.AceleraCarro()

for i in range(5):
    car1.FreiaCarro() 

car1.DesligarCarro()

print(car1.chave.marca)
