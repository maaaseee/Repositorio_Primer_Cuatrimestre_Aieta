from input_paquete.input_func import *
from dict_paquete.funciones import *
from menus import *
import json

# region Variables
grupo_sanguineo = ["A", "B", "AB", "O"]
verde_1 = "\033[38;5;22m"
verde_2 = "\033[0;32m"
violeta = "\033[0;35m"
reset = "\033[0m"
# endregion

#region CSV

def separar_string_csv(linea: str) -> list:
    """_summary_
    Elimina el salto de linea, y separa el string en una lista, por cada ","
    que tenga

    Args:
        linea (str): Recibe un string que proviene de un archivo CSV.

    Returns:
        list: Una lista del contenido de una sola linea, del archivo CSV
    """
    salto_de_linea = linea.strip("\n")
    lista = salto_de_linea.split(",")

    return lista

def parser_csv(path: str, lista: list) -> bool:
    """_summary_
    Parsea cada una de las lineas de un archivo CSV, y transforma los datos que
    surjan de la misma, para luego ser utilizados en la creacion de un diccionario.

    Args:
        path (str): Recibe el nombre del archivo CSV, y se asegura que ese archivo
        sea del tipo CSV.
        lista (list): La lista donde se van a cargar todos los diccionarios.

    Returns:
        bool: Un booleano, en caso de que se pueda realizar la acción, o no.
    """
    try:
        with open(f"{path}.csv", 'r', encoding="utf8") as archivo:
            for linea in archivo:
                registro = separar_string_csv(linea)
                if registro[0] != "ID":
                    dni_registro = f"{registro[3]:>08}"
                    id = int(registro[0])
                    nombre = registro[1]
                    apellido = registro[2]
                    dni = (dni_registro)
                    grupo_sanguineo = registro[4]
                    edad = int(registro[5])
                    altura = int(registro[6])
                    peso = float(registro[7])
                    diccionario = crear_paciente(id, nombre, apellido, dni,
                                                grupo_sanguineo, edad, altura, peso)
                    lista.append(diccionario)
        return True
    except FileNotFoundError:
        print(f"El archivo {path}.csv no pudo ser cargado, debido a que no existe y/o"
            " el nombre está mal ingresado.")
        return False
    

def overwrite_csv(path: str, lista: list[dict]):
    """_summary_
    Despues de finalizar el programa, sobrescribe los datos del archivo CSV, y con
    los datos otorgados por la lista.

    Args:
        path (str): Recibe el nombre del archivo CSV, y se asegura que ese archivo
        sea del tipo CSV.
        lista (list[dict]): Una lista que está compuesta por diccionarios.
    """
    try:
        with open(f"{path}.csv", "w", encoding= "utf-8") as archivo:
            lista_keys = list(lista[0].keys())
            registro_keys = ",".join(lista_keys) + "\n"
            archivo.write(registro_keys)

            for i in range(len(lista)):
                if i != len(lista) - 1:
                    string = (f"{lista[i]["ID"]},{lista[i]["Nombre"]},{lista[i]["Apellido"]},"
                        f"{lista[i]["DNI"]},{lista[i]["Grupo sanguineo"]},{lista[i]["Edad"]},"
                        f"{lista[i]["Altura"]},{lista[i]["Peso"]}\n")
                else:
                    string = (f"{lista[i]["ID"]},{lista[i]["Nombre"]},{lista[i]["Apellido"]},"
                            f"{lista[i]["DNI"]},{lista[i]["Grupo sanguineo"]},{lista[i]["Edad"]},"
                            f"{lista[i]["Altura"]},{lista[i]["Peso"]}")
                    
                archivo.write(string)

        print("Se modificó la base de datos correctamente!")
    except:
        print("No hay datos en la lista para modificar.")

# endregion

# region JSON

def extract_config_json(path: str) -> dict:
    """_summary_
    Extrae todos los datos de "config" para poder trabajar en el programa, y
    que esta informacion se guarde para futuros inicios del programa

    Args:
        path (str): Recibe el nombre del archivo, donde se guarda la configuracion del programa.

    Returns:
        dict: Devuelve el diccionario con las configuraciones del programa.
    """
    try:
        with open(f"{path}.json", 'r', encoding='utf-8') as archivo:
            data = json.load(archivo)
        extraccion = [data["config"]]
        lista = [extraccion[0]]
        return lista[0]

    except FileNotFoundError:
        data = {}
        data["config"] = {"last_id": 0,
                        "reportes": 0}
        
        with open(f"{path}.json", 'w', encoding="utf-8") as archivo:
            json.dump(data, archivo, indent= 4)
        
        return data["config"]

def get_last_id(lista: list[dict]) -> int:
    maximo = 0
    for dato in lista:
        if dato["ID"] > maximo:
            maximo = dato["ID"]

    return maximo

def editar_config_json(path: str , nuevo_diccionario: dict) -> json:
    """_summary_
    Edita todos los datos de "config" para que se guarden, y puedan ser utilizados
    en la proxima iteracion del programa.

    Args:
        path (str): Recibe el nombre del archivo, donde se guarda la configuracion del programa.
        nuevo_diccionario (dict): Donde se sobrescribió todos los datos del diccionario "config"

    Returns:
        json: Modificia un archivo JSON, y en caso de no existir, lo crea.
    """
    try:
        with open(f"{path}.json", 'r', encoding='utf-8') as archivo:
            data = json.load(archivo)
        
        data['config'] = nuevo_diccionario
        
        with open(f"{path}.json", 'w', encoding='utf-8') as archivo:
            json.dump(data, archivo, indent=4)
    
    except FileNotFoundError:
        print(f"El archivo '{path}.json' no existe.")
        data = {}
        data["config"] = nuevo_diccionario
        with open(f"{path}.json", 'w', encoding="utf-8") as archivo:
            json.dump(data, archivo, indent= 4)
    
    except json.JSONDecodeError:
        print(f"El archivo '{path}' no está en formato JSON correcto.")

def agregar_bajas_json(path: str, nuevas_bajas: list[dict]) -> json:
    """_summary_
    Crea o modifica un archivo JSON para que guarde a los pacientes dados de baja.

    Args:
        path (str): Recibe el directorio donde se cargan los diccionarios.
        nuevas_bajas (list[dict]): La lista con todos los diccionarios a agregar.
    
    Returns:
    json: Un archivo JSON con el contenido de todos los pacientes dados de baja.
    """
    try:
        with open(f"{path}.json", 'r', encoding='utf-8') as archivo:
            data = json.load(archivo)
        
        data["bajas"] += nuevas_bajas

    except FileNotFoundError:
        data = {}
        data["bajas"] = nuevas_bajas
    
    except json.JSONDecodeError:
        data = {}
        data["bajas"] = nuevas_bajas

    with open(f"{path}.json", 'w', encoding='utf-8') as archivo:
        json.dump(data, archivo, indent=4)

# endregion

# region Mostrar un solo paciente
def mostrar_cabecera_lista() -> str:
    """_summary_
    Muestra la cabecera de la lista de pacientes

    Returns:
    str: Cabecera de la lista de pacientes
    """
    print(f"+{"-"*4}+{"-"*20}+{"-"*20}+{"-"*9}+{"-"*15}+{"-"*6}+{"-"*8}+{"-"*10}+")

    print(f"|  {verde_1}ID{reset}|{" "*14}{verde_1}Nombre{reset}|{" "*12}{verde_1}Apellido{reset}|"
        f"{" "*6}{verde_1}DNI{reset}|{verde_1}Grupo sanguíneo{reset}|  {verde_1}Edad{reset}|"
        f"  {verde_1}Altura{reset}|{" "*6}{verde_1}Peso{reset}|")
    
    print(f"+{"-"*4}+{"-"*20}+{"-"*20}+{"-"*9}+{"-"*15}+{"-"*6}+{"-"*8}+{"-"*10}+")

def mostrar_paciente(paciente: dict) -> str:
    """_summary_
    Muestra los datos de un paciente en la lista de pacientes, con su respectiva cabecera.

    Args:
        paciente (dict): Un diccionario con datos de un paciente.
    Returns:
    str: El paciente con su cabecera de datos.
    """
    try:
        mostrar_cabecera_lista()
        print(f"|{paciente["ID"]:>4}|{paciente["Nombre"]:>20}|{paciente["Apellido"]:>20}"
            f"| {paciente["DNI"]:>8}|{paciente["Grupo sanguineo"]:>15}|{paciente["Edad"]:>6}|"
            f"{paciente["Altura"]:>5} cm|{paciente["Peso"]:>7} kg|")
        print(f"+{"-"*4}+{"-"*20}+{"-"*20}+{"-"*9}+{"-"*15}+{"-"*6}+{"-"*8}+{"-"*10}+")
    except TypeError:
        print("No se pudo mostrar el empleado, debido a una falla en el ingreso de datos.")

# endregion

# region Solicitudes
def solicitar_dato(tipo_de_dato: str) -> int|str|bool:
    """_summary_
    Función que, dependiendo el nombre del dato, llama a una funcion para solicitar datos.

    Args:
        tipo_de_dato (str): El nombre del dato que se va a solicitar.

    Returns:
        int|str|bool: El dato que se solicitó, y en caso de estar mal solicitado, un booleano
    """
    match tipo_de_dato:
        case "Nombre":
            dato = get_string_2("Ingrese el nombre: ", 1, 20, 3)
        case "Apellido":
            dato = get_string("Ingrese el apellido: ", 1, 20, 3)
        case "DNI":
            dato = get_int("Ingrese el DNI (Entre 4,000,000 y 99,999,999): ", "El DNI ingresado no es válido."
                " Por favor, vuelva a ingresarlo.", 4000000, 99999999,
                "\n", 3)
            if dato != None:
                dato = f"{dato:>08}"
        case "Grupo sanguineo":
            dato = get_string_excluyente_2("Ingrese su grupo sanguíneo (A, B, AB, O, con su respectivo signo): ", 2, 3, 
                        grupo_sanguineo, 3)
        case "Edad":
            dato = get_int("Ingrese la edad (Entre 1 y 120): ", "La edad ingresada no es válida."
                        " Por favor, vuelva a ingresarla.",
                        1, 120, "La edad ingresada no es válida.", 3)
        case "ID":
            dato = get_int("Ingrese la ID: ", "El ID ingresado no es válido. Por favor, "
                        "vuelva a ingresarlo.", 1, 1000, "\n", 3)
        case "Altura":
            dato = get_int("Ingrese la altura (en CM, entre 30 y 230): ", "La altura ingresada no es válida."
                        " Por favor, vuelva a ingresarla (la altura debe ser en CM).",
                        30, 230, "La altura ingresada no es válida.", 3)
        case "Peso":
            dato = get_float("Ingrese el peso (entre 10 y 300): ", "El peso ingresado no es válido."
                        " Por favor, vuelva a ingresarlo.",
                        10, 300, "El peso ingresado no es válido.", 3)
        case _:
            print("No existe un dato con ese nombre.")
            dato = False
    
    return dato

# endregion

# region Crear paciente
def crear_paciente(id: int, nombre: str, apellido: str, dni: int, grupo_sanguineo: str,
                    edad: int, altura: int, peso: float) -> dict:
    """_summary_
    Crea un diccionario, con todos los datos solicitados/extraídos, del paciente ingresado.

    Args:
        id (int): Numero de ID del paciente.
        nombre (str): Nombre del paciente.
        apellido (str): Apellido del paciente.
        dni (int): DNI del paciente.
        grupo_sanguineo (str): Grupo sanguíneo del paciente.
        edad (int): Edad del paciente.
        altura (int): Altura del paciente
        peso (float): Peso del paciente

    Returns:
        dict: Un diccionario con los datos del paciente.
    """
    diccionario = {
        "ID" : id,
        "Nombre" : nombre,
        "Apellido" : apellido,
        "DNI" : dni,
        "Grupo sanguineo" : grupo_sanguineo,
        "Edad" : edad,
        "Altura" : altura,
        "Peso" : peso
    }

    return diccionario

def ingresar_paciente_lista(lista: list[dict], last_id: int) -> bool|int:
    """
    Crea un paciente, con su respectiva solicitud de datos para cada espacio,
    y lo hace en formato de diccionario.

    Args:
        lista (list[dict]): La lista donde se agrega al paciente.
        last_id (int): La última id ingresada a la lista.

    Returns:
        bool|int: Booleano si falló el ingreso del paciente, int para sumar
        al contador de "last_id".
    """
    system("cls")
    bandera = True

    # nombre = solicitar_dato("Nombre")

    # if nombre == None:
    #     bandera = False
    # else:
    #     apellido = solicitar_dato("Apellido")

    #     if apellido == None:
    #         bandera = False
    #     else:
    #         dni = solicitar_dato("DNI")

    #         if dni == None:
    #             bandera = False
    #         else:
    #             if filtrar_dni(lista, dni):
    #                 print("\nEl DNI ingresado ya se encuentra en la base de datos.\n")
    #                 bandera = False
    #             else:
    #                 grupo_sanguineo = solicitar_dato("Grupo sanguineo")

    #                 if grupo_sanguineo == None:
    #                     bandera = False
    #                 else:
    #                     edad = solicitar_dato("Edad")

    #                     if edad == None:
    #                         bandera = False
    #                     else:
    #                         altura = solicitar_dato("Altura")

    #                         if altura == None:
    #                             bandera = False
    #                         else:
    #                             peso = solicitar_dato("Peso")

    #                             if peso == None:
    #                                 bandera = False

    solicitud_datos = {"Nombre": False, 
                       "Apellido": False, 
                       "DNI": False, 
                       "Grupo sanguineo": False, 
                       "Edad": False, 
                       "Altura": False, 
                       "Peso": False}

    for solicitud in solicitud_datos.keys():
        ingreso_dato = solicitar_dato(solicitud)
        if solicitud == "DNI":
            if filtrar_dni(lista, ingreso_dato):
                print("\nEl DNI ingresado ya se encuentra en la base de datos.\n")
                bandera = False
                break
        if ingreso_dato == False:
            bandera = False
            break
        
        solicitud_datos[solicitud] = ingreso_dato

    if bandera == True:
        id = last_id + 1
        paciente = crear_paciente(id, solicitud_datos["Nombre"], solicitud_datos["Apellido"],
                                solicitud_datos["DNI"], solicitud_datos["Grupo sanguineo"],
                                solicitud_datos["Edad"], solicitud_datos["Altura"], 
                                solicitud_datos["Peso"])
        mostrar_paciente(paciente)
        confirmacion = get_string_excluyente("¿Desea ingresar este paciente? (SI/NO)?: ",
                                            1, 2, ["si", "no"], 3).strip().upper()
        if confirmacion == "SI":
            lista.append(paciente)
            print("\nEl empleado fue ingresado exitosamente.\n")
            bandera = id
        else:
            print("\nEl empleado no fue ingresado.\n")
            bandera = False

    return bandera

# endregion

# region Modificar paciente

def modificar_paciente(lista: list[dict], key_busqueda: str) -> bool|dict:
    """_summary_
    Modifica varios datos de un paciente, que se busca dependiendo la "key" que el programa reciba.

    Args:
        lista (list[dict]): Lista compuesta de diccionarios.
        key_busqueda (str): La key con la que se va a realizar la busqueda del paciente.

    Returns:
        bool|dict: Devuelve un booleano en caso de no poder realizarse la operación,
        o un diccionario modificado
    """
    keys_lista = conseguir_keys_exclusiva(lista, "ID")
    lista_keys_2 = conseguir_keys(lista)

    bandera_modificacion = True
    
    system("cls")
    ingreso_dato = solicitar_dato(key_busqueda)
    
    if ingreso_dato == None:
        enviar_mensaje_error(4)
        bandera_modificacion = False
    
    elif ingreso_dato == False:
        enviar_mensaje_error(10)
        bandera_modificacion = False
    
    else:
        bandera_modificacion = menu_modificaciones(lista, ingreso_dato, keys_lista, key_busqueda
                                                    , lista_keys_2)

    return bandera_modificacion


def menu_modificaciones(lista: list[dict], ingreso: int , lista_keys: list, key: str, otra_lista: list) -> dict:
    """_summary_
    Abre un menú que le muestra al usuario que datos puede cambiar.

    Args:
        lista (list[dict]): La lista donde se encuentra el paciente a modificar.
        ingreso (int): El dato que ingresó el usuario para buscar al paciente.
        lista_keys (list): La lista de llaves que se pueden modificar. Sin "ID".
        key (str): La llave con la que el usuario compara a la lista de pacientes.
        otra_lista (list): La lista con las keys del diccionario, sin modificar.

    Returns:
        dict|bool: El empleado, modificado, si es que se editó alguno de sus datos, y un booleano, indicando si
        la función logró su cometido.
    """
    opciones = (f"{verde_2}\n- Apellido\n- Nombre\n- DNI\n- Grupo sanguíneo\n- Edad\n"
                f'- Altura\n- Peso{reset}')

    bandera = True
    while bandera:
        coincidencia = buscar_dato(lista, key, ingreso, 2)
        if coincidencia != None:
            system("cls")
            eleccion = get_string_excluyente(f"{opciones}\nIngrese el dato a modificar: ",
                                            1, 10, lista_keys, 3)
            if eleccion == None:
                bandera = False
                break
            
            eleccion = eleccion.capitalize()
            auxiliar = armar_auxiliar_diccionario(coincidencia, otra_lista)

            modificado = modificar_paciente_opciones_keys(eleccion, auxiliar, lista_keys)
            if modificado == False:
                bandera = False
                break

            comparar_pacientes(coincidencia, modificado)

            confirmacion = get_string_excluyente("¿Desea realizar esta modificacion (SI/NO)?: ",
                                                1, 2, ["si", "no"], 3).strip().upper()

            if confirmacion == "SI":
                indice = lista.index(coincidencia)
                lista[indice] = modificado
                print("Modificacion realizada.")

            else:
                print("Modificacion no realizada.")

            pregunta_modificacion = get_string_excluyente("¿Desea realizar otra "
                                                "modificacion (SI/NO)?: ",1, 2, ["SI", "NO"], 3)
            if pregunta_modificacion != "SI":
                bandera = False
        else:
            print("No se encontró el empleado.")
            bandera = False

    return bandera

def comparar_pacientes(paciente_viejo: dict, paciente_nuevo: dict):
    """_summary_
    Muestra dos diccionarios, para que el usuario vea los cambios.

    Args:
        paciente_viejo (dict): Diccionario sin modificar.
        paciente_nuevo (dict): Diccionario modificado.
    """
    print(f"Desea modificar el/los dato del siguiente paciente:")
    mostrar_paciente(paciente_viejo)
    print("Y cambiarlo por:")
    mostrar_paciente(paciente_nuevo)

def modificar_item(diccionario: dict, key: str, modificacion: any) -> bool|dict:
    """_summary_
    Edita uno de los valores de la llave del diccionario a modificar.

    Args:
        diccionario (dict): Diccionario donde se hace el cambio
        key (str): La key que se va a modificar
        modificacion (any): El dato con el que se va a reemplazar el valor de esa key.

    Returns:
        bool|dict: En caso de no recibir una modificaion ingresada correctamente, devuelve un None.
        Si no, devuelve el diccionario modificado.
    """
    if modificacion == None:
        diccionario = False
    else:
        diccionario[key] = modificacion

    return diccionario

def modificar_paciente_opciones_keys(eleccion: str, paciente_modificado: dict, keys: list):
    """_summary_
    Busca si la key seleccionada por el usuario, se encuentra en las de un diccionario

    Args:
        eleccion (str): La eleccion del usuario para modificar la key
        paciente_modificado (dict): El diccionario a modificar
        keys (list): Todas las keys que se pueden modificar

    Returns:
        dict: El diccionario modificado.
    """

    for key in keys:
        if key.upper() == eleccion.upper():
            dato = solicitar_dato(key)
            paciente_modificado = modificar_item(paciente_modificado, key, dato)
    
    return paciente_modificado

# endregion

# region Eliminar paciente

def eliminar_paciente(lista: list[dict], bajas: list[dict], key: str) -> bool:
    """_summary_
    Elimina a un paciente de la lista, segun la key con la que se desee buscarlo.

    Args:
        lista (list[dict]): Lista compuesta por diccionarios
        bajas (list[dict]): Lista donde depositar los diccionarios eliminados de la lista original
        key (str): Key para buscar al paciente

    Returns:
        bool: Dependiendo si se realizó la operacion (True) o no (False o None)
    """
    system("cls")
    ingreso_dni = solicitar_dato(key)
    if filtrar_dni(lista, ingreso_dni):
        bandera = None

        if ingreso_dni == None:
            enviar_mensaje_error(4)
        else:
            for paciente in lista:
                if paciente[key] == ingreso_dni:
                    mostrar_paciente(paciente)
                    confirmacion = get_string_excluyente("¿Desea eliminar este paciente? (SI/NO)?: ",
                                                1, 2, ["si", "no"], 3).strip().upper()
                    if confirmacion == "SI":
                        bajas.append(paciente)
                        lista.remove(paciente)
                        print("\nEl paciente fue eliminado exitosamente.\n")
                        bandera =  True
                    else:
                        print("\nEl paciente no fue eliminado.\n")
                        bandera =  False
    else:
        bandera = False
        
    return bandera

# endregion

# region Mostrar lista

def mostrar_lista(lista: list[dict]) -> str:
    """_summary_
    Muestra la lista con todos los pacientes encontrados en ella. En formato de tabla.

    Args:
        lista (list[dict]): Lista compuesta por diccionarios
    Returns:
    str: Una lista con todos los diccionarios que se encuentre cargados a una lista.
    """
    keys = conseguir_keys(lista)

    mostrar_cabecera_lista()
    for dato in lista:
        id = dato[keys[0]]
        nombre = dato[keys[1]]
        apellido = dato[keys[2]]
        dni = dato[keys[3]]
        grupo_sanguineo = dato[keys[4]]
        edad = dato[keys[5]]
        altura = dato[keys[6]]
        peso = dato[keys[7]]

        mostrar = ("|{:>4}|{:>20}|{:>20}| {:>8}|{:>15}|{:>6}|{:>5} cm|"
                    "{:>7} kg|".format(id, nombre, apellido, dni,
                                    grupo_sanguineo, edad, altura, peso))
        print(mostrar)
        print(f"+{"-"*4}+{"-"*20}+{"-"*20}+{"-"*9}+{"-"*15}+{"-"*6}+{"-"*8}+{"-"*10}+")

# endregion

# region Ordenar lista

def ordenar_lista(lista: list[dict]) -> list[dict]:
    """_summary_
    Ordena la lista segun el dato que quiera el usuario, y el orden de como desea ordenar esa lista
    (Menor a mayor, o Mayor a menor)

    Args:
        lista (list[dict]): Una lista compuesta por diccionarios.

    Returns:
        list[dict]: Una lista compuesta por diccionarios, ordenada según lo
        quiera el usuario
    """
    keys = conseguir_keys(lista)
    keys_permitidas = [keys[1], keys[2], keys[4], keys[6]]
    opciones = crear_submenus(keys_permitidas, verde_2)
    

    eleccion = get_string_excluyente(f"{opciones}\nIngrese el dato con el que desea"
                                    f" ordenar la lista: ",
                                    1, 15, keys_permitidas, 3)
    
    if eleccion == None:
        enviar_mensaje_error(9)
    else:
        for key in keys_permitidas:
            if eleccion == key:
                ordenar_con_criterio_key(key, lista)
                break

def ordenar_con_criterio_key(key: str, lista: list[dict]) -> list[dict]:
    """_summary_
    Solicita al usuario el orden deseado de la lista, y dependiendo su respuesta, 
    llama a otra funcion para realizarlo

    Args:
        key (str): La key con la que el usuario desea ordenar la lista:
        lista (list[dict]): La lista compuesta por diccionarios
    """
    orden_de_lista = get_int(f"¿Como desea ordenar la lista?\n{violeta}1. Menor a mayor\n"
                                    f"2. Mayor a menor{reset}\nElegir el número: ",
                                    "ERROR. Por favor, vuelva a elegir una opción",
                                    1, 2, "No se pudo realizar la operacion solicitada", 3)
    if orden_de_lista == 1:
        ordenar_lista_segun_orden(lista, key, orden_de_lista)
        mostrar_lista(lista)
    elif orden_de_lista == 2:
        ordenar_lista_segun_orden(lista, key, orden_de_lista)
        mostrar_lista(lista)
    else:
        enviar_mensaje_error(5)

# endregion

# region Buscar por DNI

def buscar_por_dato(lista: list[dict], key: str) -> dict:
    """_summary_
    Busca a un paciente según la key solicitada.

    Args:
        lista (list[dict]): Lista compuesta por diccionarios.
        key (str): Llave con la que se va a buscar al usuario.

    Returns:
        dict: El diccionario que se encontró, y que coincide con la busqueda.
    """
    ingreso = solicitar_dato(key)
    if ingreso == None:
        enviar_mensaje_error(4)
    
    else:
        paciente = buscar_dato(lista, key, ingreso, 2)

        if paciente == None:
            enviar_mensaje_error(11)
        else:
            mostrar_paciente(paciente)

# endregion

# region Calcular promedios

def calcular_promedio(lista: list[dict]) -> str:
    """_summary_
    Solicita al usuario la key que quiere usar para calcular el promedio.

    Args:
        lista (list[dict]): Lista compuesta de diccionarios.

    Returns:
        float: Devuelve el promedio de la key eligida
    """
    keys = conseguir_keys(lista)
    keys_permitidas = [keys[4], keys[5], keys[7]]
    opciones = crear_submenus(keys_permitidas, verde_2)

    system("cls")
    print(keys_permitidas)

    eleccion = get_string_excluyente(f"{opciones}\nIngrese el dato con el que desea"
                                    f" calcular el promedio: ",
                                    1, 16, keys_permitidas, 3)
    
    if eleccion == None:
        enviar_mensaje_error(8)
    if eleccion == "Grupo sanguineo":
        sangre = get_string_excluyente_2(f"Ingrese el dato con el que desea"
                                    f" buscar el tipo de sangre: ",
                                    2, 3, grupo_sanguineo, 3)
        promedio = calcular_promedio_key_2(lista, sangre)
        print(f"\nEl promedio de {eleccion}, fue de %{round(promedio, 2)}\n")
    else:
        for key in keys_permitidas:
            if eleccion == key:
                promedio = calcular_promedio_key(lista, eleccion)
                print(f"\nEl promedio de {eleccion}, fue de {round(promedio, 2)}\n")
                break

# endregion

# region Determinar compatibilidad.

def determinar_compatibilidad(lista: list[dict], reportes: int) -> int|bool:
    """_summary_
    Busca los tipos compatibles de sangre para el paciente buscado, y encuentra a las primeras 3
    coincidencias, creando un reporte con las mismas.

    Args:
        lista (list[dict]): Lista compuesta por diccionarios.
        reportes (int): Numero de reportes en "config"

    Returns:
        int|bool: Devuelve el contador de reportes + 1, o un booleano en caso de
        no poder concretarse
    """
    system("cls")
    documento = True
    dni = solicitar_dato("DNI")

    if dni != None:
        paciente = buscar_dato(lista, "DNI", dni, 2)
        lista_donantes = None

        match paciente["Grupo sanguineo"]:
            case "A+":
                print(f"El paciente de nombre {paciente["Nombre"]} puede donar a los grupos [A+, AB+]")
                lista_donantes = ["A+", "AB+"]
            case "A-":
                print(f"El paciente de nombre {paciente["Nombre"]} puede donar a [A+, A-, AB+, AB-]")
                lista_donantes = ["A+", "A-", "AB+", "AB-"]
            case "B+":
                print(f"El paciente de nombre {paciente["Nombre"]} puede donar a [B+, AB+]")
                lista_donantes = ["B+", "AB+"]
            case "B-":
                print(f"El paciente de nombre {paciente["Nombre"]} puede donar a [B+, B-, AB+, AB-]")
                lista_donantes = ["B+", "B-", "AB+", "AB-"]
            case "AB+":
                print(f"El paciente de nombre {paciente["Nombre"]} puede donar a [AB+]")
                lista_donantes = ["AB+"]
            case "AB-":
                print(f"El paciente de nombre {paciente["Nombre"]} puede donar a [AB+, AB-]")
                lista_donantes = ["AB+", "AB-"]
            case "O+":
                print(f"El paciente de nombre {paciente["Nombre"]} puede donar a [A+, B+, AB+, O+]")
                lista_donantes = ["A+", "B+", "AB+", "0+"]
            case "O-":
                print(f"El paciente de nombre {paciente["Nombre"]} puede donar a [A+, B+, AB+, O+, A-, B-, AB-, O-]")
                lista_donantes = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
            case _:
                print("Tipo de sangre no existente.")
        # blood_type = {  "A+": 
        #                 {
        #                 "receive": "A+, AB+",
        #                 "donate": ["A+", "AB+"]
        #                 },
        #                 "A-":
        #                 {
        #                 "receive": "A+, A-, AB+, AB-",
        #                 "donate": ["A+", "A-", "AB+", "AB-"]
        #                 },
        #             }

        coincidencias = buscar_lista_datos(lista, "Grupo sanguineo", lista_donantes)

        documento = generar_txt(paciente["ID"], coincidencias, reportes)

        mostrar_lista(coincidencias)

        print("Se ha creado un reporte con los datos de las coincidencias encontradas.")
    
    else:
        documento = False

    return documento

def generar_txt(identificacion: str|int, coincidencia: list, reportes: int) -> int:
    """_summary_

    Args:
        identificacion (str | int): El dato con el que se va a nombrar el reporte.
        coincidencia (list): Las coincidencias encontradas, y que se
        mostraran en el reporte.
        reportes (int): Contador de reportes a modificar

    Returns:
        int: Cantidad de reportes modificado (+1)
    """
    reporte = reportes + 1

    fecha = conseguir_fecha()
    coindencia = len(coincidencia)

    string = (f"Reporte N°:{reporte:04}\n"
                f"Fecha: {fecha}\n"
                f"Cantidad de coincidencias: {coindencia}\n"
                f"ID   Nombre{" "*15}Apellido{" "*13}"
                f"DNI{" "*10}Grupo sanguineo{" "*3}Edad{" "*5}Altura{" "*3}Peso       \n"
                f"{"-"*108}\n")
    
    with open(f"reporte_{reporte}_ID{identificacion}.txt", "w", encoding="utf-8") as archivo:
        archivo.write(string)
        for dato in coincidencia:
            archivo.write(f"{dato["ID"]:<4}|{dato["Nombre"]:<20}|{dato["Apellido"]:<21}|"
                        f"{dato["DNI"]:<11}|{dato["Grupo sanguineo"]:<17}|{dato["Edad"]:<8}|"
                        f"{dato["Altura"]:<6}cm|{dato["Peso"]:<9.2f}kg|\n")
    
    return reporte

def filtrar_dni(lista: list[dict], nuevo_dni: str) -> bool:
    """_summary_
    Crea 2 sets, uno con todos los DNIs de la lista de pacientes, y otro con el
    nuevo DNI que se va a ingresar. Si existe una intersección entre estos sets,
    no se permite usar ese DNI, caso contrario, lo habilita.

    Args:
        lista (list[dict]): Una lista que contiene diccionarios.
        nuevo_dni (str): Un dni de 8 caracteres numericos

    Returns:
        bool: Booleano que verifica si se cumplió la condición
    """
    verificacion = None
    lista_dnis = []

    for i in range(len(lista)):
        dni = lista[i]["DNI"]
        lista_dnis.append(dni)

    set_dni_lista = set(lista_dnis)
    set_dni_nuevo = {nuevo_dni}

    if len(set_dni_nuevo.intersection(set_dni_lista)) > 0:
        verificacion = True
    else:
        verificacion = False

    return verificacion