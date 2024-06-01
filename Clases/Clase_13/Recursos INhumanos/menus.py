from input_paquete.input_func import *
import time
from os import system

def mostrar_opciones():
    opcion = get_int("Menú\n1. Ingresar empleado\n2. Modificar empleado\n"
                    "3. Eliminar empleado\n4. Mostrar a todos los empleados\n"
                    "5. Calcular salario promedio\n6. Buscar empleado por DNI\n"
                    "7. Ordenar empleados\n8. Salir del menú\n"
                    "Ingrese la opción que desea realizar: ",
                    "\nEsa opción no existe. Por favor, vuelva a ingresarla.\n", 1, 8,
                    "La opción no ha podido ser cargada.", 2)
    
    return opcion

def clear_and_wait():
    time.sleep(5)
    system("cls")

def ask_and_clear():
    input("Presione ENTER para continuar...")
    system("cls")