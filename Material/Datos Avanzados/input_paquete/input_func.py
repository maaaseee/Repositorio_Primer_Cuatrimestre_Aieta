from input_paquete.validate import *

rojo = "\033[31m"
reset = "\033[0m"
def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, alerta: str, reintentos: int) -> int|None:
    # Se solicita la clave bancaria del usuario
    # Se valida la clave, y se vuevle a solicitar el ingreso de datos si no se encuentra entre 1000 y 9999
    # Si se repite el ingreso de datos mas de 3 veces, se llega al máximo de iteraciones y se cierra
    # Devuelve la clave bancaria

    numero = input(mensaje)

    validacion = validate_int_number(mensaje, mensaje_error, minimo, maximo, reintentos, numero)
    if validacion == None:
        numero = validacion
        print(alerta)
        return numero

    return validacion

# clave_bancaria = get_int("Ingrese su numero: ","ERROR. Ingrese nuevamente su numero",
#                         500, 1000, "El numero ingresado no es valido.", 3)

def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, alerta: str, reintentos: int) -> float|None:
    # Se solicita la altura del usuario
    # Se valida la altura, y se vuevle a solicitar el ingreso de datos si no se encuentra entre 1.60 y 2.10
    # Si se repite el ingreso de datos mas de 3 veces, se llega al máximo de iteraciones y se cierra
    # Devuelve la altura

    numero = input(mensaje)

    validacion = validate_float_number(mensaje_error, minimo, maximo, reintentos, numero)
    if validacion == None:
        numero = validacion
        print(alerta)
        return numero

    return numero

# clave_bancaria = get_float("Ingrese su numero: ","ERROR. Ingrese nuevamente su numero: ",
#                         1, 1000, "El numero ingresado no es valido.", 3)

def get_string(mensaje: str, minimo: int, maximo: int, alerta: str, reintentos: int) -> str|None:

    for _ in range(reintentos + 1):
        texto = input(mensaje)

        if validate_length(minimo, maximo, texto):

            if validate_string(texto):
                textito = texto.capitalize()
                return textito

            else:
                print(f"{rojo}El dato ingresado contiene caracteres no permitidos.\n"
                    "Por favor, ingrese los datos sin números, ni caracteres "
                    "especiales (!, @, °, etc)"
                    f"{reset}")
        
        else:
            print(f"{rojo}La cantidad de caracteres excede/es menor a los permitidos.\n"
                f"Por favor, ingrese un texto valido que se encuentre entre los {minimo}"
                f" y {maximo} caracteres. {reset}")

    print(f"{rojo}{alerta}{reset}")
    return None

# ayuda = get_string("Ingrese el nombre: ", "ERROR. Ingrese nuevamente el nombre",
#                     1, 20, "El texto ingresado no es valido", 3)
# print(ayuda)

def get_string_excluyente(mensaje: str, minimo: int, maximo: int, lista: list, alerta: str, reintentos: int) -> str|None:
    for _ in range(reintentos + 1):
        texto = input(mensaje).strip()
        textito = texto.title()


        if validate_length(minimo, maximo, textito):
            if validate_trabajos(textito, lista):
                return textito

            else:
                print(f"{rojo}El dato ingresado no es similar a uno de "
                    f"la lista.{reset}")

        else:
            print(f"{rojo}La cantidad de caracteres excede/es menor a los permitidos.\n"
                f"Por favor, ingrese un texto valido que se encuentre entre los {minimo}"
                f" y {maximo} caracteres. {reset}")

    print(f"{rojo}{alerta}{reset}")
    return None