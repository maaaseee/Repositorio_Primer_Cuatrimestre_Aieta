'''Datos correspondientes de cada paciente:

ID (int)
Nombre (str)
Apellido (str)
Edad (int)
Altura (int) (en centímetros)
Peso (float) (en kilogramos)
DNI (int)
Grupo sanguíneo (str)
'''
from menus import *
from pacientes import *

lista_pacientes = []
lista_bajas = []

datos = parser_csv("pacientes_datos", lista_pacientes)

config = extract_config_json("config")
last_id = config["last_id"]
reporte_n = config["reportes"]

bandera = True

while bandera:
    system("cls")
    if datos == False:
        clear_and_wait(5)
    opcion = mostrar_opciones()
    if opcion == 1:
        ingresar = ingresar_paciente_lista(lista_pacientes, last_id)
        if ingresar == None:
            enviar_mensaje_error(1)
        else:
            config["last_id"] = ingresar
        ask_and_clear()

    elif opcion == 2:
        if len(lista_pacientes) > 0:
            modificacion = modificar_paciente(lista_pacientes, "DNI")
            ask_and_clear()
        
        else:
            enviar_mensaje_error(2)
            clear_and_wait(5)

    elif opcion == 3:
        if len(lista_pacientes) > 0:
            despedido = eliminar_paciente(lista_pacientes, lista_bajas, "DNI")
            if despedido == False:
                enviar_mensaje_error(1)
            else:
                bajas = despedido
            ask_and_clear()
        
        else:
            enviar_mensaje_error(2)
            clear_and_wait(5)

    elif opcion == 4:
        if len(lista_pacientes) > 0:
            mostrar_lista(lista_pacientes)
            ask_and_clear()
        
        else:
            enviar_mensaje_error(2)
            clear_and_wait(5)

    elif opcion == 5:
        if len(lista_pacientes) > 1:
            ordenar_lista(lista_pacientes)
            ask_and_clear()
        
        elif len(lista_pacientes) == 1:
            print("\nSolo hay un empleado en la lista. No es necesario ordenarlos.\n")
            clear_and_wait(5)
        
        else:
            enviar_mensaje_error(2)
            clear_and_wait(5)

    elif opcion == 6:
        if len(lista_pacientes) > 0:
            buscar_por_dato(lista_pacientes, "DNI")
            ask_and_clear()
        
        else:
            enviar_mensaje_error(2)
            clear_and_wait(5)

    elif opcion == 7:
        if len(lista_pacientes) > 0:
            calcular_promedio(lista_pacientes)
            ask_and_clear()
        else:
            enviar_mensaje_error(2)
            clear_and_wait(5)
    
    elif opcion == 8:
        if len(lista_pacientes) > 0:
            documento = determinar_compatibilidad(lista_pacientes, reporte_n)
            if documento != False:
                reporte_n = documento
                ask_and_clear()
            
            else:
                enviar_mensaje_error(7)
                ask_and_clear()


    elif opcion == 9:
        eleccion= input("Ingrese SI/NO si desea salir:\n").upper()
        salir = salir_del_programa(eleccion, bandera)
        bandera = salir

    else:
        system("pause")
        system("cls")

if datos != False:
    overwrite_csv("pacientes_datos", lista_pacientes)

config["last_id"] = get_last_id(lista_pacientes)
config["reportes"] = reporte_n

editar_config_json("config", config)

if len(lista_bajas) > 0:
    agregar_bajas_json("bajas", lista_bajas)