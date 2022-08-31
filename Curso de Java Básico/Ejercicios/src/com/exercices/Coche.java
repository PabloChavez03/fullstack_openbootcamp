package com.exercices;

public class Coche {
    //atributos
    String color;
    String fabricante;
    String modelo;
    Double peso;
    Double largo;
    Integer velocidad;

    //constructores
    public Coche(){}
    public Coche(String color, String fabricante, String modelo, Double peso, Double largo){
        this.color = color;
        this.largo = largo;
        this.fabricante = fabricante;
        this.modelo = modelo;
        this.peso = peso;
    }

    public void acelerar(Integer velocidad){
        this.velocidad = velocidad;
    }

    @Override
    public String toString() {
        return "Coche{" +
                "color='" + color + '\'' +
                ", fabricante='" + fabricante + '\'' +
                ", modelo='" + modelo + '\'' +
                ", peso=" + peso +
                ", largo=" + largo +
                ", velocidad=" + velocidad +
                '}';
    }
}
