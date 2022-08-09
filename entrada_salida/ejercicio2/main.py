import pickle
import pprint


class Vehiculo:
    def __init__(self,marca,velocidad):
        self.marca = marca
        self.velocidad = velocidad
    
    def __str__(self):
        return f'El auto es un {self.marca} y su velocidad es de {self.velocidad} km/hr'


vehiculo1 = Vehiculo('Toyota',120)
file = open('vehiculo.bin','wb')
pickle.dump(vehiculo1,file)
file.close()

file1 = open('vehiculo.bin','rb')
pprint.pprint(file1.read())
file1.seek(0)
vehiculo = pickle.load(file1)
print(vehiculo)
file1.close()