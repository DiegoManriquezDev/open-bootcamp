def esNumeroPrimo(numero):
    aux = True
    for i in range(2,numero):
        if(numero % i == 0):
            aux = False
            return aux
    return aux

numero = int(input('Ingresa el valor para saber si es primo o no: '))

if(numero == 1):
    print('El numero 1 no se considera ni primo in compuesto.')
elif(esNumeroPrimo(numero)):
    print('Es un numero primo!')
else:
    print('No es un numero primo.')