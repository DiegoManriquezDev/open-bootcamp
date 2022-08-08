import operaciones.suma
import operaciones.resta
import operaciones.multiplicacion
import operaciones.division

def main():
    print(operaciones.suma.suma(2,2))
    print(operaciones.resta.resta(15,2))
    print(operaciones.multiplicacion.multiplicacion(7,9))
    print(operaciones.division.division(26,7))


if __name__ == '__main__':
    main()