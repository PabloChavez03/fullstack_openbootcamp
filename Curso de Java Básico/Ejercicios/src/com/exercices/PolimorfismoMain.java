package com.exercices;

public class PolimorfismoMain {
    public static void main(String[] args) {

        Coche cochesin = new Coche();
        CocheElectrico electricCochesin = new CocheElectrico();

        // polimorfismo

        Coche cochesinPoli = new CocheElectrico();
    }
}
