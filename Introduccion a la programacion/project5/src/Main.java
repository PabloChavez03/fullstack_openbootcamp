public class Main {
    public static void main(String[] args) {
        System.out.println("Hola perrin");
        factorial(5);
    }

    public static int factorial(int numero) {
        int resultado;
        if (numero == 1) {
            return 1;
        }
        resultado = factorial(numero - 1 ) * numero;

        return resultado;
    }
}
