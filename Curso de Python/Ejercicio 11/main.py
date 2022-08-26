def isPrimo(numero):
    if(numero == 1 and type(numero) == int):
        return 'Es primo'
    
    for i in range(2,numero):
        if (numero % i == 0 and type(numero) == int):
            return 'No es primo'
    return 'Es primo'

        
            

print(isPrimo(89))
