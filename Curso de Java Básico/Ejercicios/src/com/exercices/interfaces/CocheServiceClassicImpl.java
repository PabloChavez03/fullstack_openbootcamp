package com.exercices.interfaces;

import com.exercices.Coche;
import com.exercices.CocheElectrico;
import com.exercices.interfaces.CocheService;

public class CocheServiceClassicImpl implements CocheService {

    @Override
    public Coche crearCocheDemo() {
        System.out.println("Creando coche clasico");
        return new Coche();
    }
}
