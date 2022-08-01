import math

def areaTriangulo(altura,base):
    return altura*base

def areaCirculo(radio):
    area = math.pi*(radio**2)
    return area

areaTri = areaTriangulo(15,10)
areaCir = areaCirculo(5)

print('El area del triangulo es: {}'.format(areaTri))
print('El area del circulo es: {}'.format(round(areaCir,2)))