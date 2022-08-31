package com.exercices.interfaces;

import com.exercices.Coche;

public class MainImplements {
    public static void main(String[] args) {

        CocheService service1 = new CocheServiceSport();
        CocheService service2 = new CocheServiceClassicImpl();

        System.out.println(service1 + " " + service2);

        Coche coche1 = service1.crearCocheDemo();
        Coche coche2 = service2.crearCocheDemo();

        System.out.println(coche1 + "" + coche2);
    }
}
