package org.example;

public class Main {
    public static void main(String[] args) {
        //Objeto Cliente
        Cliente cliente1 = new Cliente();

        cliente1.edad = 31;
        System.out.println("Edad: " + cliente1.edad);
        cliente1.nombre = "Erika";
        System.out.println("Nombre: " + cliente1.nombre);
        cliente1.telefono = "+5917654646";
        System.out.println("Telefono: " + cliente1.telefono);
        cliente1.credito = 250;
        System.out.println("Credito: " + cliente1.credito);

        //Objeto Trabajador
        Trabajador trabajador1 = new Trabajador();

        trabajador1.edad = 30;
        System.out.println("Edad: " + trabajador1.edad);
        trabajador1.nombre = "Diego";
        System.out.println("Nombre: " + trabajador1.nombre);
        trabajador1.telefono = "+59178565014";
        System.out.println("Telefono: " + trabajador1.telefono);
        trabajador1.salario = 5000.50;
        System.out.println("Salario: " + trabajador1.salario);

    }
}

class Persona{
    int edad;
    String nombre;
    String telefono;

}

class Cliente extends Persona{
    int credito;
}

class Trabajador extends Persona{
    double salario;
}

