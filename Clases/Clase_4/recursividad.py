# from Package_folder.input import get_int

# numero_get_int = get_int()

# def sumar_naturales(numero) -> int:
#     if numero == 0:
#         resultado = 0

#     else:
#         resultado = numero + sumar_naturales(numero - 1)

#     return resultado

# resultado_final = sumar_naturales(numero_get_int)
# print(resultado_final)

# base_get_int = get_int()
# exponente_get_int = get_int()

# def calcular_potencia(base: int, exponente: int) -> int:
#     if exponente == 0:
#         return 1

#     else:
#         cuenta = base ** exponente
#         resultado = calcular_potencia(base, exponente - 1)
#         return cuenta + resultado


# resultado_final = calcular_potencia(base_get_int, exponente_get_int)

# print(resultado_final)

def fibonacci(numero: int) -> int:
    if numero == 0:
        return 0
    if numero == 1:
        return 1
    else:
        return fibonacci(numero - 1) + fibonacci(numero - 2)

    return resultado

a = fibonacci(7)
print(a)