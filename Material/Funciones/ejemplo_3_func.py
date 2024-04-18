def presentar_alumno(nombre: str, edad: int, altura: float) -> int:
    #   Muestra los datos del alumno
    #   Recibe el nombre, la edad, y la altura
    #   Devuelve un número
    print(f"{nombre}, {edad}, {altura}.")
    return 1
    
retorno = presentar_alumno("Marcela", 55, 1.60)

def modificar_valor(el_numero: int) -> int:
    el_numero = 25
    return el_numero

numero = 5
numero = modificar_valor(numero)
print(numero)

def modificar_lista(una_lista: list) -> None:
    una_lista[3] = ":v"

lista = [5, 6, 8, 9, 12]
print(lista)

modificar_lista(lista)
print(lista)


def get_int(mensaje, minimo, maximo) -> int:
    numero = input(mensaje)
    numero = int(numero)
    while numero < minimo or numero > maximo:
        numero = input(f"Error. {mensaje}")
        numero = int(numero)

    return numero

edad = get_int("Ingrese su edad: ", 18, 30)
legajo = get_int("Ingrese su legajo: ", 1000, 9999)
nota = get_int("Ingrese su nota: ", 1, 10)

