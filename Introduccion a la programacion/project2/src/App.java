public class App {
    public static void main(String[] args) {
        isTrueOrFalse(0);
        isMinorAThree(-10);
        isDoWhile(1);
        isForNumber();
        isSwitchCase("Primavera");
    }

    public static void isTrueOrFalse(int numero) {
        if (numero > 0) {
            System.out.println("Es positivo");
        } else if (numero < 0) {
            System.out.println("Es negativo");
        } else {
            System.out.println("Es igual a cero");
        }
    }

    public static void isMinorAThree (int numero) {
        while (numero < 3 ) {
            System.out.println(numero);
            numero++;
        }
        System.out.println("El numero es igual o mayor a tres");
    }

    public static void isDoWhile (int numero) {
        do {
            System.out.println(numero);
            numero = 3;
        } while (numero < 3);
    }

    public static void isForNumber () {
        for (int numero = 0; numero <= 3; numero++) {
            System.out.println(numero);
        }
    }

    public static void isSwitchCase (String estacion) {
        switch (estacion) {
            case "Otoño" -> System.out.println("Es otoño");
            case "Invierno" -> System.out.println("Es invierno");
            case "Primavera" -> System.out.println("Es primavera");
            case "Verano" -> System.out.println("Es verano");
            default -> System.out.println("No ingresaste una estacion valida");
        }
    }
}