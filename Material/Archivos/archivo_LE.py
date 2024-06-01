# #Escritura Texto
# archivo = open("mi_primer_archivo.txt","w")
# archivo.write("Hola Mundo")

# archivo.close()

# lista = ["sebas","juan", "pedro"]
# archivo = open("nombres.txt", "w")
# for nombre in lista:
#     archivo.write(f"{nombre}\n")
# archivo.close

# lista = ["sebas","juan", "pedro"]
# cadena = ""

# for nombre in lista:
#     cadena += f"{nombre}\n"

# archivo = open("nombresdos.txt", "w")
# archivo.write(cadena)
# archivo.close


# #Administrador de contexto

# with open("nombres.txt", "r") as archivo:
#     contenido = archivo.readlines()
# for nombre in contenido:
#     print(nombre.upper(), end="")

#---------


try:
    with open("nombres.txt", "r") as archivo:
        for linea in archivo:
            print(linea)
except:
    print("El archivo no existe")

print("Acá continua el programa")