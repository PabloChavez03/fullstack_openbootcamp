public class App {
    public static void main(String[] args){
        Persona miPersona = new Persona();
        miPersona.setEdad(25);
        miPersona.setNombre("Pablo");
        miPersona.setTelefono("+5493442654108");

        int edad = miPersona.getEdad();
        String nombre = miPersona.getNombre();
        String telefono = miPersona.getTelefono();

        System.out.println("Nombre: " + nombre + " " + "Edad: " + edad + " " + "Telefono: " + telefono);
    }
}

class Persona {
    private int edad;
    private String nombre;
    private String telefono;

    public void setEdad(int edad) {
        this.edad = edad;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }
    public int getEdad() {
        return this.edad;
    }
    public String getNombre() {
        return this.nombre;
    }
    public String getTelefono() {
        return this.telefono;
    }
}