from alumno import *
from os import system

bandera = True

lista_alumnos = []

def mostrar_opciones():
    opcion = input("Menú\n1. Cargar\n2. Modificar\n3. Eliminar\n4. Mostrar\n5. Salir\nElija una opcion:\n")
    return opcion

system("cls")
while bandera:
    opcion = mostrar_opciones()
    match opcion:
        case "1":
            ingresar_alumno_lista(lista_alumnos)
        case "2":
            modificar_alumnos(lista_alumnos)
        case "3":
            eliminar_alumno(lista_alumnos, 46745279)
        case "4":
            mostrar_lista_alumnos(lista_alumnos)
        case "5":
            bandera = False
    system("pause")
    system("cls")