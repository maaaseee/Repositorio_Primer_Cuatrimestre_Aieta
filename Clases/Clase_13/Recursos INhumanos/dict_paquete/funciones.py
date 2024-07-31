from test.menus import *
from os import system
import math
from input_paquete.input_func import *

def confirmar_eleccion(mensaje: str, modificacion, opcion_1, opcion_2):
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
    # Extrae las keys de un diccionario, adentro de una lista
    keys = list(lista.keys())

    return keys

def armar_auxiliar_diccionario(lista_auxiliar: list[dict], keys) -> dict:
    # Crea un diccionario auxiliar con las keys del diccionario original
    diccionario_auxiliar = {}
    for key in keys:
        diccionario_auxiliar[key] = lista_auxiliar[key]

    return diccionario_auxiliar

def calcular_promedio_key(lista: list[dict], key: str):
    # Calcula el promedio de una key de la lista de empleados
    acumulador = 0
    for empleado in lista:
        acumulador += empleado[key]

    promedio = acumulador / len(lista)
    return promedio

def ordenar_lista_segun_orden(lista: list[dict], key: str, orden: int) -> list[dict]:
    # Segun el número de orden, se indica el criterio para ordenar la lista.
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

def max_value_id(lista: list[dict]):
    # Devuelve el valor maximo de una key de la lista de empleados
    valor_maximo = 0
    if len(lista) > 0:
        for empleado in lista:
            if empleado["ID"] > valor_maximo:
                valor_maximo = empleado["ID"]

    return valor_maximo

def last_id(value_1: int, value_2: int) -> int:
    last_id = 0
    if value_1 == value_2 or value_1 > value_2:
        last_id = value_1
    elif value_2 > value_1:
        last_id = value_2

    return last_id


# def ordenar_lista_empleados_menor_a_mayor(lista: list[dict], key: dict[str]):
#     # Ordena la lista segun la key ingresada
#     # Lo hace de menor a mayor
#     largo_de_lista = len(lista)
#     for i in range(largo_de_lista):
#         for j in range(0, largo_de_lista - i - 1):
#             if lista[j][key] > lista[j + 1][key]:
#                 lista[j], lista[j + 1] = lista[j + 1], lista[j]

# def ordenar_lista_empleados_mayor_a_menor(lista: list[dict], key: dict[str]):
#     # Ordena la lista segun la key ingresada
#     # Lo hace de mayor a menor
#     largo_de_lista = len(lista)
#     for i in range(largo_de_lista):
#         for j in range(0, largo_de_lista - i - 1):
#             if lista[j][key] < lista[j + 1][key]:
#                 lista[j], lista[j + 1] = lista[j + 1], lista[j]