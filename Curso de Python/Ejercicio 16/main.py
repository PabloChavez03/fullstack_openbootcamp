from time import localtime
from alarma import alarma

def main():

    _, _, _, hora, minutos, segundos, _, _, _ = localtime()

    print(alarma(hora, minutos, segundos))


if __name__ == '__main__':
    main()