from input_paquete.input_func import *
from dict_paquete.funciones import *
import math
from menus import *
from os import system

puestos_de_trabajo = ["Gerente", "Supervisor", "Analista", "Encargado", "Asistente"]
violeta = "\033[0;35m"
reset = "\033[0m"

# region Crear_empleado
# - 1 ------------------------------------------------------------------------------------------------------ #
def crear_empleado(id: int, nombre: str, apellido: str, dni: int, puesto: str,
                    salario: int) -> dict:
    # Crea un diccionario con los datos otorgados del empleado
    diccionario_empleado = {
        "ID" : id,
        "Nombre" : nombre,
        "Apellido" : apellido,
        "DNI" : dni,
        "Puesto" : puesto,
        "Salario" : salario
    }

    return diccionario_empleado

def solicitar_dato(tipo_de_dato: str):
    match tipo_de_dato:
        case "Nombre":
            dato = get_string("Ingrese el nombre: ", 1, 20,
                            "El nombre ingresado no es válido", 3)
        case "Apellido":
            dato = get_string("Ingrese el apellido: ", 1, 20,
                                "El apellido ingresado no es válido", 3)
        case "DNI":
            dato = get_int("Ingrese su dni: ", "El DNI ingresado no es válido."
                " Por favor, vuelva a ingresarlo.", 5000000, 99999999,
                "El DNI ingresado no es válido", 3)
        case "Puesto":
            dato = get_string_excluyente("Ingrese su puesto: ", 5, 9, 
                        puestos_de_trabajo, "El puesto ingresado no es válido", 3)
        case "Salario":
            dato = get_int("Ingrese su salario: ", "El salario ingresado no es válido."
                        " Por favor, vuelva a ingresarlo.",
                        234315, math.inf, "El salario ingresado no es válido.", 3)
        case "ID":
            dato = get_int("Ingrese su ID: ", "El ID ingresado no es válido. Por favor, "
                        "vuelva a ingresarlo.", 1, 1000, "\n", 3)
    
    return dato

def ingresar_empleado_lista(lista_empleados: list[dict], last_id: int) -> bool:
    # Solicita todos los datos para rellenar en un diccionario, y los agrega a una lista
    # Usa funciones de "input_paquete"
    id = last_id + 1
    bandera = True

    nombre = solicitar_dato("Nombre")
    if nombre == None:
        bandera = False
    
    apellido = solicitar_dato("Apellido")
    if apellido == None:
        bandera = False
    
    dni = solicitar_dato("DNI")
    if dni == None:
        bandera = False

    puesto = solicitar_dato("Puesto")
    if puesto == None:
        bandera = False

    salario = solicitar_dato("Salario")
    if salario == None:
        bandera = False

    diccionario_empleado = crear_empleado(id, nombre, apellido, dni, puesto, salario)

    mostrar_empleado(diccionario_empleado)

    lista_empleados.append(diccionario_empleado)
    print("\nEl empleado fue ingresado exitosamente.\n")

    return bandera

# endregion

# region Modificar_empleado
# - 2 ------------------------------------------------------------------------------------------------------ #

def modificar_empleado(lista_empleados: list[dict]) -> bool|dict:
    # Solicita el ID del empleado a modificar
    # Se le pregunta al usuario cual es la key que desea modificar
    # Ademas, se le pregunta al usuario si está seguro de que desea modificar ese dato.
    # Usa funciones de "input_paquete"
    keys_lista = conseguir_keys(lista_empleados[0])
    bandera_modificacion = True

    system("cls")
    ingreso_id = solicitar_dato("ID")
    
    if ingreso_id == None:
        enviar_mensaje_error(3)
    else:
        bandera_modificacion = menu_modificaciones(lista_empleados, ingreso_id, keys_lista,
                                                    "ID", bandera_modificacion)

    return bandera_modificacion

def menu_modificaciones(lista: list[dict], id: int ,keys: list, key: str , bandera: bool):
    verde = "\033[0;32m"
    reset = "\033[0m"
    opciones = f"{verde}\n- Apellido\n- Nombre\n- DNI\n- Puesto\n- Salario\n{reset}"
    for i in range(len(lista)):
        if lista[i][key] == id:
            eleccion = get_string_excluyente(f"{opciones}Ingrese el dato a modificar: ",
                                            1, 10, keys, "\n", 3)
            if eleccion == None:
                bandera = False
                break
            eleccion = eleccion.capitalize()

            auxiliar = armar_auxiliar_diccionario(lista[i], keys)

            empleado_modificado = modificar_empleado_opciones_keys(eleccion, lista[i])
            if empleado_modificado == False:
                bandera = False
                break
            
            print(f"Desea modificar el dato de {eleccion} del siguiente empleado:")
            mostrar_empleado(auxiliar)
            print("Y cambiarlo por:")
            mostrar_empleado(empleado_modificado)

            segunda_eleccion = confirmar_eleccion(f"Ingrese SI/NO si desea cambiar el dato del empleado:\n",
                                                lista[i], empleado_modificado, auxiliar)
            if segunda_eleccion == False:
                bandera = False
            break

    return bandera

def modificar_item(diccionario: dict, key: str, modificacion) -> bool:
    if modificacion == None:
        diccionario = False
    else:
        diccionario[key] = modificacion

    return diccionario

def modificar_empleado_opciones_keys(eleccion_mayus: str, empleado_modificado):
    # Compara la eleccion, con las keys del diccionario
    # Se reemplaza el dato original, con el dato nuevo
    # Usa funciones de "input_paquete"
    match eleccion_mayus:
        case "Apellido":
            apellido = solicitar_dato("Apellido")
            empleado_modificado = modificar_item(empleado_modificado, "Apellido", apellido)
        
        case "Nombre":
            nombre = solicitar_dato("Nombre")
            empleado_modificado = modificar_item(empleado_modificado, "Nombre", nombre)

        case "Dni":
            dni = solicitar_dato("DNI")
            empleado_modificado = modificar_item(empleado_modificado, "DNI", dni)
        
        case "Puesto":
            puesto = solicitar_dato("Puesto")
            empleado_modificado = modificar_item(empleado_modificado, "Puesto", puesto)
        
        case "Salario":
            salario = solicitar_dato("Salario")
            empleado_modificado = modificar_item(empleado_modificado, "Salario", salario)
    
    return empleado_modificado
# endregion

# region Eliminar_empleado
# - 3 ------------------------------------------------------------------------------------------------------ #

def eliminar_empleado(lista_empleados: list[dict], lista_despedidos: list[dict], key: str) -> bool:
    # Solicita el ID del empleado a eliminar
    # Verifica si realmente desea eliminar al empleado
    ingreso_id = solicitar_dato("ID")

    if ingreso_id == None:
        enviar_mensaje_error(3)
    else:
        for empleado in lista_empleados:
            if empleado[key] == ingreso_id:
                mostrar_empleado(empleado)
                despedido = None
                despedido = confirmar_eleccion(f"Ingrese SI/NO si desea eliminar al empleado:\n",
                                                despedido, 1, 2)
                
                if despedido == 1:
                    lista_despedidos.append(empleado)
                    lista_empleados.remove(empleado)
                break
#endregion

# region Mostrar_lista_empleados
# - 4 ------------------------------------------------------------------------------------------------------ #

def mostrar_cabecera_lista():
    verde = "\033[38;5;22m"
    print(f"+{"-"*3}+{"-"*20}+{"-"*20}+{"-"*9}+{"-"*14}+{"-"*14}+")

    print(f"| {verde}ID{reset}|{" "*14}{verde}Nombre{reset}|{" "*12}{verde}Apellido{reset}|"
        f"{" "*6}{verde}DNI{reset}|{" "*8}{verde}Puesto{reset}|{" "*7}{verde}Salario{reset}|")
    
    print(f"+{"-"*3}+{"-"*20}+{"-"*20}+{"-"*9}+{"-"*14}+{"-"*14}+")

def mostrar_empleado(un_empleado: dict):
    # Muestra a uno solo de los empleados, con un formato de tabla
    mostrar_cabecera_lista()

    print(f"| {un_empleado["ID"]}|{un_empleado["Nombre"]:>20}|{un_empleado["Apellido"]:>20}"
        f"|{un_empleado["DNI"]:>9}|{un_empleado["Puesto"]:>14}|${un_empleado["Salario"]:>13.0f}|")
    print("+---+--------------------+--------------------+---------+--------------+--------------+")

def mostrar_lista_empleados(lista_empleados: list[dict]):
    # Crea una lista con formato de tabla para mostrar a todos los empleados
    verde = "\033[38;5;22m"

    mostrar_cabecera_lista()
    for empleado in lista_empleados:
        id = empleado["ID"]
        nombre = empleado["Nombre"]
        apellido = empleado["Apellido"]
        dni = empleado["DNI"]
        puesto = empleado["Puesto"]
        salario = empleado["Salario"]
        signo_pesos = f"{verde}${reset}"

        mostrar = "|{:>3}|{:>20}|{:>20}|{:>9}|{:>14}|{:}{:>13.0f}|".format(id, nombre, apellido, dni, puesto, signo_pesos, salario)
        print(mostrar)
        print(f"+{"-"*3}+{"-"*20}+{"-"*20}+{"-"*9}+{"-"*14}+{"-"*14}+")
# endregion

# region Calcular_promedio_salarios
# - 5 ------------------------------------------------------------------------------------------------------ #

def calcular_promedio_key(lista_empleados:list[dict], key: str):
    # Calcula el promedio de una key de la lista de empleados
    acumulador = 0
    for empleado in lista_empleados:
        acumulador += empleado[key]

    promedio = acumulador / len(lista_empleados)
    return promedio
#endregion

# region Buscar_empleado_por_dni
# - 6 ------------------------------------------------------------------------------------------------------ #

def buscar_empleado_por_dni(lista_empleados: list[dict]):
    # Busca a un empleado por su DNI y lo muestra
    solicitar_dni = solicitar_dato("DNI")
    if solicitar_dni == None:
        enviar_mensaje_error(4)
    else:
        for empleado in lista_empleados:
            if empleado["DNI"] == solicitar_dni:
                mostrar_empleado(empleado)
                break
#endregion

# region Ordenar_lista_empleados
# - 7 ------------------------------------------------------------------------------------------------------ #

def ordenar_lista_empleados(lista_empleados: list[dict]):
    # Ordena la lista de empleados según el criterio elegido por el usuario
    # Debe ingresar el nombre de la llave a ordenar, y si es de Menor a mayor, o Mayor a menor
    verde = "\033[0;32m"
    keys_lista = conseguir_keys(lista_empleados[0])
    opciones = f"{verde}\n- Apellido\n- Nombre\n- Salario\n{reset}"

    eleccion = get_string_excluyente(f"{opciones}Ingrese el dato con el que desea"
                                    f" ordenar la lista: ",
                                    1, 10, keys_lista,
                                    "El dato ingresado no es válido", 3)
    
    if eleccion == None:
        print("El dato ingresado no es válido para ordenar la lista")
    else:
        if eleccion == "Apellido":
            ordenar_con_criterio_key(eleccion, lista_empleados)

        elif eleccion == "Nombre":
            ordenar_con_criterio_key(eleccion, lista_empleados)

        elif eleccion == "Salario":
            ordenar_con_criterio_key(eleccion, lista_empleados)

def ordenar_con_criterio_key(key: str, lista: list[dict]):
    # Ordena la lista de empleados según el criterio de orden (Menor a mayor = 1/ Mayor a menor = 2)
    orden_de_lista = get_int(f"¿Como desea ordenar la lista?\n{violeta}1. Menor a mayor\n"
                                    f"2. Mayor a menor{reset}\nElegir el número: ",
                                    "ERROR. Por favor, vuelva a elegir una opción",
                                    1, 2, "No se pudo realizar la operacion solicitada", 3)
    if orden_de_lista == 1:
        ordenar_lista_segun_orden(lista, key, orden_de_lista)
        mostrar_lista_empleados(lista)
    elif orden_de_lista == 2:
        ordenar_lista_segun_orden(lista, key, orden_de_lista)
        mostrar_lista_empleados(lista)
    else:
        enviar_mensaje_error(5)

#endregion