from Package_folder.input import get_int
from especificas import *
from arrays_generales import *

bandera_seguir = True
cantidad_numeros_para_ingresar = 5

lista = [0] * cantidad_numeros_para_ingresar

contador_positivos = 0
sumar_pares = 0

for i in range(len(lista)):
    lista[i] = get_int("Ingrese su numero: ")
    contador_positivos += filtrar_enteros(lista[i])
    sumar_pares += filtrar_pares(lista[i])


while bandera_seguir:
    opcion = int(input("1.Mostrar cantidad de positivos y negativos \n"
                        "2.Mostrar la suma de los números pares\n"
                        "3.Mostrar el mayor de los números"
                        " impares. \n4.Listar los números ingresados"
                        "\n5.Listar solo números pares.\n6.Listar los números"
                        " de las posiciones impares \n7.Salir\n"))

    match opcion:
        case 1:
            print(f"La cantidad de numeros positivos es: {contador_positivos}"
            f" y la de negativos es de: {cantidad_numeros_para_ingresar - contador_positivos}")
        case 2:
            print(sumar_pares)
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            seguir = input("¿Está seguro que desea salir? Si/No \n")
            if seguir == "Si":
                bandera_seguir = False



















# def calcular_descuento(precio: float, cantidad: int, descuento: float) -> int|float:
#     precio = float(input(precio))
#     cantidad = int(input(cantidad))
#     descuento = float(input(descuento))

#     suma_productos = precio * cantidad

#     if cantidad > 9:
#         descuento = (suma_productos * descuento) / 100
#         descuento_aplicado = suma_productos - descuento
#     else:
#         descuento_aplicado = suma_productos

#     return descuento_aplicado

# factura = calcular_descuento("El precio del producto es: $", "La cantidad de productos es: ",
#                             "Y el descuento es del: %")

# print(f"El precio final de estos productos es de: {factura}")