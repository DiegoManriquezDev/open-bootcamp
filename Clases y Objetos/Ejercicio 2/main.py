class Alumno:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        if self.nota < 51:
            return 'El alumno {}, saco "{}" y ha Reprobado!'.format(self.nombre,self.nota)
        else:
            return 'El alumno {}, saco "{}" y ha Aprobado!'.format(self.nombre,self.nota)


alumno = Alumno('Diego',85)
print(alumno)