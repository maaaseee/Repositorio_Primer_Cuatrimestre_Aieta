nombres = ["Juan","Maria", "Luis"]
apellidos = ["Lopez", "Gomez", "Ruiz"]
edades = [20, 35, 42]

with open("agenda.csv", "w") as archivo:
    for i in range(len(nombres)):
        linea = f"{nombres[i]},{apellidos[i]},{edades[i]}\n"
        archivo.write(linea)

#---------------
nombres = ["Juan","Maria", "Luis"]
apellidos = ["Lopez", "Gomez", "Ruiz"]
edades = [20, 35, 42]
linea = ""

for i in range(len(nombres)):
    linea += f"{nombres[i]},{apellidos[i]},{edades[i]}\n"
with open("agenda.csv", "w") as archivo:
    archivo.write(linea)

#----------

with open("agenda.csv", "r") as archivo:
    for linea in archivo:
        registro = linea.split(",")

#--------
import re

with open("agenda.csv", "r") as archivo:
    for linea in archivo:
        registro = re.split(",| \n", linea)