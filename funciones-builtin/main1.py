from functools import reduce


lista = [1,2,3,4,5,6,7,8,9]

elementosImpares = list(filter(lambda x: x % 2 != 0, lista))

sumaElementos = reduce(lambda a,b: a+b, elementosImpares)

print(sumaElementos)

