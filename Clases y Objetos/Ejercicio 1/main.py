class Vehiculo:
    def __init__(self,color,ruedas,puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self):
        return 'El color del auto es {}, tiene {} ruedas y {} puertas'.format(self.color,self.ruedas,self.puertas)


class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color,ruedas,puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return 'El color del auto es {}, tiene {} ruedas y {} puertas. Su velocidad es de {} y cuenta con {} cilindradas'.format(self.color,self.ruedas,self.puertas,self.velocidad,self.cilindrada)

coche = Coche('Negro',4,5,120,3500)
print(coche)