from input_paquete.validate import *

rojo = "\033[31m"
reset = "\033[0m"
def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, alerta: str, reintentos: int) -> int|None:
    """_summary_

    Args:
        mensaje (str): Mensaje para la introduccion de datos.
        mensaje_error (str): En caso de no seleccionaro correctamente el dato, se muestra un error.
        minimo (int): Rango minimo del numero
        maximo (int): Rango maximo del numero
        alerta (str): Si no se puede validar el numero, muestra una alerta indicando la falla en la validacion final.
        reintentos (int): Cantidad de reintentos para el ingreso de datos.

    Returns:
        int|None: Devuelve el numero en caso de ser validado, caso contrario, devuelve un None
    """

    numero = input(mensaje).lstrip()
    
    validacion = validate_int_number(mensaje, mensaje_error, minimo, maximo, reintentos, numero)
    if validacion == None:
        numero = validacion
        print(alerta)
    else:
        numero = validacion


    return numero


def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, alerta: str, reintentos: int) -> float|None:
    """_summary_

    Args:
        mensaje (str): Mensaje para la introduccion de datos.
        mensaje_error (str): En caso de no seleccionaro correctamente el dato, se muestra un error.
        minimo (int): Rango minimo del numero
        maximo (int): Rango maximo del numero
        alerta (str): Si no se puede validar el numero, muestra una alerta indicando la falla en la validacion final.
        reintentos (int): Cantidad de reintentos para el ingreso de datos.

    Returns:
        float|None: Devuelve el numero en caso de ser validado, caso contrario, devuelve un None
    """

    numero = input(mensaje).strip()

    validacion = validate_float_number(mensaje, mensaje_error, minimo, maximo, reintentos, numero)
    if validacion == None:
        numero = validacion
        print(alerta)
    else:
        numero = validacion

    return numero


def get_string(mensaje: str, minimo: int, maximo: int, reintentos: int) -> str|None:
    """_summary_
    Pide un string, el cual puede contener espacios entre sus caracteres, ademas de guiones y apostrofes.

    Args:
        mensaje (str): Mensaje para el ingreso de datos
        minimo (int): Minimo de caracteres
        maximo (int): Maximo de caracteres
        reintentos (int): Cantidad de reintentos para el ingreso de datos.

    Returns:
        str|None: Devuelve el dato ingresado, o un None en caso de no poder validar
        correctamente, pasado todos los intentos-
    """
    validacion = None
    for _ in range(reintentos + 1):
        texto = input(mensaje)
        texto_2 = space_in_blank(texto)
        if validate_length(minimo, maximo, texto_2):

            if validate_string(texto_2):
                texto_3 = texto_2.title()
                validacion = texto_3
                break

            else:
                print(f"{rojo}El dato ingresado contiene caracteres no permitidos.\n"
                    "Por favor, ingrese los datos sin números, ni caracteres "
                    "especiales (!, @, °, etc)"
                    f"{reset}")
        
        else:
            print(f"{rojo}La cantidad de caracteres excede/es menor a los permitidos.\n"
                f"Por favor, ingrese un texto valido que se encuentre entre los {minimo}"
                f" y {maximo} caracteres. {reset}")

    return validacion

def get_string_2(mensaje: str, minimo: int, maximo: int, reintentos: int) -> str|None:
    """_summary_
    Pide un string, y evita que este sea ingresado con espacios entre sus caracteres.

    Args:
        mensaje (str): Mensaje para el ingreso de datos
        minimo (int): Minimo de caracteres
        maximo (int): Maximo de caracteres
        reintentos (int): Cantidad de reintentos para el ingreso de datos.

    Returns:
        str|None: Devuelve el dato ingresado, o un None en caso de no poder validar
        correctamente, pasado todos los intentos-
    """
    validacion = None
    for _ in range(reintentos + 1):
        texto = input(mensaje)
        texto_2 = not_spaces_in_blank(texto)
        if validate_length(minimo, maximo, texto_2):

            if validate_string(texto_2):
                texto_3 = texto_2.title()
                validacion = texto_3
                break

            else:
                print(f"{rojo}El dato ingresado contiene caracteres no permitidos.\n"
                    "Por favor, ingrese los datos sin números, ni caracteres "
                    "especiales (!, @, °, etc)"
                    f"{reset}")
        
        else:
            print(f"{rojo}La cantidad de caracteres excede/es menor a los permitidos.\n"
                f"Por favor, ingrese un texto valido que se encuentre entre los {minimo}"
                f" y {maximo} caracteres. {reset}")

    return validacion


def get_string_excluyente(mensaje: str, minimo: int, maximo: int, lista: list, reintentos: int) -> str|None:
    validacion = None
    for _ in range(reintentos + 1):
        texto = input(mensaje).strip()

        texto_2 = texto.capitalize()
        if validate_length(minimo, maximo, texto_2):
            if validate_lista(texto_2, lista):
                validacion = texto_2
                break

            else:
                print(f"{rojo}El dato ingresado no es similar a uno de "
                    f"la lista.{reset}")

        else:
            print(f"{rojo}La cantidad de caracteres excede/es menor a los permitidos.\n"
                f"Por favor, ingrese un texto valido que se encuentre entre los {minimo}"
                f" y {maximo} caracteres. {reset}")

    return validacion

def get_string_excluyente_2(mensaje: str, minimo: int, maximo: int, lista: list, reintentos: int) -> str|None:
    """_summary_
    Pide un string al usuario, que se encuentre dentro de una lista de opciones.

    Args:
        mensaje (str): Mensaje de introduccion de dato.
        minimo (int): Minimo de caracteres
        maximo (int): Maximo de caracteres
        lista (list): Lista con la que excluye a los ingresos de datos
        reintentos (int): Cantidad de veces a volver a intentar el ingreso

    Returns:
        str|None: Devuelve el dato ingresado, o un None en caso de no poder validar
        correctamente, pasado todos los intentos-
    """
    validacion = None
    for _ in range(reintentos + 1):
        texto = input(mensaje).strip()
        texto_2 = texto.upper()
        texto_3 = texto_2.rstrip("+")
        texto_4 = texto_3.rstrip("-")

        if validate_length(minimo, maximo, texto_2):
            if validate_lista(texto_4, lista):
                validacion = texto_2
                break

            else:
                print(f"{rojo}El dato ingresado no es similar a uno de "
                    f"la lista.{reset}")

        else:
            print(f"{rojo}La cantidad de caracteres excede/es menor a los permitidos.\n"
                f"Por favor, ingrese un texto valido que se encuentre entre los {minimo}"
                f" y {maximo} caracteres. {reset}")


    return validacion

