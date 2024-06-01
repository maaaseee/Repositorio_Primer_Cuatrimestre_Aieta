from input_paquete.input_func import *
import math

puestos_de_trabajo = ["Gerente", "Supervisor", "Analista", "Encargado", "Asistente"]

def crear_empleado(id: int, nombre: str, apellido: str, dni: int, puesto: str,
                    salario: int) -> dict:
    diccionario_empleado = {
        "ID" : id,
        "Nombre" : nombre,
        "Apellido" : apellido,
        "DNI" : dni,
        "Puesto" : puesto,
        "Salario" : salario
    }

    return diccionario_empleado

def ingresar_empleado_lista(lista_empleados: list[dict], lista_despedidos: list[dict]):
    id = (len(lista_empleados)) + len(lista_despedidos) + 1

    nombre = get_string("Ingrese el nombre: ", 1, 20, 
                        "El nombre ingresado no es válido", 3)
    if nombre == None:
        print("El empleado no fue ingresado correctamente.")
        return None
    
    apellido = get_string("Ingrese el apellido: ", 1, 20,
                        "El apellido ingresado no es válido", 3)
    if apellido == None:
        print("El empleado no fue ingresado correctamente.")
        return None
    
    dni = get_int("Ingrese su dni: ", "El DNI ingresado no es válido."
                " Por favor, vuelva a ingresarlo.",
                5000000, 99999999,
                "El DNI ingresado no es válido", 3)
    if dni == None:
        print("El empleado no fue ingresado correctamente.")
        return None

    puesto = get_string_excluyente("Ingrese su puesto: ", 5, 9, puestos_de_trabajo,
                        "El puesto ingresado no es válido", 3)
    if puesto == None:
        print("El empleado no fue ingresado correctamente.")
        return None
    
    salario = get_int("Ingrese su salario: ", "El salario ingresado no es válido."
                        " Por favor, vuelva a ingresarlo.",
                        234315, math.inf, "El salario ingresado no es válido.", 3)
    if salario == None:
        print("El empleado no fue ingresado correctamente.")
        return None

    diccionario_empleado = crear_empleado(id, nombre, apellido, dni, puesto, salario)

    lista_empleados.append(diccionario_empleado)

    print("\nEl empleado fue ingresado exitosamente.\n")

def eliminar_empleado(lista_empleados: list[dict], lista_despedidos: list[dict]):
    solicitar_id = get_int("Ingrese la ID del empleado: ", "El ID ingresado no es válido", 1,
                            math.inf, "El ID ingresado no es válido", 3)
    
    if solicitar_id == None:
        print("El ID no fue ingresado correctamente. Volviendo al menú...")
    else:
        eliminado = None
        for empleado in lista_empleados:
            if empleado["ID"] == solicitar_id:
                eliminado = empleado
                print("\nEl empleado fue removido exitosamente.\n")

        if eliminado != None:
            lista_despedidos.append(eliminado)
            lista_empleados.remove(eliminado)
        else:
            print("El empleado no fue encontrado en la lista de empleados.")

def modificar_empleado(lista_empleados: list[dict]):
    verde = "\033[0;32m"
    reset = "\033[0m"
    opciones = f"{verde}\n- Apellido\n- Nombre\n- DNI\n- Puesto\n- Salario\n{reset}"
    keys_lista = list(lista_empleados[0].keys())

    solicitar_id = get_int("Ingrese su ID: ", "El ID ingresado no es válido",
                            1, math.inf, "El ID ingresado no es válido", 3)
    
    if solicitar_id == None:
        print("El ID no fue ingresado correctamente.")
    else:
        for i in range(len(lista_empleados)):
            if lista_empleados[i]["ID"] == solicitar_id:
                eleccion = get_string_excluyente(f"Ingrese el dato a modificar:\n{opciones}\n",
                                                1, 10, keys_lista,
                                                "El dato ingresado no es válido", 3)
                eleccion_mayus = eleccion.upper()

                auxiliar = {
                    "ID": lista_empleados[i]["ID"],
                    "Nombre": lista_empleados[i]["Nombre"],
                    "Apellido": lista_empleados[i]["Apellido"],
                    "DNI": lista_empleados[i]["DNI"],
                    "Puesto": lista_empleados[i]["Puesto"],
                    "Salario": lista_empleados[i]["Salario"]
                }

                empleado_modificado = modificar_empleado_opciones_keys(eleccion_mayus, 
                                                                    lista_empleados[i])
                
                print(f"Desea modificar el dato de {eleccion} del siguiente empleado:")
                mostrar_empleado(auxiliar)
                print("Y cambiarlo por:")
                mostrar_empleado(empleado_modificado)

                eleccion_empleado = input("Ingrese SI/NO si desea "
                                            "cambiar el dato del empleado:\n").upper()

                if eleccion_empleado == "SI":
                    lista_empleados[i] = empleado_modificado
                    print("\nEl empleado fue modificado exitosamente.\n")
                
                elif eleccion_empleado == "NO":
                    lista_empleados[i] = auxiliar
                    print("\nEl cambio fue revertido exitosamente.\n")
                
                else:
                    bandera = False
                    for _ in range(3):
                        eleccion_empleado = input("Ingrese SI/NO si desea "
                                            "cambiar el dato del empleado:\n").upper()
                        if eleccion_empleado == "SI":
                            lista_empleados[i] = empleado_modificado
                            bandera = True
                            print("\nEl empleado fue modificado exitosamente.\n")
                            break
                        
                        elif eleccion_empleado == "NO":
                            lista_empleados[i] = auxiliar
                            bandera = True
                            print("\nEl cambio fue revertido exitosamente.\n")
                            break
                    
                    if bandera == False:
                        print("\nNo se ha indicado si se desea modificar al empleado."
                            " Volviendo al menú...\n")
                        lista_empleados[i] = auxiliar

def modificar_empleado_opciones_keys(eleccion_mayus: str, empleado_modificado):
    match eleccion_mayus:
        case "APELLIDO":
            apellido = get_string("\nIngrese el apellido: ", 1, 20,
                                    "El apellido ingresado no es válido", 3)
            if apellido == None:
                print("El empleado no fue ingresado correctamente.")
                return None
            else:
                empleado_modificado["Apellido"] = apellido
                return empleado_modificado

        case "NOMBRE":
            nombre = get_string("\nIngrese el nombre: ", 1, 20,
                                    "El nombre ingresado no es válido", 3)
            if nombre == None:
                print("El empleado no fue ingresado correctamente.")
                return None
            else:
                empleado_modificado["Nombre"] = nombre
                return empleado_modificado

        case "DNI":
            dni = get_int("\nIngrese su DNI: ", "El DNI ingresado no es válido",
                            5000000, 99999999, 
                            "El DNI ingresado no es válido. Por favor,"
                            " vuelva a ingresarlo.", 3)
            if dni == None:
                print("El empleado no fue ingresado correctamente.")
                return None
            else:
                empleado_modificado["DNI"] = dni
                return empleado_modificado
            
        case "PUESTO":
            puesto = get_string_excluyente("\nIngrese su puesto: ", 5, 9, puestos_de_trabajo,
                                            "El puesto ingresado no es válido", 3)
            if puesto == None:
                print("El empleado no fue ingresado correctamente.")
                return None
            else:
                empleado_modificado["Puesto"] = puesto
                return empleado_modificado
            
        case "SALARIO":
            salario = get_int("\nIngrese su salario: ",
                            "El salario ingresado no es válido. Por favor, vuelva a ingresarlo.",
                            234315, math.inf, "El salario ingresado no es válido", 3)
            if salario == None:
                print("El empleado no fue ingresado correctamente.")
                return None
            else:
                empleado_modificado["Salario"] = salario
                return empleado_modificado

def mostrar_empleado(un_empleado: dict):
    verde = "\033[38;5;22m"
    reset = "\033[0m"

    print("+---+--------------------+--------------------+---------+--------------+--------------+")
    print(f"| {verde}ID{reset}|              {verde}Nombre{reset}|            {verde}Apellido{reset}|"
        f"      {verde}DNI{reset}|        {verde}Puesto{reset}|       {verde}Salario{reset}|")

    print("+---+--------------------+--------------------+---------+--------------+--------------+")
    print(f"| {un_empleado["ID"]}|{un_empleado["Nombre"]:>20}|{un_empleado["Apellido"]:>20}"
        f"|{un_empleado["DNI"]:>9}|{un_empleado["Puesto"]:>14}|${un_empleado["Salario"]:>13.0f}|")
    print("+---+--------------------+--------------------+---------+--------------+--------------+")
    

def mostrar_lista_empleados(lista_empleados: list[dict]):
    verde = "\033[38;5;22m"
    reset = "\033[0m"

    print("+---+--------------------+--------------------+---------+--------------+--------------+")
    print(f"| {verde}ID{reset}|              {verde}Nombre{reset}|            {verde}Apellido{reset}|"
        f"      {verde}DNI{reset}|        {verde}Puesto{reset}|       {verde}Salario{reset}|")
    print("+---+--------------------+--------------------+---------+--------------+--------------+")

    for empleado in lista_empleados:
        id = empleado["ID"]
        nombre = empleado["Nombre"]
        apellido = empleado["Apellido"]
        dni = empleado["DNI"]
        puesto = empleado["Puesto"]
        salario = empleado["Salario"]
        signo_pesos = f"{verde}${reset}"

        mostrar = "|{:>3}|{:>20}|{:>20}|{:>9}|{:>14}|{:}{:>13.0f}|".format(id, nombre, apellido, dni, puesto, signo_pesos, salario)
        print(mostrar)
        print("+---+--------------------+--------------------+---------+--------------+--------------+")

def calcular_promedio_salario(lista_empleados:list[dict]):
    acumulador = 0
    for empleado in lista_empleados:
        acumulador += empleado["Salario"]

    promedio = acumulador / len(lista_empleados)
    return promedio

def buscar_empleado_por_dni(lista_empleados: list[dict]):
    if len(lista_empleados) > 0:
        solicitar_dni = get_int("Ingrese su dni: ",
                                "El DNI ingresado no es válido. Por favor, vuelva a ingresarlo.",
                                5000000, 99999999, "El DNI ingresado no es válido", 3)
        
        if solicitar_dni == None:
            print("El DNI no fue ingresado correctamente.")
        else:
            for empleado in lista_empleados:
                if empleado["DNI"] == solicitar_dni:
                    mostrar_empleado(empleado)
    else:
        print("\nTodavia no hay empleados para ordenar.")

def ordenar_lista_empleados(lista_empleados: list[dict], keys_datos: list):
    verde = "\033[0;32m"
    violeta = "\033[0;35m"
    reset = "\033[0m"
    opciones = f"{verde}\n- Apellido\n- Nombre\n- Salario\n{reset}"

    eleccion = get_string_excluyente(f"Ingrese el dato con el que desea "
                                    f"ordenar la lista{opciones}",
                                    1, 10, keys_datos,
                                    "El dato ingresado no es válido", 3)
    
    if eleccion == None:
        print("El dato ingresado no es válido para ordenar la lista")
    else:
        if eleccion.upper() == "APELLIDO":
            orden_de_lista = get_int(f"¿Como desea ordenar la lista?\n{violeta}1. Menor a mayor\n"
                                    f"2. Mayor a menor{reset}\nElegir el número: ",
                                    "ERROR. Por favor, vuelva a elegir una opción",
                                    1, 2, "No se pudo realizar la operacion solicitada", 3)
            if orden_de_lista == 1:
                ordenar_lista_empleados_menor_a_mayor(lista_empleados, "Apellido")
                mostrar_lista_empleados(lista_empleados)
            elif orden_de_lista == 2:
                ordenar_lista_empleados_mayor_a_menor(lista_empleados, "Apellido")
                mostrar_lista_empleados(lista_empleados)
            else:
                print("No se pudo ordenar la lista.")

        elif eleccion.upper() == "NOMBRE":
            orden_de_lista = get_int(f"¿Como desea ordenar la lista?\n{violeta}1. Menor a mayor\n"
                                    f"2. Mayor a menor{reset}\nElegir el número: ",
                                    "ERROR. Por favor, vuelva a elegir una opción",
                                    1, 2, "No se pudo realizar la operacion solicitada", 3)
            if orden_de_lista == 1:
                ordenar_lista_empleados_menor_a_mayor(lista_empleados, "Nombre")
                mostrar_lista_empleados(lista_empleados)
            elif orden_de_lista == 2:
                ordenar_lista_empleados_mayor_a_menor(lista_empleados, "Nombre")
                mostrar_lista_empleados(lista_empleados)
            else:
                print("No se pudo ordenar la lista.")

        elif eleccion.upper() == "SALARIO":
            orden_de_lista = get_int(f"¿Como desea ordenar la lista?\n{violeta}1. Menor a mayor\n"
                                    f"2. Mayor a menor{reset}\nElegir el número: ",
                                    "ERROR. Por favor, vuelva a elegir una opción",
                                    1, 2, "No se pudo realizar la operacion solicitada", 3)
            if orden_de_lista == 1:
                ordenar_lista_empleados_menor_a_mayor(lista_empleados, "Salario")
                mostrar_lista_empleados(lista_empleados)
            elif orden_de_lista == 2:
                ordenar_lista_empleados_mayor_a_menor(lista_empleados, "Salario")
                mostrar_lista_empleados(lista_empleados)
            else:
                print("No se pudo ordenar la lista.")


def ordenar_lista_empleados_menor_a_mayor(lista: list[dict], key: dict):
    # Ordena la lista segun la key ingresada
    # Lo hace de menor a mayor
    largo_de_lista = len(lista)
    for i in range(largo_de_lista):
        for j in range(0, largo_de_lista - i - 1):
            if lista[j][key] > lista[j + 1][key]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def ordenar_lista_empleados_mayor_a_menor(lista: list[dict], key: dict):
    # Ordena la lista segun la key ingresada
    # Lo hace de mayor a menor
    largo_de_lista = len(lista)
    for i in range(largo_de_lista):
        for j in range(0, largo_de_lista - i - 1):
            if lista[j][key] < lista[j + 1][key]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]