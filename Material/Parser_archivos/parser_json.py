import json

def parser_json(path: str) -> list:
    with open(path, "r") as archivo:
        diccionario = json.load(archivo)

    return diccionario["bzrp"]

def generar_json(path: str, lista: list):
    with open(path, "w", encoding = "utf8") as archivo:
        json.dump(lista, archivo, indent = 4)

mi_lista = parser_json("Material\Parser_archivos\data.json")

# print(mi_lista)

# for tema in mi_lista:
#     print(tema)

otra_lista = [mi_lista[0], mi_lista[1], mi_lista[2], mi_lista[3]]

diccionario = {}

diccionario["bzrp"] = otra_lista[0]

generar_json("Material\Parser_archivos\copia_data.json", otra_lista)