from input_paquete.input_func import *
import time
from os import system

def mostrar_opciones():
    opcion = get_int("¡Bienvenido a Vidda!\n"
                    "1. Ingresar paciente\n"
                    "2. Modificar paciente\n"
                    "3. Eliminar paciente\n"
                    "4. Mostrar a todos los pacientes\n"
                    "5. Ordenar pacientes\n"
                    "6. Buscar paciente por DNI\n"
                    "7. Calcular promedios\n"
                    "8. Determinar compatibilidad\n"
                    "9. Salir del menú (Esto guarda todas las modificaciones)\n"
                    "Ingrese la opción que desea realizar: ",
                    "\nEsa opción no existe. Por favor, vuelva a ingresarla.\n" , 1, 9,
                    "\nLa opción no ha podido ser cargada.\n", 0)
    
    return opcion

def clear_and_wait(tiempo: int):
    """_summary_
    Limpia la terminal luego de transcurrir el tiempo asignado.

    Args:
        tiempo (int): Tiempo a transcurrir
    """
    time.sleep(tiempo)
    system("cls")

def ask_and_clear():
    """_summary_
    Pregunta al usuario si desea continuar, y limpia la terminal.
    """
    system("pause")
    system("cls")

def enviar_mensaje_error(error: int) -> str:
    """_summary_

    Args:
        error (int): Numero con el error a mostrar
    Returns:
    str: El error que se encontró en el funcionamiento del programa
    """
    match error:
        case 1:
            print("\nEl paciente no fue ingresado correctamente.")
        case 2:
            print("\nNo hay pacientes en la lista. Por favor, antes de usar esta "
                "función, ingrese a un paciente.\n")
        case 3:
            print("El ID no fue ingresado correctamente. Volviendo al menú...\n")
        case 4:
            print("El DNI no fue ingresado correctamente. Volviendo al menú...\n")
        case 5:
            print("No se pudo ordenar la lista.")
        case 6:
            print("\nNo se ha indicado si se desea realizar la modificacion."
                " Volviendo al menú...\n")
        case 7:
            print("No se pudo generar el reporte. Volviendo al menú...")
        case 8:
            print("El dato ingresado no es válido para calcular el promedio")
        case 9:
            print("El dato ingresado no es válido para ordenar la lista")
        case 10:
            print("Se encontró una falla en la solicitud de datos. Volviendo al menú...")
        case 11:
            print("No existe un empleado con ese mismo DNI. Volviendo al menú...")

def salir_del_programa(eleccion: str, bandera: bool):
    """_summary_
    Concreta la salida del programa, o la cancela.

    Args:
        eleccion (str): Eleccion que llega a la funcion
        bandera (bool): Bandera a cambiar, segun la eleccion

    Returns:
        bool: Bandera en False, en caso de salir del programa
    """
    if eleccion == "SI":
        bandera = False
        print("\nSaliendo del programa...")
        clear_and_wait(3)
    elif eleccion == "NO":
        system("pause")
        system("cls")
    else:
        for _ in range(2):
            eleccion_empleado = input("Ingrese SI/NO si desea salir:\n").upper()
            if eleccion_empleado == "SI":
                bandera = False
                print("\nSaliendo del programa...")
                clear_and_wait(3)
            elif eleccion_empleado == "NO":
                system("pause")
                system("cls")

    return bandera

def crear_submenus(keys: list, color: str):
    """_summary_
    Crea un submenú con sus respectivo color.

    Args:
        keys (list): Llaves para crear submenú
        color (str): Color para los datos mostrados.

    Returns:
        str: Una cadena con un submenú armado
    """
    string = f"{color}"
    for i in range(len(keys)):
        if i + 1 == len(keys):
            string += f"- {keys[i]}"
        else:
            string += f"- {keys[i]}\n"
    string += f"{reset}"

    return string