from menus import *
from os import system
from input_paquete.input_func import *
from datetime import date


def confirmar_eleccion(mensaje: str, modificacion: any, opcion_1: any, opcion_2: any) -> any:
    # Se ingresan dos opciones a la funcion, y se reemplaza a la variable "modificacion"
    # Este reemplazo depende de la respuesta del usuario

    mensaje_1 = "\nSe realizó la modificación exitosamente.\n"
    mensaje_2 = "\nEl cambio fue revertido exitosamente.\n"

    bandera_error = True
    for _ in range(4):
        eleccion_empleado = input(mensaje).upper()
        if eleccion_empleado == "SI":
            modificacion = opcion_1
            bandera_error = False
            print(mensaje_1)
            break
        
        elif eleccion_empleado == "NO":
            modificacion = opcion_2
            bandera_error = False
            print(mensaje_2)
            break
    
    if bandera_error == True:
        enviar_mensaje_error(6)
        modificacion = opcion_2
    
    return modificacion

def conseguir_keys(lista: list[dict]) -> list:
    """_summary_
    Crea una lista con las keys de un diccionario

    Args:
        lista (list[dict]): Lista compuesta de diccionarios

    Returns:
        list: La lista SOLO con las keys del diccionario.
    """
    keys = list(lista[0].keys())
    
    return keys

def conseguir_keys_exclusiva(lista: list[dict], key_prohibida: str) -> list:
    """_summary_
    Crea una lista con las keys de un diccionario, a excepcion de una.

    Args:
        lista (list[dict]): Lista compuesta de diccionarios
        key_prohibida (str): Key que no se desea agregar a la lista.

    Returns:
        list: Lista SOLO con las keys seleccionadas del diccionario.
    """
    keys = list(lista[0].keys())
    indice = keys.index(key_prohibida)
    keys.pop(indice)
    
    return keys

def armar_auxiliar_diccionario(dict_auxiliar: dict, keys: list) -> dict:
    """_summary_
    Crea un diccionnario auxiliar para trabajar las modificaciones.

    Args:
        lista_auxiliar (list[dict]): Diccionario original
        keys (list): Lista de keys del diccionario original

    Returns:
        dict: La copia del diccionario.
    """
    diccionario_auxiliar = {}
    for key in keys:
        diccionario_auxiliar[key] = dict_auxiliar[key]

    return diccionario_auxiliar

def calcular_promedio_key(lista: list[dict], key: str) -> float:
    """_summary_

    Args:
        lista (list[dict]): Lista compuesta de diccionarios.
        key (str): Key con la que se encuentra el promedio

    Returns:
        float: Devuelve el promedio de todos los valores de una key, que se
        encuentre en una lista
    """
    acumulador = 0
    for dato in lista:
        acumulador += dato[key]

    promedio = acumulador / len(lista)
    return promedio

def ordenar_lista_segun_orden(lista: list[dict], key: str, orden: int) -> list[dict]:
    """_summary_
    Ordena la lista segun el orden solicitado por el usuario.

    Args:
        lista (list[dict]): Lista compuesta de diccionarios.
        key (str): Key con la que se ordena la lista.
        orden (int): Orden de menor a mayor (1), o mayor a mejor (2)

    Returns:
        list[dict]: La lista ordenada
    """
    largo_de_lista = len(lista)
    match orden:
        case 1:
            for i in range(largo_de_lista):
                for j in range(0, largo_de_lista - i - 1):
                    if lista[j][key] > lista[j + 1][key]:
                        lista[j], lista[j + 1] = lista[j + 1], lista[j]
        case 2:
            for i in range(largo_de_lista):
                for j in range(0, largo_de_lista - i - 1):
                    if lista[j][key] < lista[j + 1][key]:
                        lista[j], lista[j + 1] = lista[j + 1], lista[j]

def buscar_dato(lista: list[dict], key: str, busqueda: int|str|float, filtrador: int) -> list:
    """_summary_

    Args:
        lista (list[dict]): Lista compuesta de diccionarios.
        key (str): Key usada para buscar a las coincidencias.
        busqueda (int | str | float): El dato con el que debe coincidir algun diccionario.
        filtrador (int): El tipo de busqueda que se realiza (1 busca mayores a "busqueda",
        2 busca un dato igual a "busqueda")

    Returns:
        list: Lista con las coincidencias encontradas.
    """
    resultado = []
    match filtrador:
        case 1:
            for data in lista:
                if data[key] > busqueda:
                    resultado.append(data)
            if len(resultado) == 0:
                resultado = None
        case 2:
            for data in lista:
                if data[key] == busqueda:
                    resultado = data
    
    return resultado

def buscar_lista_datos(lista: list[dict], key: str, lista_filtradora: list) -> list:
    """_summary_
    Busca 3 diccionarios de una lista de diccionarios, que coincidan con los datos buscados en una lista.

    Args:
        lista (list[dict]): Lista compuesta por diccionarios.
        key (str): Key para buscar las coincidencias.
        lista_filtradora (list): Lista con varias opciones a buscar.

    Returns:
        list: Lista con las coincidencias encontradas.
    """
    resultado = []
    contador = 0
    for data in lista:
        for tipo in lista_filtradora:
            if contador == 3:
                break
            if data[key] == tipo:
                resultado.append(data)
                contador += 1

    return resultado

def conseguir_fecha():
    fecha = date.today()
    fecha_formateada = fecha.strftime("%d-%m-%Y")

    return fecha_formateada

def quitar_ceros_string(string: str):
    string = str(string)
    string_2 = "0"
    for i in range(len(string)):
        string_2 += string[i]

    return string_2

def calcular_promedio_key_2(lista: list[dict], key: str) -> float:
    """_summary_

    Args:
        lista (list[dict]): Lista compuesta de diccionarios.
        key (str): Key con la que se encuentra el promedio

    Returns:
        float: Devuelve el promedio de todos los valores de una key, que se
        encuentre en una lista
    """
    acumulador = 0
    for dato in lista:
        if dato["Grupo sanguineo"] == key:
            acumulador += 1

    promedio = ((acumulador * 100) / len(lista))
    return promedio


