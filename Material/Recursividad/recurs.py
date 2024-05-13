def calcular_factorial(numero) -> int:
    if numero == 0:
        resultado = 1
    else:
        resultado = numero * calcular_factorial(numero - 1)
    
    return resultado

numero = 5
factorial = calcular_factorial(numero)

print(f"El factorial del número {numero} es: {factorial}.")