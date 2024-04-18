def filtrar_pares (numero):
    filtrador = numero % 2

    if filtrador == 0:
        return "El número es par"
    
    return "El número es impar"
    # if numero % 2 == 0:
    #     return "El número es par"
    # else:
    #     return "El número es impar"

numero = input("Ingrese el número aquí: ")
numero = int(numero)

respuesta = filtrar_pares(numero)

print(respuesta)