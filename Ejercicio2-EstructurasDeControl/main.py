print('Calcularemos cuales son los numeros impares entre un rango de numeros que tu elijas')

listImpares = []
numero_inicial = int(input('Elije el numero inicial: '))
numero_final = int(input('Elije el numero final: '))

for i in range(numero_inicial,numero_final + 1,1):
    if(i % 2 != 0):
        listImpares.append(i)

print('Los numeros impares entre {} y {} son: {}'.format(numero_inicial,numero_final,listImpares))