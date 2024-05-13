
def filtrar_enteros(numero: int):
    # Si el número es positivo, suma 1 al contador
    # Esto sirve para saber cuantos positivos hay
    # Si es negativo, no suma nada

    if numero > 0:
        contador = 1
    else:
        contador = 0
    
    return contador