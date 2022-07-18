package org.example;

public class Main {
    public static void main(String[] args) {

        System.out.println(suma(5,10,13));

        Coche miCoche = new Coche();
        miCoche.aumentarNumPuertas();
        System.out.println("Ahora el coche tiene: " + miCoche.numPuertas + " puertas");
    }

    public static int suma(int a, int b, int c){
        return a + b + c;
    }

}
class Coche{
    public int numPuertas = 4;

    public void aumentarNumPuertas(){
        this.numPuertas++;
    }

}