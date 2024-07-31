from input_paquete.input_func import *
from dict_paquete.funciones import *
from menus import *
import math
import json
from datetime import date

puestos_de_trabajo = ["Gerente", "Supervisor", "Analista", "Encargado", "Asistente"]
violeta = "\033[0;35m"
reset = "\033[0m"

# region Archivos
def parser_csv(path: str, lista: list):
    with open(path, 'r', encoding="utf8") as archivo:
        next(archivo)
        for linea in archivo:
            registro = separar_string_csv(linea)
            id = int(registro[0])
            nombre = registro[1]
            apellido = registro[2]
            dni = int(registro[3])
            puesto = registro[4]
            salario = int(registro[5])
            diccionario = crear_empleado(id, nombre, apellido, dni, puesto, salario)
            lista.append(diccionario)

def extract_config_json(path):
    try:
        with open(path, 'r', encoding='utf-8') as archivo:
            data = json.load(archivo)
        extraccion = [data["config"]]
        lista = [extraccion[0]]
        return lista

    except FileNotFoundError:
        with open(path, 'w', encoding="utf-8") as archivo:
            data = {}
            data["config"] = {"last_id": 0,
                            "bajas": 0,
                            "reportes_salario": 0,
                            "reportes_apellidos": 0}
            json.dump(data, archivo, indent= 4)
            return data["config"]

def get_last_id(lista):
    maximo = 0
    for dato in lista:
        if dato["ID"] > maximo:
            maximo = dato["ID"]

    return maximo

def overwrite_json(path: str, diccionario: dict):
    with open(path, "r", encoding="utf-8") as archivo:
        data = json.load(archivo)
    
    data["config"] = diccionario

    with open(path, "w", encoding="utf-8") as archivo:
        json.dump(data, archivo, indent= 4)

def separar_string_csv(linea: str) -> list:
    salto_de_linea = linea.strip("\n")
    lista = salto_de_linea.split(",")

    return lista

def overwrite_csv(path: str, lista: list[dict]):
    with open(path, 'w', encoding="utf8") as archivo:
        archivo.write("ID,Nombre,Apellido,DNI,Puesto,Salario\n")
        for i in range(len(lista)):
            if i != len(lista) - 1:
                string = (f"{lista[i]["ID"]},{lista[i]["Nombre"]},{lista[i]["Apellido"]},"
                    f"{lista[i]["DNI"]},{lista[i]["Puesto"]},{lista[i]["Salario"]}\n")
            else:
                string = (f"{lista[i]["ID"]},{lista[i]["Nombre"]},{lista[i]["Apellido"]},"
                        f"{lista[i]["DNI"]},{lista[i]["Puesto"]},{lista[i]["Salario"]}")
            
            archivo.write(string)

def copy_json(path: str, path_2: str):
    try:
        with open(path, 'r', encoding='utf-8') as archivo:
            data = json.load(archivo)
        data = "\n" + data

        with open(path_2, 'a', encoding='utf-8') as archivo:
            json.dump(data, archivo, indent= 4)
    except FileNotFoundError:
        with open(path_2, 'w', encoding='utf-8') as archivo:
            json.dump(data, archivo, indent= 4)

def create_bajas_json(path: str, lista: dict):
    try:
        with open(path, "r", encoding='utf-8') as archivo:
            data = json.load(archivo)
        data = data + "\n" + lista

        with open(path, 'a', encoding='utf-8') as archivo:
            json.dump(data, archivo, indent= 4)
    except FileNotFoundError:
        with open(path, "w", encoding="utf-8") as archivo:
            json.dump(lista, archivo, indent=4)

# endregion

# region Crear empleado
# - 1 ------------------------------------------------------------------------------------------------------ #
def crear_empleado(id: int, nombre: str, apellido: str, dni: int, puesto: str,
                    salario: int) -> dict:
    diccionario_empleado = {
        "ID" : id,
        "Nombre" : nombre,
        "Apellido" : apellido,
        "DNI" : dni,
        "Puesto" : puesto,
        "Salario" : salario
    }

    return diccionario_empleado

def solicitar_dato(tipo_de_dato: str) -> int|str|bool:
    # El parámetro solicita que tipo de dato se va a pedir al usuario
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
                "\n", 3)
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

def ingresar_empleado_lista(lista_empleados: list[dict], last_id) -> bool|int:
    # Solicita todos los datos para rellenar en un diccionario, y los agrega a una lista
    # Usa funciones de "input_paquete"
    bandera = True

    nombre = solicitar_dato("Nombre")
    if nombre == None:
        bandera = False

    else:
        apellido = solicitar_dato("Apellido")
        if apellido == None:
            bandera = False

        else:
            dni = solicitar_dato("DNI")
            if dni == None:
                bandera = False

            else:
                puesto = solicitar_dato("Puesto")
                if puesto == None:
                    bandera = False
                
                else:
                    salario = solicitar_dato("Salario")
                    if salario == None:
                        bandera = False
    
    if bandera == True:
        id = last_id + 1
        diccionario_empleado = crear_empleado(id, nombre, apellido, dni, puesto, salario)

        mostrar_empleado(diccionario_empleado)

        lista_empleados.append(diccionario_empleado)
        print("\nEl empleado fue ingresado exitosamente.\n")

        bandera = id
    
    return bandera

# endregion

# region Modificar empleado
# - 2 ------------------------------------------------------------------------------------------------------ #

def modificar_empleado(lista_empleados: list[dict]) -> bool|dict:
    # Solicita el ID del empleado a modificar
    # Se le pregunta al usuario cual es la key que desea modificar
    # Ademas, se le pregunta al usuario si está seguro de que desea modificar ese dato.
    # Usa funciones de "input_paquete" y "dict_paquete"
    keys_lista = conseguir_keys(lista_empleados)
    bandera_modificacion = True

    system("cls")
    ingreso_id = solicitar_dato("ID")
    
    if ingreso_id == None:
        enviar_mensaje_error(3)
    else:
        bandera_modificacion = menu_modificaciones(lista_empleados, ingreso_id, keys_lista,
                                                    "ID", bandera_modificacion)

    return bandera_modificacion

def menu_modificaciones(lista: list[dict], id: int ,lista_keys: list, key: str , bandera: bool):
    verde = "\033[0;32m"
    opciones = f"{verde}\n- Apellido\n- Nombre\n- DNI\n- Puesto\n- Salario\n{reset}"

    coincidencia_empleado = buscar_dato(lista, key, id, 2)
    bandera = True
    if coincidencia_empleado != None:
        eleccion = get_string_excluyente(f"{opciones}Ingrese el dato a modificar: ",
                                        1, 10, lista_keys, "\n", 3)
        if eleccion == None:
            bandera = False
        eleccion = eleccion.capitalize()

        auxiliar = armar_auxiliar_diccionario(coincidencia_empleado, lista_keys)

        empleado_modificado = modificar_empleado_opciones_keys(eleccion, coincidencia_empleado)
        if empleado_modificado == False:
            bandera = False
        
        print(f"Desea modificar el dato de {eleccion} del siguiente empleado:")
        mostrar_empleado(auxiliar)
        print("Y cambiarlo por:")
        mostrar_empleado(empleado_modificado)

        segunda_eleccion = confirmar_eleccion(f"Ingrese SI/NO si desea cambiar el dato del empleado:\n",
                                            coincidencia_empleado, empleado_modificado, auxiliar)
        if segunda_eleccion == False:
            bandera = False

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

# region Eliminar empleado
# - 3 ------------------------------------------------------------------------------------------------------ #

# def bajas_json(path: str, despedido: dict, numero):
#     # Se guarda al empleado dado de baja en un archivo .json
#     # Si el archivo no existe, se crea uno nuevo
#     bandera = True
#     try:
#         with open(path, "r") as archivo:
#             data = json.load(archivo)
#         data[f"baja{numero}"] = [despedido]
    
#     except FileNotFoundError:
#         diccionario = despedido
#         lista = [diccionario]
#         data = {f"baja{numero}": lista}

#     except json.JSONDecodeError:
#         data = {}
#         data[f"baja{numero}"] = [despedido]

#     with open(path, "w") as archivo:
#             json.dump(data, archivo, indent=4)

#     return bandera

def eliminar_empleado(lista_empleados: list[dict], key: str, bajas: int, bajas_lista: list) -> int|bool:
    # Solicita el ID del empleado a eliminar
    # Verifica si realmente desea eliminar al empleado
    ingreso_id = solicitar_dato("ID")
    baja = False

    if ingreso_id == None:
        enviar_mensaje_error(3)
    else:
        empleado = buscar_dato(lista_empleados, key, ingreso_id, 2)
        if empleado != []:
            mostrar_empleado(empleado)
            despedido = None
            despedido = confirmar_eleccion(f"Ingrese SI/NO si desea eliminar al empleado:\n",
                                            despedido, 1, 2)
            
            if despedido == 1:
                lista_empleados.remove(empleado)
                bajas_lista.append(empleado)


        else:
            print("\nNo se encontró un empleado con la ID ingresada\n")

    return baja
#endregion

# region Mostrar lista de empleados
# - 4 ------------------------------------------------------------------------------------------------------ #

def mostrar_cabecera_lista():
    verde = "\033[38;5;22m"
    print(f"+{"-"*4}+{"-"*20}+{"-"*20}+{"-"*9}+{"-"*14}+{"-"*14}+")

    print(f"|  {verde}ID{reset}|{" "*14}{verde}Nombre{reset}|{" "*12}{verde}Apellido{reset}|"
        f"{" "*6}{verde}DNI{reset}|{" "*8}{verde}Puesto{reset}|{" "*7}{verde}Salario{reset}|")
    
    print(f"+{"-"*4}+{"-"*20}+{"-"*20}+{"-"*9}+{"-"*14}+{"-"*14}+")

def mostrar_empleado(un_empleado: dict):
    # Muestra a uno solo de los empleados, con un formato de tabla
    mostrar_cabecera_lista()

    print(f"|{un_empleado["ID"]:>4}|{un_empleado["Nombre"]:>20}|{un_empleado["Apellido"]:>20}"
        f"|{un_empleado["DNI"]:>9}|{un_empleado["Puesto"]:>14}|${un_empleado["Salario"]:>13.0f}|")
    print(f"+{"-"*4}+{"-"*20}+{"-"*20}+{"-"*9}+{"-"*14}+{"-"*14}+")

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

        mostrar = "|{:>4}|{:>20}|{:>20}|{:>9}|{:>14}|{:}{:>13.0f}|".format(id, nombre, apellido, dni, puesto, signo_pesos, salario)
        print(mostrar)
        print(f"+{"-"*4}+{"-"*20}+{"-"*20}+{"-"*9}+{"-"*14}+{"-"*14}+")
# endregion

# region Calcular promedio de salarios
# - 5 ------------------------------------------------------------------------------------------------------ #

def calcular_promedio_key(lista_empleados:list[dict], key: str) -> float:
    # Calcula el promedio de una key de la lista de empleados
    acumulador = 0
    for empleado in lista_empleados:
        acumulador += empleado[key]

    promedio = acumulador / len(lista_empleados)
    return promedio
#endregion

# region Buscar empleado por DNI
# - 6 ------------------------------------------------------------------------------------------------------ #

def buscar_por_dni(lista_empleados: list[dict]) -> dict:
    # Busca a un empleado por su DNI y lo muestra
    ingreso_dni = solicitar_dato("DNI")
    if ingreso_dni == None:
        enviar_mensaje_error(4)
    else:
        empleado = buscar_dato(lista_empleados, "DNI", ingreso_dni, 2)
        if empleado == None:
            enviar_mensaje_error(1)
        mostrar_empleado(empleado)
#endregion

# region Ordenar lista de empleados
# - 7 ------------------------------------------------------------------------------------------------------ #

def ordenar_lista(lista_empleados: list[dict]) -> list[dict]:
    # Ordena la lista de empleados según el criterio elegido por el usuario
    # Debe ingresar el nombre de la llave a ordenar, y si es de Menor a mayor, o Mayor a menor
    verde = "\033[0;32m"
    keys_lista = conseguir_keys(lista_empleados)
    opciones = f"{verde}- Apellido\n- Nombre\n- Salario\n{reset}"
    auxiliar = armar_auxiliar_lista(lista_empleados)

    # system("cls")
    eleccion = get_string_excluyente(f"{opciones}Ingrese el dato con el que desea"
                                    f" ordenar la lista: ",
                                    1, 10, keys_lista,
                                    "El dato ingresado no es válido", 3)
    
    if eleccion == None:
        print("El dato ingresado no es válido para ordenar la lista")
    else:
        if eleccion == "Apellido":
            ordenar_con_criterio_key(eleccion, lista_empleados)
            # ordenar_lista_segun_orden(lista_empleados, "ID", 1)

        elif eleccion == "Nombre":
            ordenar_con_criterio_key(eleccion, lista_empleados)
            # ordenar_lista_segun_orden(lista_empleados, "ID", 1)

        elif eleccion == "Salario":
            ordenar_con_criterio_key(eleccion, lista_empleados)
            # ordenar_lista_segun_orden(lista_empleados, "ID", 1)

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

# region Generar reporte de empleados (salarios)

def generar_txt(lista: list[dict], key: str, pivote: int|str, filtrador: int, reporte_n: int) -> int:

    if filtrador == 1:
        coincidencia = buscar_dato(lista, key, pivote, filtrador)
    elif filtrador == 2:
        coincidencia = buscar_dato(lista, key, pivote, filtrador)

    key = key.lower()
    
    reporte = reporte_n + 1

    mostrar_lista_empleados(coincidencia)

    fecha = conseguir_fecha()
    coindencia = len(coincidencia)

    string = (f"Reporte N°:{reporte:04}\n"
                f"Fecha: {fecha}\n"
                f"Cantidad de coincidencias: {coindencia}\n"
                f"ID   Nombre{" "*15}Apellido{" "*13}"
                f"DNI{" "*8}Puesto{" "*6}Salario     \n"
                f"{"-"*85}")
    
    with open(f"Reportes/reporte_{reporte}_{key}.txt", "w", encoding="utf-8") as archivo:
        archivo.write(string)
        for empleado in coincidencia:
            archivo.write(f"\n{empleado['ID']:<5}{empleado['Nombre']:<21}"
                        f"{empleado['Apellido']:<21}{empleado['DNI']:<11}"
                        f"{empleado['Puesto']:<12}${empleado['Salario']:<13.0f}")
    
    return reporte

# - 8 ------------------------------------------------------------------------------------------------------ #

def generar_reporte_salario(lista: list[dict], key: str, reporte_n: int) -> int|bool:
    salario = get_int("Ingrese el monto: ", "ERORR. Ingreselo nuevamente.", 1,
                    math.inf, "No se pudo validar el monto", 3)
    if salario == None:
        bandera = False
    else:
        bandera = generar_txt(lista, key, salario, 1, reporte_n)
        print('El reporte se ha generado exitosamen en la carpeta "Reportes"')

    return bandera

# endregion

# region Generar reporte de empleados (apellidos)
# - 9 ------------------------------------------------------------------------------------------------------ #

def generar_reporte_apellido(lista: list[dict], key: str, reporte_n: int) -> int|bool:
    apellido = solicitar_dato("Apellido")
    if apellido == None:
        bandera = False

    else:
        bandera = generar_txt(lista, key, apellido, 2, reporte_n)
        print('El reporte se ha generado exitosamen en la carpeta "Reportes"')

    return bandera

# endregion