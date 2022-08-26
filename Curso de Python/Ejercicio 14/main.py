class Alumno:
    nombre = None
    calificacion = None

    def setNombre(self,nombre):
        self.nombre = nombre
    
    def setCalificacion(self,calificacion):
        self.calificacion = calificacion
    
    def getVeredicto(self):
        if (self.calificacion < 6 and self.calificacion > 0):
            return "El alumno desaprobo con la nota de " + str(self.calificacion)
        elif (self.calificacion >= 6 and self.calificacion <= 10):
            return "El alumno aprobo satisfactoriamente con la calificacion de " + str(self.calificacion)
        else:
            return "404"

a = Alumno()
a.setNombre("Pablo")
a.setCalificacion(10)

print(a.nombre)
print(a.calificacion)
print(a.getVeredicto())