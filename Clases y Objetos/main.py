class Vehiculo:
    color = "Negro"
    ruedas = 4
    puertas = 5

class Coche(Vehiculo):
    velocidad = 120.0
    cilindrada = 3000

coche = Coche()
print(coche.color)
print(coche.ruedas)
print(coche.puertas)
print(coche.velocidad)
print(coche.cilindrada)