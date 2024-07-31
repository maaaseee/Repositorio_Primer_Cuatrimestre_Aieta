from input_paquete.input_func import *
import time
from os import system

def mostrar_opciones():
    opcion = get_int("¡Bienvenido a Recursos INHumanos!\n"
                    "1. Ingresar empleado\n"
                    "2. Modificar empleado\n"
                    "3. Eliminar empleado\n"
                    "4. Mostrar a todos los empleados\n"
                    "5. Calcular salario promedio\n"
                    "6. Buscar empleado por DNI\n"
                    "7. Ordenar empleados\n"
                    "8. Generar reporte de coincidencias según salarios\n"
                    "9. Generar reporte  de coincidencias segun apellido\n"
                    "10. Salir del menú\n"
                    "Ingrese la opción que desea realizar: ",
                    "\nEsa opción no existe. Por favor, vuelva a ingresarla.\n" , 1, 10,
                    "\nLa opción no ha podido ser cargada.\n", 2)
    
    return opcion

def clear_and_wait(tiempo: int):
    time.sleep(tiempo)
    system("cls")

def ask_and_clear():
    system("pause")
    system("cls")

def enviar_mensaje_error(error: int):
    match error:
        case 1:
            print("\nEl empleado no fue ingresado correctamente.")
        case 2:
            print("\nNo hay empleados en la lista. Por favor, antes de usar esta "
                "función, ingrese un empleado.\n")
        case 3:
            print("El ID no fue ingresado correctamente. Volviendo al menú...")
        case 4:
            print("El DNI no fue ingresado correctamente. Volviendo al menú...")
        case 5:
            print("No se pudo ordenar la lista.")
        case 6:
            print("\nNo se ha indicado si se desea realizar la modificacion"
                " Volviendo al menú...\n")
        case 7:
            print("No se pudo generar el reporte. Volviendo al menú...")