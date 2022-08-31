package com.exercices.interfaces;

import com.exercices.Coche;
import com.exercices.CocheElectrico;

public class CocheServiceSport implements CocheService{

    @Override
    public Coche crearCocheDemo() {
        System.out.println("Creando coche de carreas");
        return new CocheElectrico();
    }
}
