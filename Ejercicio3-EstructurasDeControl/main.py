print('Mostraremos en orden inverso un rango de numeros que tu elijas.')

numero_inicial = int(input('Ingresa el primer valor: '))
numero_final = int(input('Ingresa el segundo valor: '))

for i in range(numero_final,numero_inicial-1,-1):
    print(i)