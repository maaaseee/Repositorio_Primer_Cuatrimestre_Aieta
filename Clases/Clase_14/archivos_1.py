'''
Crear una función que reciba como parámetros una lista de números y el path de un archivo.
La misma deberá guardar la lista en un archivo de texto.
'''
import random
def guardar_lista(lista: list, path: str):
    with open(path, 'w') as archivo:
        for elemento in lista:
            if elemento == lista[0]:
                archivo.write(str(elemento))
            else:
                archivo.write('\n' + str(elemento))

def guardar_lista_2(lista: list, path: str):
    listita = []
    for elemento in lista:
        listita.append(str(elemento))
    cadena = ",".join(listita)

    with open(path, 'w', encoding="utf8") as archivo:
        archivo.write(cadena)

lista_numeros = []
for _ in range(15):
    numero = random.randint(0, 100)
    numero = lista_numeros.append(numero)

guardar_lista(lista_numeros, "Clases/Clase_14/lista_numeros_2.txt")
guardar_lista_2(lista_numeros, "Clases/Clase_14/lista_numeros.txt")


'''
Crear una función que reciba como parámetro el path de un archivo.
La misma deberá leer el archivo del ejercicio anterior, solo dejando pasar a la lista los números múltiplos de 2.
'''

def leer_archivo(path: str):
    lista_numeros = []
    with open(path, 'r') as archivo:
        for linea in archivo:
            if int(linea) % 2 == 0 and int(linea) != 0:
                lista_numeros.append(int(linea))

    return lista_numeros

def leer_archivo_2(path: str):
    cadenita = ""
    with open(path, 'r') as archivo:
        for linea in archivo:
            cadenita += linea
    listita = cadenita.split(",")

    lista_numeros = []
    for numero in listita:
        if int(numero) % 2 == 0:
            lista_numeros.append(int(numero))
    
    return lista_numeros

# print(leer_archivo("Clases/Clase_14/lista_numeros_2.txt"))
# print(leer_archivo_2("Clases/Clase_14/lista_numeros.txt"))

'''
Crear una función que reciba como parámetros dos paths: uno correspondiente a un archivo de origen y
otro correspondiente a un archivo de destino.

La función debe leer el contenido del archivo de origen y luego transcribirlo en el archivo de destino.
En caso de error la función retornará algún tipo de código de error indicando que paso.
'''

poema = "Mis pasos en esta calle Resuenan En otra calle Donde Oigo mis pasos Pasar en esta calle Donde Sólo es real la niebla."

def traslado_de_texto(path_1: str, path_2: str):
    try:
        with open(path_1, 'r', encoding="utf8") as archivo:
            contenido = archivo.read()
    except:
        print("No se pudo leer correctamente el primer path")
        return None

    try:
        with open(path_2, 'w', encoding="utf8") as archivo:
            archivo.write(contenido)
        archivito = open(path_2, 'r', encoding="utf8")
        print(archivito.read())

    except:
        print("No se pudo trasladar el texto al segundo archivo.")
        return None
    
    return True

archivo = traslado_de_texto("Clases/Clase_14/poema.txt", "Clases/Clase_14/poema_2.txt")

'''
Crear una función llamada contar_elementos que recibe como parámetro el path de un archivo de texto que contiene un poema.
La función deberá contar la cantidad de líneas, la cantidad de palabras y la cantidad de caracteres que contiene el poema.
La función retornará un diccionario con los datos obtenidos.
# '''
def contar_elementos(path: str):
    diccionario_poema = {
    "lineas" : 0,
    "palabras" : 0,
    "caracteres" : 0
    }
    with open(path, 'r', encoding="utf8") as archivo:
        for linea in archivo:
            diccionario_poema["lineas"] += 1
            lista = linea.split(" ")
            diccionario_poema["palabras"] += len(lista)
            for caracter in linea:
                if ord(caracter) != ord(" "):
                    diccionario_poema["caracteres"] += 1

    print(diccionario_poema)

contar_elementos(r"Clases\Clase_14\poema.txt")