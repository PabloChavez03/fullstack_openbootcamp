public class Main {
    public static void main(String[] args) {
        Cliente client = new Cliente(25,"Pablo","3446654108");
        client.setCredito(2000);
        System.out.println("Nombre: " + client.nombre + " Edad: " + client.edad + " Telefono: " + client.telefono + " Credito: " + client.getCredito());

        Trabajador empleado = new Trabajador(30, "Sofia", "4231231323");
        empleado.setSalario(40000);
        System.out.println("Nombre: " + empleado.nombre + " Edad: " + empleado.edad + " Telefono: " + empleado.telefono + " Salario: " + empleado.getSalario());
    }
}

class Persona {
    public int edad;
    public String nombre;
    public String telefono;
}

class Cliente extends Persona {
    private int credito;

    public Cliente(int edad, String nombre, String telefono){
        this.edad = edad;
        this.nombre = nombre;
        this.telefono = telefono;
    }

    public void setCredito(int credito) {
        this.credito = credito;
    }

    public int getCredito(){
        return this.credito;
    }
}

class Trabajador extends Persona {
    private int salario;

    public Trabajador(int edad, String nombre, String telefono){
        this.edad = edad;
        this.nombre = nombre;
        this.telefono = telefono;
    }

    public void setSalario(int salario){
        this.salario = salario;
    }
    public int getSalario(){
        return this.salario;
    }

}