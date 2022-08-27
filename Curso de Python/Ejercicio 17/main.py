def main():
    
    
    def escribirArchivo(fichero,texto):
        f = open(fichero,'w')

        for txt in texto:
            if (txt.endswith('\n')):
                f.write(txt)
            else:
                newTxt = txt + '\n'
                f.write(newTxt)
        f.close()


    datos = ["Modulo 8","Entradas y salidas","Ejercicio 1"]

    escribirArchivo('archivo.txt',datos)

    def leerArchivo(fichero):
        f = open(fichero,'r')
        texto = f.read()
        f.close()
        return texto
    
    print(leerArchivo('archivo.txt'))


if __name__ == '__main__':
    main()