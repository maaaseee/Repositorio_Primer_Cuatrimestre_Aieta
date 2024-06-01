# QUEVEDO || BZRP Music Sessions #52,
# 827192970,
# 204,
# https://i.ytimg.com/vi/A_g3lMcWVy0/sddefault.jpg,
# https://youtube.com/watch?v=A_g3lMcWVy0,
# 2022-07-06 00:00:00
import re

def parser_csv(path: str, lista) -> list:
    lista = []
    exito = True
    try:
        with open(path, "r", encoding = "utf8") as archivo:
            for linea in archivo:
                registro = re.split(",|\n", linea)
                diccionario = {}
                diccionario["titulo"] = registro[0]
                diccionario["vistas"] = registro[1]
                diccionario["duracion"] = registro[2]
                diccionario["miniatura"] = registro[3]
                diccionario["url"] = registro[4]
                diccionario["fecha"] = registro[5]
                lista.append(diccionario)
    except:
        exito = False


    return exito

def generar_csv(path: str, lista: list):
    with open(path, "w", encoding = "utf8") as archivo:
        for tema in lista:
            linea = f"{tema["titulo"]} - {tema["vistas"]} - {tema["duracion"]} - {tema["url"]}\n"
            archivo.write(linea)

lista_temas = []
retorno = parser_csv("Material\Parser_archivos\data.csv", lista_temas)

if retorno:
    for tema in lista_temas:
        print(f"{tema["titulo"]}")

else:
    print("El archivo no existe")

# otra_lista = [lista_temas[0], lista_temas[1], lista_temas[2], lista_temas[3]]

# generar_csv("Material\Parser_archivos\copia_data.csv", otra_lista)


