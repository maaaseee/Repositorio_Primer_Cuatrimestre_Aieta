def validate_int_number(mensaje_error: str, minimo: int, maximo: int, reintentos: int, numero: int) -> int|float|None:
    if numero >= minimo and numero <= maximo:
        resultado = numero
        
    else:
        for i in range(0, reintentos):
            resultado = None

            numero = input(mensaje_error)
            numero = int(numero)

            if numero >= minimo and numero <= maximo:
                resultado = numero
                break

    return resultado

def validate_float_number(mensaje_error: str, minimo: float, maximo: float, reintentos: int, numero: float) -> float|None:
    if numero >= minimo and numero <= maximo:
        resultado = numero
    else:
        for i in range(0, reintentos):
            resultado = None

            numero = input(mensaje_error)
            numero = float(numero)

            if numero >= minimo and numero <= maximo:
                resultado = numero
                break

    return resultado

def validate_length(mensaje_error: str, minimo: int, maximo: int, reintentos: int, longitud: int) -> str|None:
    if longitud >= minimo and longitud <= maximo:
        resultado = longitud
    else:
        for i in range(0, reintentos):
            resultado = None

            texto = input(mensaje_error)
            longitud = len(texto)
                
            if longitud >= minimo and longitud <= maximo:
                resultado = longitud
                break

    return resultado