from threading import local
import time

horaSalida = 19

print('Son las: ', time.strftime('%H:%M:%S',time.localtime()))
hora = int(time.strftime('%H'))
minuto = int(time.strftime('%M'))
segundo = int(time.strftime('%S'))


if (hora >= horaSalida and (minuto >= 0 or segundo >= 0)):
    print('Es hora de ir a casa.')
else:
    print('Faltan {} hora(s), {} minuto(s) y {} segundo(s) para terminar el horario laboral'.format((horaSalida - 1)- hora,59 - minuto, 59 - segundo))
