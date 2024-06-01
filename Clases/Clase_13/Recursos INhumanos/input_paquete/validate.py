rojo = "\033[31m"
reset = "\033[0m"

def validate_int_number(mensaje: str, mensaje_error: str, minimo: int, maximo: int, 
                        reintentos: int, numero: str) -> int|None:
    if numero.isnumeric() and (int(numero) >= minimo and int(numero) <= maximo):
        resultado = int(numero)
    
    else:
        for _ in range(0, reintentos):
            resultado = None

            print(f"{rojo}{mensaje_error}{reset}")
            numero = input(mensaje)

            if numero.isnumeric() and (int(numero) >= minimo and int(numero) <= maximo):
                return int(numero)

    return resultado

def es_numero_valido(numero: str, minimo: float, maximo: float) -> float | None:
    # Validar flotantes
    if numero.count('.') == 1:
        parte_entera, parte_decimal = numero.split('.')
        if parte_entera.isnumeric() and parte_decimal.isnumeric():
            numero_float = float(numero)
            if minimo <= numero_float <= maximo:
                return numero_float
    return None

def validate_float_number(mensaje_error: str, minimo: float, maximo: float, reintentos: int, numero: str) -> float | None:
    resultado = es_numero_valido(numero, minimo, maximo)
    if resultado != None:
        return resultado

    for _ in range(reintentos):
        numero = input(mensaje_error)
        resultado = es_numero_valido(numero, minimo, maximo)
        if resultado != None:
            return resultado

    return None

def validate_length(minimo: int, maximo: int, texto: str) -> bool|None:
    longitud = len(texto)
    if longitud >= minimo and longitud <= maximo:
        longitud = True
    else:
        longitud = False

    return longitud

def validate_string(texto: str) -> bool|None:
    textito = texto.strip(" ")
    if textito.isalpha():
        return True
    
    return None

def validate_trabajos(texto: str, base_de_datos: list) -> bool|None:
    for dato in base_de_datos:
        if texto == dato.capitalize():
            return True

    return None