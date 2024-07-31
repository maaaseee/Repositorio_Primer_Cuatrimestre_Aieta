from menus import *
from os import system
from input_paquete.input_func import *
from datetime import date


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
    keys = list(lista[0].keys())

    return keys

def armar_auxiliar_diccionario(lista_auxiliar: list[dict], keys) -> dict:
    # Crea un diccionario auxiliar con las keys del diccionario original
    diccionario_auxiliar = {}
    for key in keys:
        diccionario_auxiliar[key] = lista_auxiliar[key]

    return diccionario_auxiliar

def armar_auxiliar_lista(lista) -> list:
    lista_auxiliar = []
    for elemento in lista:
        lista_auxiliar.append(elemento)

    return lista_auxiliar

def calcular_promedio_key(lista: list[dict], key: str) -> float:
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

def buscar_dato(lista: list, key: str, busqueda: int, filtrador: int) -> list:
    resultado = []
    match filtrador:
        case 1:
            for data in lista:
                if data[key] > busqueda:
                    resultado.append(data)
        case 2:
            for data in lista:
                if data[key] == busqueda:
                    resultado = data
    
    return resultado

def conseguir_fecha():
    fecha = date.today()
    fecha_formateada = fecha.strftime("%d-%m-%Y")

    return fecha_formateada
