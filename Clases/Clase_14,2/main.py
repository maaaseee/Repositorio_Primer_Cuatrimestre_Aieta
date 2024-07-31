from empleado import *
from os import system
from menus import *

bandera = True

extraccion = extract_config_json("config.json")
config = extraccion[0]

lista_empleados = []
lista_despedidos = []

parser_csv("empleados.csv", lista_empleados)

last_id = get_last_id(lista_empleados)
bajas = config["bajas"]
reportes_salario = config["reportes_salario"]
reportes_apellido = config["reportes_apellido"]

# system("cls")
while bandera:
    opcion = mostrar_opciones()
    if opcion == 1:
        if len(lista_empleados) < 120:
            ingresar = ingresar_empleado_lista(lista_empleados, last_id)
            if ingresar == None:
                enviar_mensaje_error(1)
            else:
                last_id = ingresar
            ask_and_clear()

        else:
            print("\nLa lista de empleados está llena.\n")
            clear_and_wait(5)

    elif opcion == 2:
        if len(lista_empleados) > 0:
            modificacion = modificar_empleado(lista_empleados)
            if modificacion == False:
                enviar_mensaje_error(1)
            ask_and_clear()
        
        else:
            enviar_mensaje_error(2)
            clear_and_wait(5)

    elif opcion == 3:
        if len(lista_empleados) > 0:
            despedido = eliminar_empleado(lista_empleados, "ID", bajas + 1, lista_despedidos)
            if despedido == False:
                enviar_mensaje_error(1)
            else:
                bajas = despedido
            ask_and_clear()
        
        else:
            enviar_mensaje_error(2)
            clear_and_wait(5)

    elif opcion == 4:
        if len(lista_empleados) > 0:
            mostrar_lista_empleados(lista_empleados)
            ask_and_clear()
        
        else:
            enviar_mensaje_error(2)
            clear_and_wait(5)

    elif opcion == 5:
        if len(lista_empleados) > 0:
            promedio = calcular_promedio_key(lista_empleados, "Salario")
            print(f"\nEl promedio de salarios de todos los empleados es de: ${promedio}\n")
            ask_and_clear()
        
        else:
            enviar_mensaje_error(2)
            clear_and_wait(5)

    elif opcion == 6:
        if len(lista_empleados) > 0:
            buscar_por_dni(lista_empleados)
            ask_and_clear()
        
        else:
            enviar_mensaje_error(2)
            clear_and_wait(5)

    elif opcion == 7:
        if len(lista_empleados) > 1:
            ordenar_lista(lista_empleados)
            ask_and_clear()
        elif len(lista_empleados) == 1:
            print("\nSolo hay un empleado en la lista. No es necesario ordenarlos.\n")
            clear_and_wait(5)
        else:
            enviar_mensaje_error(2)
            clear_and_wait(5)

    elif opcion == 8:
        if len(lista_empleados) > 0:
            reporte = generar_reporte_salario(lista_empleados, "Salario")
            if reporte == False:
                enviar_mensaje_error(7)
                clear_and_wait(5)
            else:
                reportes_salario = reporte
        else:
            enviar_mensaje_error(2)
            clear_and_wait(5)

    elif opcion == 9:
        if len(lista_empleados) > 0:
            reporte = generar_reporte_salario(lista_empleados, "Apellido")
            if reporte == False:
                enviar_mensaje_error(7)
                clear_and_wait(5)
            else:
                reportes_apeliido = reporte
        else:
            enviar_mensaje_error(2)
            clear_and_wait(5)

    elif opcion == 10:
        eleccion_empleado = input("Ingrese SI/NO si desea salir:\n").upper()
        if eleccion_empleado == "SI":
            bandera = False
            print("\nSaliendo del programa...")
            clear_and_wait(3)
        
        elif eleccion_empleado == "NO":
            system("pause")
            system("cls")
        
        else:
            for _ in range(2):
                eleccion_empleado = input("Ingrese SI/NO si desea salir:\n").upper()
                if eleccion_empleado == "SI":
                    bandera = False
                    print("\nSaliendo del programa...")
                    clear_and_wait(3)
                elif eleccion_empleado == "NO":
                    system("pause")
                    system("cls")

    elif opcion == None:
        system("pause")
        system("cls")

    else:
        system("pause")
        system("cls")

overwrite_csv("empleados.csv", lista_empleados)

config = {"last_id": last_id, "bajas": bajas, "reportes_salario": reportes_salario, "reportes_apellido": reportes_apellido}

overwrite_json("config.json", config)

# create_bajas_json("bajas.json", lista_despedidos)