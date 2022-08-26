import math

def areaTriangulo(base,altura):
    return int((base*altura)/2)

def areaCirculo(radio):
    resultado = (math.pi * radio**2)
    return round(resultado,2)

print(areaTriangulo(2,12))
print(areaCirculo(10))