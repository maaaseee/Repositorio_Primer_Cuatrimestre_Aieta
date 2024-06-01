import json

diccionario_1 = {"nombre": "Federico", "Edad": 18}
diccionario_2 = {"nombre": "Marcela", "Edad": 55}
diccionario_3 = {"nombre": "David", "Edad": 20}

lista = [diccionario_1, diccionario_2, diccionario_3]

data = {}

data["personas"] = lista

with open("personas.json", "w") as archivo:
    json.dump(data, archivo, indent = 4)

with open("personas.json", "r") as archivo:
    data = json.load(archivo)

lista_personas = data["personas"]

print(lista_personas[0])