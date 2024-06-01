def crear_alumno(dni: int, nombre: str, apellido: str, nota: int) -> dict:
    diccionario_alumno = {
        "dni" : dni,
        "nombre" : nombre,
        "apellido" : apellido,
        "nota" : nota
    }

    return diccionario_alumno

def ingresar_alumno_lista(lista_alumnos: list[dict]):     # USAR LAS FUNCIONES GET_STRING
    dni = input("Ingresar: ")
    nombre = input("Ingresar: ")
    apellido = input("Ingresar: ")
    nota = input("Ingresar: ")

    diccionario_alumno = crear_alumno(dni, nombre, apellido, nota)

    lista_alumnos.append(diccionario_alumno)

def mostrar_lista_alumnos(lista_alumnos: list[dict]):
    for alumno in lista_alumnos:
        mostrar_alumno(alumno)

def mostrar_alumno(un_alumno: dict):
    print(f"{un_alumno["dni"]} - {un_alumno["apellido"]} - {un_alumno["nombre"]} - {un_alumno["nota"]}")

def modificar_alumnos(lista_alumnos: list[dict], dni: int):
    for i in range(len(lista_alumnos)):
        if lista_alumnos[i]["dni"] == dni:
            mostrar_alumno(lista_alumnos[i])
            auxiliar = lista_alumnos[i]
            ingresar_nota = int(input("Ingrese la nueva nota: "))
            lista_alumnos[i]["nota"] = ingresar_nota
            break

def eliminar_alumno(lista_alumnos: list[dict], dni: int):
    for alumno in lista_alumnos:
        if alumno["dni"] == dni:
            mostrar_alumno(alumno) # HACE UNA VALIDACION, VAGO
            eliminado = alumno
            break

    if eliminado != None:
        lista_alumnos.remove(eliminado)

    return eliminado