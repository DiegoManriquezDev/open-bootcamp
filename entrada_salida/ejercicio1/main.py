f = open('prueba.txt','a')

texto = input('Agrega un texto al fichero: ')
texto += '\n'

f.write(texto)
f.close()