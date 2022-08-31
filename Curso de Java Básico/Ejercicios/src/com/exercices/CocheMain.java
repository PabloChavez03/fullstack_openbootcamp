package com.exercices;

public class CocheMain {
    public static void main(String[] args) {

        Coche miCoche = new Coche("Verde","Toyota","Corolla", 1000.10,5.10);
        Coche suCoche = new Coche();

        miCoche.acelerar(120);
        System.out.println(miCoche);
        System.out.println(suCoche);

        CocheElectrico electrico = new CocheElectrico("SamsungElectric");
        System.out.println();

    }
}
