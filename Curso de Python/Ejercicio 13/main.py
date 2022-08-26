class Vehiculo:
    color = None
    ruedas = None
    puertas = None
    def __init__(self,color,ruedas,puertas):
        self.color = color
        self.puertas = puertas
        self.ruedas = ruedas

class Coche(Vehiculo):
    velocidad = None
    cilindrada = None
    def __init__(self,velocidad,cilindrada,puertas,ruedas,color):
        super().__init__(color,ruedas,puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

c = Coche(120,50,4,4,"Rojo")

print("Velocidad:",c.velocidad)
print("Cilindrada:",c.cilindrada)
print("Puertas:",c.puertas)
print("Ruedas:",c.ruedas)
print("Color:",c.color)


