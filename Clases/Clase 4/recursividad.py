# from input import get_int

# def sumar_naturales(numero) -> int:
#     if numero == 0:
#         resultado = 0

#     else:
#         resultado = numero + sumar_naturales(numero - 1)

#     return resultado

# resultado_final = sumar_naturales(numero = 10)

# print(resultado_final)

# def calcular_potencia(base: int, exponente: int) -> int:
#     if exponente == 0:
#         return 1

#     else:
#         cuenta = base ** exponente
#         resultado = calcular_potencia(base, exponente - 1)
#         return cuenta + resultado


# resultado_final = calcular_potencia(base = 2, exponente = 6)

# print(resultado_final)

def fibonacci(numero: int) -> int:
    cuenta = 0
    
    if numero > 4:
        return numero
    else:
        cuenta = numero + fibonacci(numero + cuenta)

    return cuenta


a = fibonacci(numero = 0)
print(a)