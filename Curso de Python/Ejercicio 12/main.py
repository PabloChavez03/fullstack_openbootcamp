def bisiesto(numero):
    if(numero % 4 == 0 and type(numero) == int):
        return 'Es año bisiesto'
    return 'No es bisiesto'

print(bisiesto(2024))