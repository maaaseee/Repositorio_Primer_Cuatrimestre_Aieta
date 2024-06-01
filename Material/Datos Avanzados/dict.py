diccionario = {
    'nombre': 'Juan',
    'edad': 21,
    'genero': 'masculino',
    'edad': 33
}

# print(diccionario['nombre'])
# print(diccionario['genero'])

# diccionario["nombre"].append("Marcela")

# edad = diccionario.pop("edad")
# print(edad)

# print(diccionario)

print(diccionario.keys())
print(diccionario.values())
print(diccionario.items())

for key in diccionario.keys():
    print(key)

################################################################################################

# for clave, valor in diccionario.items():
#     print(f"{clave}: {valor}")

# colores = {"Blanco" : (255,255,255),
#            "Negro" : (0,0,0),
#            "Rojo" : (255,0,0),
#            "Azul" : (0,0,255),
#            "Verde" : (0,255,0),
#            "Azul Claro" : (0,150,255)}

# for clave in colores.keys():
#     print(f"» {clave}")