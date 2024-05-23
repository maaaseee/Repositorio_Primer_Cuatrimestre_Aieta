diccionario = {
    'nombre': 'Juan',
    'edad': 21,
    'genero': 'masculino',
    'edad': 33
}

# print(diccionario['nombre'])
# print(diccionario['genero'])

diccionario["profesion"] = "estudiante"

# edad = diccionario.pop("edad")
# print(edad)

# print(diccionario)

# print(diccionario.keys())
# print(diccionario.values())
# print(diccionario.items())

################################################################################################

for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")