import pickle


class Vehiculo:
    nombre = None
    tipo = None

    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo


def main():

    v1 = Vehiculo("Juancito", "Auto")

    f = open('vehiculo1.bin', 'wb')
    pickle.dump(v1, f)
    f.close()

    fr = open('vehiculo1.bin', 'rb')
    v1_copy = pickle.load(fr)
    fr.close()

    print(v1_copy.nombre)
    print(v1_copy.tipo)


if __name__ == '__main__':
    main()
