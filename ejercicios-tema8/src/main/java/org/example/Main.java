package org.example;

public class Main {
    public static void main(String[] args) {

        Persona usuario1 = new Persona();
        usuario1.setEdad(30);
        System.out.println("Mi edad es: " + usuario1.getEdad());

        usuario1.setNombre("Diego");
        System.out.println("Mi nombre es: " + usuario1.getNombre());

        usuario1.setTelefono("+59178565014");
        System.out.println("Mi telefono es: " + usuario1.getTelefono());

    }
}

class Persona{
    private int edad;
    private String nombre;
    private String telefono;

    public void setEdad(int edad){
        this.edad = edad;
    }
    public int getEdad(){
        return this.edad;
    }

    public void setNombre(String nombre){
        this.nombre = nombre;
    }
    public String getNombre(){
        return this.nombre;
    }

    public void setTelefono(String telefono){
        this.telefono = telefono;
    }
    public String getTelefono(){
        return this.telefono;
    }


}
