from functools import reduce

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

resLista = list(filter(lambda x: x % 2 != 0, lista)) # impares
resultado = reduce(lambda a,b: a + b, resLista)

print(resultado)