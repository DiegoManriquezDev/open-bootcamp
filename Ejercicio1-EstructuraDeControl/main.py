edad = int(input('Bienvenido a la fiesta, que edad tienes?? '))

if(edad >= 18):
    print('Tienes {} años, eres mayor de edad, puedes pasar.'.format(edad))
else:
    print('Lo siento eres mu joven, no puedes ingresar con {} años'.format(edad))