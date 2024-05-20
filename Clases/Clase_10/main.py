from class_boligrafo import *

bandera_seguir = True

rojo = "\033[91m"
azul = "\033[94m"
reset = "\033[0m"

boligrafo_azul = Lapicera("Azul", "Fino")
boligrafo_rojo = Lapicera("Rojo", "Grueso")

while bandera_seguir == True:
    print("Bienvenido al menú interactivo de la 'SmartPen'")

    menu = mostrar_menu()
    match menu:
        case 1:
            boligrafo_utilizado = input("Ingrese el color del boligrafo a utilizar:\n")
            match boligrafo_utilizado:
                case "Azul":
                    boligrafo_utilizado = boligrafo_azul
                    texto_ingresado = input("Ingrese el texto a escribir:\n")
                    mensaje = boligrafo_azul.escribir(texto_ingresado)
                    print(f"{azul}{mensaje}{reset}")

                case "Rojo":
                    boligrafo_utilizado = boligrafo_rojo
                    texto_ingresado = input("Ingrese el texto a escribir:\n")
                    mensaje = boligrafo_rojo.escribir(texto_ingresado)
                    print(f"{rojo}{mensaje}{reset}")

                case _:
                    print("No existe este color")

        case 2:
            color = input("Ingrese el color del boligrafo a recargar:\n")
            cantidad = int(input("Ingrese la cantidad de tinta a cargar:\n"))
            while cantidad < 0 and cantidad > 1000000:
                cantidad = int(input("Ingrese la cantidad de tinta a cargar:\n"))

            match color:
                case "Azul":
                    color = boligrafo_azul
                    print(f"{boligrafo_azul.recargar(cantidad)}")

                case "Rojo":
                    color = boligrafo_rojo
                    print(f"{boligrafo_rojo.recargar(cantidad)}")

                case _:
                    print("No existe este color")

        case 3:
            boligrafo_utilizado = input("Ingrese el color del boligrafo que quiere revisar:\n")

            match boligrafo_utilizado:
                case "Azul":
                    print(boligrafo_azul.capacidad_tinta)

                case "Rojo":
                    print(boligrafo_rojo.capacidad_tinta)

                case _:
                    print("No existe este color")

        case 4:
            seguir = input("¿Está seguro que desea salir? Si/No \n")

            if seguir == "Si":
                bandera_seguir = False