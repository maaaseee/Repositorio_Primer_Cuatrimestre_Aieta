def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int|None:
    # Se solicita la clave bancaria del usuario
    # Se valida la clave, y se vuevle a solicitar el ingreso de datos si no se encuentra entre 1000 y 9999
    # Si se repite el ingreso de datos mas de 3 veces, se llega al máximo de iteraciones y se cierra
    # Devuelve la clave bancaria
    
    numero = input(mensaje)
    numero = int(numero)

    while numero < minimo or numero > maximo:
        numero = input(mensaje_error)
        numero = int(numero)
        reintentos -= 1

        if reintentos < 1:
            numero = None
            print(f"La contraseña ingresada es inválida.")
            break

    return numero

clave_bancaria = get_int("Ingrese su clave bancaria: ", "ERROR. Ingrese nuevamente su clave bancaria: ", 1000, 9999, 3)

print(f"La clave bancaria ingresada es: ({clave_bancaria})")

# def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos: int) -> float|None:
#     # Se solicita la altura del usuario
#     # Se valida la altura, y se vuevle a solicitar el ingreso de datos si no se encuentra entre 1.60 y 2.10
#     # Si se repite el ingreso de datos mas de 3 veces, se llega al máximo de iteraciones y se cierra
#     # Devuelve la altura

#     numero = input(mensaje)
#     numero = float(numero)

#     while numero < minimo or numero > maximo:
#         numero = input(mensaje_error)
#         numero = float(numero)
#         reintentos -= 1

#         if reintentos < 1:
#             numero = None
#             print(f"La contraseña ingresada es inválida.")
#             break

#     return numero

# altura = get_float("Ingrese la altura: ", "ERROR. Ingrese nuevamente la altura: ", 1.60, 2.10, 3)

# print(f"La altura ingresada es: ({altura})")

# def get_string(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> str|None:
#     # Se solicita una contraseña al usuario
#     # Se valida la cantidad de caracteres de la contraseña, y se vuevle a solicitar 
#     # el ingreso de datos si no se encuentra entre 4 y 12 caracteres

#     # Si se repite el ingreso de datos mas de 3 veces, se llega al máximo de iteraciones y se cierra
#     # Devuelve la contraseña

#     texto = input(mensaje)
#     longitud = len(texto)

#     while longitud < minimo or longitud > maximo:
#         texto = input(mensaje_error)
#         longitud = len(texto)
        
#         reintentos -= 1
#         if reintentos < 1:
#             texto = None
#             print(f"La contraseña ingresada es inválida.")
#             break

#     return texto

# texto = get_string("Ingrese la contraseña: ", "ERROR. Ingrese nuevamente la contraseña: ", 4, 12, 3)

# print(f"La contraseña ingresada es: ({texto})")