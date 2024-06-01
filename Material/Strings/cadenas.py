# cadena = "Hola Mundo"
# caracter = cadena[0]
# print(caracter)  #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# cadena[2] = 'P'
################################################################################################

# subcadena = ""
# for i in range(2,6):
#     print(cadena[i], end = "")

# print(cadena[2:6])
# print(cadena[:6])
# print(cadena[2:])
# print(cadena[0:])
# print(cadena[:])
# print(cadena[::-1])

################################################################################################

# cadena = "Hola mundo"
# cadena = "P" + cadena[1:]
# print(cadena)

# cadena_2 = ", ¿Como están? \n"
# cadena_3 = f"{cadena}{cadena_2}"
# print(cadena_3)

# print(cadena_3 * 3)

################################################################################################

# cadena = "hola"
# print(cadena == "hola")
# print(cadena != "hola")
# print(cadena == "Hola")  # H no es igual a h es valor ASCII
# print(cadena > "Hola")
# print(cadena < "azul")

################################################################################################

# nombres = ["Luis", "Marcela", "Carlos", "Dario", "Araceli"]

# for i in range(0, len(nombres) - 1):
#     for j in range(i+1, len(nombres)):
#         if nombres[i] > nombres[j]:
#             auxiliar = nombres[i]
#             nombres[i] = nombres[j]
#             nombres[j] = auxiliar

# print(nombres)

################################################################################################

# cadena = "HOLA"
# for i in range(len(cadena)):
#     print(cadena[i])

################################################################################################

# cadena = "H3la"
# cadena_2 = ""

# print(ord(" "))
# print(chr(32))

# for i in range(len(cadena)):
#     orden = ord(cadena[i]) - 32
#     caracter = chr(orden)
#     cadena_2 += caracter

# print(cadena_2)

# orden = 65
# print(chr(orden))

################################################################################################

# for i in range(len(cadena)):
#     orden = ord(cadena[i])
#     if orden >= 65 or orden <= 126:
#         caracter = chr(orden + 32)
#         cadena_2 += caracter
#         continue

#     cadena_2 += cadena[i]

# print(cadena_2)

################################################################################################
# def es_caracter_valido(un_caracter, validos):
#     es_valido = True
#     for i in range(len(validos)):
#         if un_caracter == validos[i]:
#             es_valido = False
#             break

#     return es_valido

# # caracteres_validos = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# # cadenita = "HolA"

# vector = [3, 8, 1, 4, 7]
# for i in range(0, len(vector)-1):  # NO ORDENA LOS NÚMEROS, iniciar en 0
#     for j in range(i+1, len(vector)):
#         if vector[i] < vector[j]:
#             auxiliar = vector[i]
#             vector[i] = vector[j]
#             vector[j] = auxiliar
# print(vector)

################################################################################################

# cadena = "MARCELA BU"
# rojo = "\033[31m"
# reset = "\033[0m"
# print(f"{rojo}{cadena}{reset}")

# cadena = cadena.capitalize() # Marcela bu
# print(f"{rojo}{cadena}{reset}")

# cadena = cadena.title() # Marcela Bu
# print(f"{rojo}{cadena}{reset}")

# cadena = cadena.replace("Bu", "!!") # Marcela !!
# print(f"{rojo}{cadena}{reset}")

# cadena = "L-Gante | Sesión #38"
# cadena = cadena.split("#")
# cadena = cadena[0].strip(("| Sesión "))
# (print(f"{rojo}El dato ingresado contiene caracteres no permitidos.\n"
#       "Por favor, ingrese los datos sin números, ni caracteres especiales (!, @, °, etc)"
#       f"{reset}")


# delimitador = ","
# lista = ["Java", "Python", "C#", "C"]
# cadena = delimitador.join(lista)
# print(f"{rojo}{cadena}{reset}")

# numero = 5
# print(f"{rojo}{numero:09}{reset}")

# cadena = "222"
# cadena = cadena.zfill(9)
# print(f"{rojo}{cadena}{reset}")

# cadena = "Hola mundo"
# print(cadena.isalpha())  #False
# cadena = "Hola"
# print(cadena.isalpha())  #True

# cadena = "holamundo123"
# print(cadena.isalnum())  #True
# cadena = "hola mundo123"
# print(cadena.isalnum())  #False

# cadena = "hola mundo hola mundo hola mundo"
# cantidad = cadena.count("la")
# print(f"{rojo}{cantidad}{reset}")

# indice = cadena.find("mundo")
# print(indice)

# indice = cadena.find("mundo", 10)
# print(indice)

# print("*" * 30)

print("Apellido".capitalize())