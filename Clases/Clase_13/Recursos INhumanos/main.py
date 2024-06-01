from empleados import *
from os import system
from menus import *

bandera = True

lista_empleados = [
{"id":1,"nombre":"Cynthea","apellido":"Zarfai","dni":8510287,"puesto":"VP Marketing","salario":1480693.9},
{"id":2,"nombre":"Gisela","apellido":"Felstead","dni":5637974,"puesto":"Business Systems Development Analyst","salario":1495869.57},
{"id":3,"nombre":"Sophey","apellido":"Bernollet","dni":7435874,"puesto":"Senior Sales Associate","salario":1449795.04},
{"id":4,"nombre":"Pieter","apellido":"Cominello","dni":5725298,"puesto":"Operator","salario":398865.62},
{"id":5,"nombre":"Colleen","apellido":"Awmack","dni":8463930,"puesto":"Registered Nurse","salario":355302.98},
{"id":6,"nombre":"Ravi","apellido":"Eller","dni":9588904,"puesto":"Account Coordinator","salario":421655.32},
{"id":7,"nombre":"Kerk","apellido":"Renon","dni":7589187,"puesto":"Nuclear Power Engineer","salario":274067.25},
{"id":8,"nombre":"Zach","apellido":"Theseira","dni":6210134,"puesto":"Safety Technician IV","salario":848155.45},
{"id":9,"nombre":"Perren","apellido":"Bollen","dni":6987462,"puesto":"Chief Design Engineer","salario":1008071.31},
{"id":10,"nombre":"Pollyanna","apellido":"Thebeaud","dni":6773503,"puesto":"Geological Engineer","salario":975500.41},
{"id":11,"nombre":"Roderic","apellido":"Merington","dni":6126389,"puesto":"Executive Secretary","salario":915265.29},
{"id":12,"nombre":"Delinda","apellido":"Gerb","dni":6434457,"puesto":"Geological Engineer","salario":916305.17},
{"id":13,"nombre":"Jocelin","apellido":"Hannan","dni":6099296,"puesto":"Account Executive","salario":1023710.91},
{"id":14,"nombre":"Dori","apellido":"Toth","dni":8008983,"puesto":"Media Manager III","salario":874456.77},
{"id":15,"nombre":"Hastings","apellido":"Mace","dni":7270435,"puesto":"Civil Engineer","salario":706397.11},
{"id":16,"nombre":"Martha","apellido":"Larive","dni":6029079,"puesto":"Sales Representative","salario":1070157.98},
{"id":17,"nombre":"Beckie","apellido":"Klimt","dni":8474227,"puesto":"Payment Adjustment Coordinator","salario":817468.77},
{"id":18,"nombre":"Lurline","apellido":"Adelberg","dni":6033389,"puesto":"Database Administrator III","salario":1360247.16},
{"id":19,"nombre":"Robena","apellido":"Ullrich","dni":6905629,"puesto":"Geologist II","salario":1314243.84},
{"id":20,"nombre":"Xylina","apellido":"Avrahamov","dni":6164631,"puesto":"Assistant Professor","salario":434321.31}
]
lista_despedidos = []

system("cls")
while bandera:
    opcion = mostrar_opciones()
    if opcion == 1:
        if len(lista_empleados) < 20:
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