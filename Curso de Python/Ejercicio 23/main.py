from getpass import getpass
from importlib.machinery import all_suffixes
import sqlite3

alumnos = [(1,"Pablo","Chavez"),(2,"Victor","Roman"),(3,"Oscar","Silva"),(4,"Angela","Rodriguez"),(5,"Matias","Antunez"),(6,"Llamil","Chanta"),(7,"Brayan","Ceron"),(8,"Carlos","Espinosa")]

def main():
    for alumno in alumnos:
        id,nombre,apellido = alumno
        print(insertarAlumnos(id,nombre,apellido))
    
    print(getAlumno("Brayan"))


def insertarAlumnos(id,nombre,apellido):
    conn = sqlite3.connect('alumnos.db', isolation_level=None)
    cursor = conn.cursor()

    querySelect = f'SELECT * FROM alumnos WHERE id={id}'
    rows = cursor.execute(querySelect)
    data = rows.fetchone()

    if(type(data)):
        return "El alumno ya existe"

    query = '''INSERT INTO alumnos(id,nombre,apellido) VALUES(?,?,?)'''
    cursor.execute(query, (id,nombre,apellido))

    

    cursor.close()
    conn.close()

    return "Alumno insertado"



def getAlumno(nombre):
    conn = sqlite3.connect('alumnos.db')
    cursor = conn.cursor()

    query = f'SELECT * FROM alumnos WHERE nombre="{nombre}"'

    rows = cursor.execute(query)
    data = rows.fetchone()

    cursor.close()
    conn.close()

    if (type(data) == None):
        return "El alumno no existe o no ha sido agregado"
    else:
        return data


if __name__ == '__main__':
    main()