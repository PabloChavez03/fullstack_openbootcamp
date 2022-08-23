public class App {
    public static void main(String[] args) {
        int result;
        result = suma(10,20, 30);

        Coche miCoche = new Coche();
        miCoche.incrementDoors();
        miCoche.incrementDoors();
        miCoche.incrementDoors();
        miCoche.incrementDoors();


        System.out.println(result);
        System.out.println(miCoche.doors);
    }

    public static int suma(int a, int b, int c) {
        return a + b + c;

    }

}

class Coche {
    public int doors = 0;

    public void incrementDoors() {
        this.doors++;
    }
}
