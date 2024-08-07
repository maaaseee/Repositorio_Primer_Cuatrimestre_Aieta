from empleados import *
from os import system
from menus import *

bandera = True

lista_empleados = [
{'ID': 1, 'Nombre':'Juan', 'Apellido': 'Aerez', 'DNI': 12345678, 'Puesto': 'Ingeniero', 'Salario': 50000.0},
{'ID': 2, 'Nombre':'Maria', 'Apellido': 'Aomez', 'DNI': 87654321, 'Puesto': 'Analista', 'Salario': 45000.0},
{'ID': 3, 'Nombre':'Carlos', 'Apellido': 'Sanchez', 'DNI': 23456789, 'Puesto': 'Gerente', 'Salario': 70000.0},
{'ID': 4, 'Nombre':'Ana', 'Apellido': 'Lopez', 'DNI': 98765432, 'Puesto': 'Desarrollador', 'Salario': 55000.0},
{'ID': 19, 'Nombre':'Luis', 'Apellido': 'Martinez', 'DNI': 34567890, 'Puesto': 'Diseñador', 'Salario': 40000.0}
]
lista_despedidos = [
{'ID': 20, 'Nombre':'Federico', 'Apellido': 'Aieta', 'DNI': 34576890, 'Puesto': 'Diseñador', 'Salario': 45000.0}
]

system("cls")
while bandera:
    opcion = mostrar_opciones()
    a = max_value_id(lista_empleados)
    b = max_value_id(lista_despedidos)
    id_mx = last_id(a, b)
    if opcion == 1:
        if len(lista_empleados) < 20:
            ingresar = ingresar_empleado_lista(lista_empleados, id_mx)
            if ingresar == False:
                enviar_mensaje_error(1)
            clear_and_wait(5)

        else:
            print("\nLa lista de empleados está llena.\n")
            clear_and_wait(5)

    elif opcion == 2:
        if len(lista_empleados) > 0:
            modificacion = modificar_empleado(lista_empleados)
            if modificacion == False:
                enviar_mensaje_error(1)
            clear_and_wait(5)
        
        else:
            enviar_mensaje_error(2)
            clear_and_wait(5)

    elif opcion == 3:
        if len(lista_empleados) > 0:
            eliminar_empleado(lista_empleados, lista_despedidos, "ID")
            clear_and_wait(5)
        
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
            buscar_empleado_por_dni(lista_empleados)
            ask_and_clear()
        
        else:
            enviar_mensaje_error(2)
            clear_and_wait(5)

    elif opcion == 7:
        if len(lista_empleados) > 1:
            ordenar_lista_empleados(lista_empleados)
        elif len(lista_empleados) == 1:
            print("\nSolo hay un empleado en la lista. No es necesario ordenarlos.\n")
            clear_and_wait(5)
        else:
            enviar_mensaje_error(2)
            clear_and_wait(5)

    elif opcion == 8:
        eleccion_empleado = input("Ingrese SI/NO si desea "
                                "cambiar el dato del empleado:\n").upper()
        if eleccion_empleado == "SI":
            bandera = False
            print("\nSaliendo del programa...")
            clear_and_wait(3)
        
        elif eleccion_empleado == "NO":
            system("cls")
        
        else:
            for _ in range(2):
                eleccion_empleado = input("Ingrese SI/NO si desea "
                                            "cambiar el dato del empleado:\n").upper()
                if eleccion_empleado == "SI":
                    bandera = False
                    print("\nSaliendo del programa...")
                    clear_and_wait(3)
                elif eleccion_empleado == "NO":
                    system("cls")

    else:
        system("pause")
        system("cls")