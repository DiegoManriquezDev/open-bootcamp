package org.example;

import jdk.swing.interop.SwingInterOpUtils;

public class Main {
    public static void main(String[] args) {

        //Usando un if
        int numeroIf = 0;

        if(numeroIf > 0){
            System.out.println("La variable numeroIf es un numero positivo");
        } else if (numeroIf < 0) {
            System.out.println("La variable numeroIf es un numero negativo");
        }else {
            System.out.println("La variable numeroIf es cero");
        }

        //Usando el bucle while
        int numeroWhile = -5;
        while (numeroWhile < 3){
            System.out.println(numeroWhile);
            numeroWhile++;
        }

        //Usando el bucle Do While
        int numeroDoWhile = 2;
        do {
            System.out.println("El valor de numeroDoWhile es: " + numeroDoWhile);
            numeroDoWhile++;
        }while (numeroDoWhile < 3);

        //Usando el bucle For
        for (int numeroFor = 0; numeroFor <= 3; numeroFor++){
            System.out.println("El valor de numero for es: " + numeroFor);
        }

        //Usando la sentencia switch
        String estacion = "INVIERNO";
        switch (estacion){
            case "PRIMAVERA":
                System.out.println("Que hermosa primavera! xD");
                break;
            case "VERANO":
                System.out.println("Hora de ir a la playa! Aprovechemos el VERANO!");
                break;
            case "OTOÑO":
                System.out.println("OTOÑO, comienzan a caer las hojas!");
                break;
            case "INVIERNO":
                System.out.println("El INVIERNO mas frio de la decada! =s");
                break;
            default:
                System.out.println("No se detecta ninguna estacion, verifica el dato que estas colocando -.-");
                break;
        }


    }
}