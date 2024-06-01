cadena = input("Ingrese la cadena acá: ")

'''
1)
Crear una función que reciba como parámetro una cadena y determine la cantidad
de vocales que hay de cada una (individualmente). La función retornará una matriz
indicando en la columna 1 cada vocal, y en la columna 2 la cantidad.
'''

# def contar_vocales(cadena: str) -> list:
#     vocales = ['a', 'e', 'i', 'o', 'u']
#     matriz_vocales = [[0] * 2 for _ in range(len(vocales))]
#     for i in range(len(cadena)):
#         for j in range(len(vocales)):
#             matriz_vocales[j][0] = vocales[j]
#             if cadena[i] == vocales[j]:
#                 matriz_vocales[j][1] += 1
#     return matriz_vocales

# matriz_vocales = contar_vocales(cadena)
# print(matriz_vocales)

'''
2)
Crear una función que reciba una cadena y un caracter. La función deberá devolver
el índice en el que se encuentre la primera incidencia de dicho caracter, o -1 en 
caso de que no esté.
'''
# caracter = []
# for caracteres in range(2):
#     pedir_caracter = input("Ponga su carácter acá: ")
#     caracter += pedir_caracter

# def contar_vocales(cadena: str, caracteres: str) -> int:
#     caracteres_prohibidos = caracteres
#     matriz_vocales = [[-1] * 2 for _ in range(len(caracteres_prohibidos))]

#     for i in range(len(cadena)):
#         for j in range(len(caracteres_prohibidos)):
#             matriz_vocales[j][0] = caracteres_prohibidos[j]
#             if matriz_vocales[j][1] == -1 and cadena[i] == caracteres_prohibidos[j]:
#                 matriz_vocales[j][1] = i+1
    
#     return matriz_vocales

# matriz_vocales_posicion = contar_vocales(cadena, pedir_caracter)
# print(matriz_vocales_posicion)

'''
3)
Crear una función que reciba como parámetro una cadena y determine si la misma
es o no un palíndromo. Deberá retornar un valor booleano indicando lo sucedido.
'''
# def transformar_mayusculas(cadena: str, cadena_vacia: str) -> str:
#     for i in range(len(cadena)):
#         orden = ord(cadena[i])
#         if orden >= 65 and orden <= 90:  # ASCII
#             caracter = chr(orden + 32)
#             cadena_vacia += caracter
#             continue
#         cadena_vacia += cadena[i]

#     return cadena_vacia

def quitar_espacios(cadena: str, cadena_vacia: str) -> str:
    for i in range(len(cadena)):
        if cadena[i]!= " ":
            cadena_vacia += cadena[i]

    return cadena_vacia

# def detectar_palindromo(cadena: str) -> bool:
#     palindromo = False
#     cadena_lower = ""
#     cadena_sin_espacios = ""

#     cadena_lower = transformar_mayusculas(cadena, cadena_lower)
#     cadena_sin_espacios = quitar_espacios(cadena_lower, cadena_sin_espacios)
    
#     for i in range(len(cadena_sin_espacios)):
#         if cadena_sin_espacios[i] != cadena_sin_espacios[len(cadena_sin_espacios) -1 -i]:
#             break
#         palindromo = True

#     return palindromo


# palindromo = detectar_palindromo(cadena)
# print(palindromo)

'''
4)
Crear una función que reciba como parámetro una cadena y suprima los caracteres repetidos.
'''

# def quitar_repetidos(cadena: str) -> str:
#     cadena_sin_espacios = ""
#     caracteres_repetidos = ""
#     cadena_sin_elementos = ""

#     cadena_sin_espacios = quitar_espacios(cadena, cadena_sin_espacios)

#     for i in range(len(cadena_sin_espacios)):
#         if i == 0:
#             cadena_sin_elementos += cadena_sin_espacios[i]
#             caracteres_repetidos += cadena_sin_espacios[i]
#             continue
#         for j in range(len(caracteres_repetidos)):
#             if cadena_sin_espacios[i] == caracteres_repetidos[j]:
#                 break
#         else:
#             cadena_sin_elementos += cadena_sin_espacios[i]
#             caracteres_repetidos += cadena_sin_espacios[i]

#     return cadena_sin_elementos

# cadena_repetidos = quitar_repetidos(cadena)
# print(cadena_repetidos)

'''
5)
Crear una función que reciba una cadena por parámetro y suprima las vocales de la misma.
'''

# def quitar_repetidos_con_vocales(cadena: str) -> str:
#     cadena_sin_espacios = ""
#     cadena_vacia = ""
#     caracteres_repetidos = ['a', 'e', 'i', 'o', 'u']

#     cadena_sin_espacios = quitar_espacios(cadena, cadena_sin_espacios)

#     for i in range(len(cadena_sin_espacios)):
#         bandera = False
#         for j in range(len(caracteres_repetidos)):
#             if cadena_sin_espacios[i] == caracteres_repetidos[j]:
#                 bandera = True
#                 break
#         if bandera == False:
#             cadena_vacia += cadena_sin_espacios[i]

#     return cadena_vacia

# cadena_repetidos_vocales = quitar_repetidos_con_vocales(cadena)
# print(cadena_repetidos_vocales)

'''
6)
Crear una función para contar cuántas veces aparece una subcadena dentro de una cadena.
'''

def contar_subcadenas(cadena: str, cadena_vacia: str) -> int:
    cadena_vacia = ""
    contador = 0
    cadena = quitar_espacios(cadena, cadena_vacia)
    subcadena = input("Ingrese la subcadena acá: ")
    longitud_subcadena = len(subcadena)

    for i in range(len(cadena)):
        if cadena[i:i + longitud_subcadena] == subcadena:
            contador += 1

    return contador

subcadenas = contar_subcadenas(cadena)

print(subcadenas)

'''
CSI UTN

Se ha encontrado una muestra de ADN en el lugar del crimen que contiene la siguiente
secuencia de bases nitrogenadas: “CGTTTAATG”. La investigación ha revelado tres 
posibles sospechosos, cada uno con su propia muestra de ADN:

Juan Pérez
Muestra de ADN: "CGGGGCTAAAATTTTTTACGATCG"
María Rodríguez
Muestra de ADN: "AACGTTTAATGTTCTAAGCTGCG"
Carlos Sánchez
Muestra de ADN: "CGGGGCTAAAATTTTTTACGATCG"

Para resolver el caso, nos piden que desarrollemos un programa que compare las
combinaciones de bases nitrogenadas de la muestra encontrada con las muestras 
de los sospechosos. 

Mostrar el nombre por pantalla en caso de encontrar al asesino, o la leyenda “SON TODOS INOCENTES”. 
'''

lista_adn = [['Juan Perez', 'CGGGGCTAAAATTTTTTACGATCG'],
            ['Maria Rodriguez', 'AACGTTTAATGTCTAAGCTGCG'], 
            ['Carlos Sanchez', 'CGGGGCTAAAATTTTTTACGATCG']]

subcadena = "CGTTTAATG"

def encontrar_culpable(subcadena: str, matriz_adn: list) -> str:
    longitud_subcadena = len(subcadena)
    bandera_culpable = True
    mensaje = ""

    for i in range(len(matriz_adn)):
        cadena_adn = matriz_adn[i][1]

        for j in range(len(cadena_adn)):
            segmento = cadena_adn[j:j + longitud_subcadena]
            if segmento == subcadena:
                mensaje = (f"El/la culpable se llama {matriz_adn[i][0]}"
                            f", y su adn es {matriz_adn[i][1]}")
                bandera_culpable = False

    if bandera_culpable:
        mensaje = "SON TODOS INOCENTES"

    return mensaje

culpable = encontrar_culpable(subcadena, lista_adn)

print(culpable)