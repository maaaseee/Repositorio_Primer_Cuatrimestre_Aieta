rojo = "\033[31m"
reset = "\033[0m"

def validate_int_number(mensaje: str, mensaje_error: str, minimo: int, maximo: int, 
                        reintentos: int, numero: str) -> int|None:
    """_summary_
    Valida que un numero se encuentre en base 10, y que no tenga ningun signo, ademas
    de encontrarse en el rango solicitado

    Args:
        mensaje (str): Mensaje para la introduccion de datos.
        mensaje_error (str): En caso de no seleccionaro correctamente el dato, 
        se muestra un error.
        minimo (int): Rango minimo del numero
        maximo (int): Rango maximo del numero
        alerta (str): Si no se puede validar el numero, muestra una alerta indicando
        la falla en la validacion final.
        reintentos (int): Cantidad de reintentos para el ingreso de datos.
        numero (str): Numero a validar

    Returns:
        int|None: Devuelve el numero validado, caso contrario, devuelve un None.
    """
    if numero.isdigit() and (int(numero) >= minimo and int(numero) <= maximo):
        resultado = int(numero)
    
    else:
        for _ in range(0, reintentos):

            print(f"{rojo}{mensaje_error}{reset}")
            numero = input(mensaje)

            if numero.isnumeric() and (int(numero) >= minimo and int(numero) <= maximo):
                return int(numero)
        resultado = None

    return resultado

def es_numero_valido(numero: str, minimo: float, maximo: float) -> float | None:
    """_summary_
    Valida que el número tenga un punto (indicando que, es del tipo float)

    Args:
        numero (str): Numero a validar, del tipo float
        minimo (float): Rango minimo del numero
        maximo (float): Rango maximo del numero

    Returns:
        float | None: Devuelve el numero validado, caso contrario, devuelve un None.
    """

    if len(numero) > 0:
        if numero.count(".") == 1:
            separacion = numero.split('.')
            if separacion[0].isnumeric() and separacion[1].isnumeric():
                numero_float = float(numero)
                if minimo <= numero_float and numero_float <= maximo:
                    validacion = numero_float
        
        elif numero.isnumeric() == False:
            validacion = None
        
        else:
            validacion = float(numero)
    else:
        validacion = None
    
    return validacion

def validate_float_number(mensaje, mensaje_error: str, minimo: float, maximo: float, reintentos: int, numero: str) -> float | None:
    """_summary_
    Valida el ingreso de un numero del tipo Float.

    Args:
        mensaje (str): Mensaje para la introduccion de datos.
        mensaje_error (str): En caso de no seleccionaro correctamente el dato, 
        se muestra un error.
        minimo (floaat): Rango minimo del numero
        maximo (float): Rango maximo del numero
        alerta (str): Si no se puede validar el numero, muestra una alerta indicando
        la falla en la validacion final.
        reintentos (int): Cantidad de reintentos para el ingreso de datos.
        numero (str): Numero a validar

    Returns:
        float | None: Devuelve el numero validado, caso contrario, devuelve un None.
    """
    resultado = es_numero_valido(numero, minimo, maximo)
    if resultado == None:
        for _ in range(reintentos):
            print(f"{rojo}{mensaje_error}{reset}")
            numero = input(mensaje)
            resultado = es_numero_valido(numero, minimo, maximo)
            if resultado != None:
                validacion = resultado
                break
            validacion = None

    else:
        validacion = resultado

    return validacion

def validate_length(minimo: int, maximo: int, texto: str) -> bool|None:
    """_summary_
    Valida la longitud de una cadena.

    Args:
        minimo (int): Minimo de caracteres.
        maximo (int): Maximo de caracteres.
        texto (str): Mensaje ingresado por el usuario.

    Returns:
        bool|None: 
    """
    longitud = len(texto)
    if longitud >= minimo and longitud <= maximo:
        longitud = True
    else:
        longitud = False

    return longitud

def validate_string(texto: str) -> bool:
    """_summary_
    Valida que el texto solo tenga caracteres del alfabeto.

    Args:
        texto (str): El texto que recibe la validacion

    Returns:
        bool: Devuelve un booleano en caso de realizarse la validacion (True),
        caso contrario (None).
    """
    validacion = None
    textito = texto.replace(" ", "").replace("-", "").replace("'", "")
    if textito.isalpha():
        validacion = True
    
    return validacion

def validate_lista(texto: str, base_de_datos: list) -> bool|None:
    """_summary_
    Valida que el texto ingresado, se encuentre en una lista filtradora.

    Args:
        texto (str): Texto ingresado por el usuario.
        base_de_datos (list): Lista para buscar coincidencia con el texto

    Returns:
        bool|None: En caso de encontrar el dato, devuelve True, caso contrario, devuelve None
    """
    validacion = None
    for dato in base_de_datos:
        if texto.capitalize() == dato.capitalize():
            validacion = True

    return validacion

def space_in_blank(texto: str) -> str:
    """_summary_
    Devuelve a la cadena, sin excesos de espacios entre sus caracteres.

    Args:
        texto (str): Texto a modificar

    Returns:
        str: La cadena modificada
    """
    texto_nuevo = ""
    for i in range(len(texto)):
        if texto[i] == " " and texto[i - 1] == " ":
            pass
        else:
            texto_nuevo += texto[i]

    return texto_nuevo

def not_spaces_in_blank(texto: str):
    """_summary_
    Devuelve la cadena, sin espacios entre caracteres.

    Args:
        texto (str): Texto a modificar

    Returns:
        str: La cadena, sin espacios entre caracteres alfabeticos
    """
    texto_nuevo = ""
    for i in range(len(texto)):
        if texto[i] != " ":
            texto_nuevo += texto[i]

    return texto_nuevo
