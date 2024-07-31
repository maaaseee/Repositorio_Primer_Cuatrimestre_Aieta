import math

'''Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.'''

def solicitar_numero_entero(reutilizar_1) -> int:
    print("Verificar número entero")
    while True:
        try:
            numero_entero = input("Ingrese su número aquí: ")
            numero_entero = int(numero_entero)
            return numero_entero
        except ValueError:
            print("Ingrese un número válido.")

respuesta_1 = solicitar_numero_entero()

print(respuesta_1)

'''Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.'''

def solicitar_numero_float(reutilizar_2) -> float:
    print("Verificar número flotante")
    while True:
        try:
            numero_float = input("Ingrese el número aquí: ")
            numero_float = float(numero_float)
            return numero_float
        except ValueError:
            print("Ingrese un número válido.")

respuesta_2 = solicitar_numero_float()

print(respuesta_2)

'''Crear una función que le solicite al usuario el ingreso de una cadena y la retorna. '''

def solicitar_cadena(reutilizar_3) -> str:
    print("Verificar cadena")
    while True:
        try:
            cadena = input("Ingrese su texto aquí: ")
            cadena = str(cadena)
            return cadena
        except ValueError:
            print("Ingrese la cadena nuevamente.")

respuesta_3 = solicitar_cadena()

print(respuesta_3)

'''Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.'''

def solicitar_numero_entero_reut(numero_entero: int) -> int:
    return numero_entero

def solicitar_numero_float_reut(numero_float: float) -> float:
    return numero_float

def solicitar_cadena_reut(cadena: str) -> str:
    return cadena

while True:
    print("Verificar número entero")
    numero_entero_a = input("Ingrese su número aquí: ")
    try:
        numero_entero_a = int(numero_entero_a)
    except ValueError:
        print("Ingrese un número válido.")
        continue

    print("Verificar número flotante")
    numero_float_b = input("Ingrese su número aquí: ")
    try:
        numero_float_b = float(numero_float_b)
    except ValueError:
        print("Ingrese un número válido.")
        continue

    print("Verificar cadena")
    cadena_c = input("Ingrese su cadena aquí: ")
    try:
        cadena_c = str(cadena_c)
        break
    except ValueError:
        print("Ingrese una cadena válida.")
        continue

entero = solicitar_numero_entero_reut(numero_entero_a)
flotante = solicitar_numero_float_reut(numero_float_b)
string = solicitar_cadena_reut(cadena_c)

print(f"{entero} + {flotante} + {string}")

'''Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.'''

def calcular_area_circulo():
    print("Calcular área de un círculo")
    while True:
        try:
            radio = input("Ingrese el radio de su círculo: ")
            radio = float(radio)
            cuenta_final = math.pi * (radio ** 2)
        except ValueError:
            print("Ingrese el radio de su círculo nuevamente.")

        return cuenta_final

respuesta_5 = calcular_area_circulo()

print(respuesta_5)

'''Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.'''

def filtrar_pares ():
    print("Verificar número par o impar")
    numero = input("Ingrese el número para verificar aquí: ")
    numero = int(numero)
    filtrador = numero % 2

    if filtrador % 2 == 1:
        return "El número es impar"
    
    return "El número es par"

respuesta_6 = filtrar_pares()

print(respuesta_6)

'''Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.'''

def encontrar_numero_max():
    bandera = True
    numero_maximo = 0

    print("Encontrar número máximo entre 3 ingresos")
    for ingresos in range(3):
        while True:
            try:
                numero_float = input("Ingrese el número aquí: ")
                numero_float = float(numero_float)
                break
            except ValueError:
                print("Ingrese un número válido.")
                continue

        while bandera == True or numero_float > numero_maximo:
            numero_maximo = numero_float
            bandera = False

    return numero_maximo

respuesta = encontrar_numero_max()

print(respuesta)

'''Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.'''

def calcular_potencia():
    print("Ingresar número a potenciar, y su exponente")
    while True:
        numero = input("Ingrese el número a potenciar: ")
        try:
            numero = float(numero)
        except ValueError:
            print("Ingrese un número válido.")
            continue

        potencia = input("Ingrese el exponente al que quiere potenciarlo: ")
        try:
            potencia = int(potencia)
            break
        except ValueError:
            print("Ingrese un número válido.")
            continue

    cuenta = numero ** potencia

    return cuenta

potencia_hecha = calcular_potencia()

print(potencia_hecha)