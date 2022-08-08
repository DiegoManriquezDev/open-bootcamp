f = open('prueba.txt','w')
texto = input('Agrega un texto al fichero: ')
texto += '\n'
f.write(texto)
f.close()

f = open('prueba.txt','r+')
texto2 = input('Agrega un texto al fichero: ')
texto2 += '\n'
f.readline()
f.write(texto2)

print(f.read())
f.close()