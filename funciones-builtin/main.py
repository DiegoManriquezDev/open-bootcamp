paises = []

agregarPais = int(input('Quieres agregar un país a la lista?\nSi: Ingresa el numero 1\nNo:Ingresa el numero\n'))

while agregarPais == 1:
    pais = input('Ingresa el pais que quieres agregar a la lista:\n')
    paises.append(pais)
    agregarPais = int(input('Quieres agregar un país a la lista?\nSi: Ingresa el numero 1\nNo:Ingresa el numero 2\n'))



paisesSinRepetir = set(paises)
paisesOrdenados = sorted(paisesSinRepetir)

print(paisesOrdenados)