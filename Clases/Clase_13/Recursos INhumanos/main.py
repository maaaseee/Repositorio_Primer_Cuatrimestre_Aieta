from empleados import *
from os import system
from menus import *

bandera = True

lista_empleados = [{'ID': 19, 'Nombre':'Luis', 'Apellido': 'Martinez', 'DNI': 34567890, 'Puesto': 'Diseñador', 'Salario': 40000.0}]
lista_despedidos = []

system("cls")
while bandera:
    opcion = mostrar_opciones()
    if opcion == 1:
        if len(lista_despedidos) < 21:
            ingresar_empleado_lista(lista_empleados, lista_despedidos)
            clear_and_wait()
        else:
            print("La lista de empleados está llena.")
            clear_and_wait()

    elif opcion == 2:
        if len(lista_empleados) > 0:
            modificar_empleado(lista_empleados)
            clear_and_wait()
        else:
            print("No hay empleados en la lista. Por favor, antes de usar esta "
                "función, ingrese un empleado")
            clear_and_wait()

    elif opcion == 3:
        if len(lista_empleados) > 0:
            eliminar_empleado(lista_empleados, lista_despedidos)
            clear_and_wait()
        else:
            print("No hay empleados en la lista. Por favor, antes de usar esta "
                "función, ingrese un empleado")
            clear_and_wait()

    elif opcion == 4:
        if len(lista_empleados) > 0:
            mostrar_lista_empleados(lista_empleados)
            ask_and_clear()
        else:
            print("No hay empleados en la lista. Por favor, antes de usar esta "
                "función, ingrese un empleado")
            clear_and_wait()

    elif opcion == 5:
        if len(lista_empleados) > 0:
            promedio = calcular_promedio_salario(lista_empleados)
            print(f"\nEl promedio de salarios de todos los empleados es de: ${promedio}\n")
            ask_and_clear()
        else:
            print("No hay empleados en la lista. Por favor, antes de usar esta "
                "función, ingrese un empleado")
            clear_and_wait()

    elif opcion == 6:
        if len(lista_empleados) > 0:
            buscar_empleado_por_dni(lista_empleados)
            ask_and_clear()
        else:
            print("No hay empleados en la lista. Por favor, antes de usar esta "
                "función, ingrese un empleado")
            clear_and_wait()

    elif opcion == 7:
        if len(lista_empleados) > 1:
            ordenar_lista_empleados(lista_empleados)
        elif len(lista_empleados) == 1:
            print("Solo hay un empleado en la lista. No es necesario ordenarlos.")
            clear_and_wait()
        else:
            print("No hay empleados en la lista. Por favor, antes de usar esta "
                "función, ingrese un empleado")
            clear_and_wait()

    elif opcion == 8:
        eleccion_empleado = input("Ingrese SI/NO si desea "
                                "cambiar el dato del empleado:\n").upper()
        if eleccion_empleado == "SI":
            bandera = False
            print("Saliendo del programa...")
            clear_and_wait()
        elif eleccion_empleado == "NO":
            system("cls")
        else:
            for _ in range(2):
                eleccion_empleado = input("Ingrese SI/NO si desea "
                                            "cambiar el dato del empleado:\n").upper()
                if eleccion_empleado == "SI":
                    bandera = False
                    print("Saliendo del programa...")
                    clear_and_wait()
                elif eleccion_empleado == "NO":
                    system("cls")

    else:
        system("pause")
        system("cls")