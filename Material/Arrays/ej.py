def sumar_posistivos(lista: list) -> int:
    retorno = -2
    if type(lista) == list: 
        retorno = -1
        if len(lista) > 0:
            retorno = 0
            for i in range(len(lista)):
                if lista[i] > 0:
                    retorno += lista[i]

    return retorno

def buscar_maximo(lista: list) -> int:
    bandera_maximo = True
    for i in range(len(lista)):
        if bandera_maximo == True or numero_maximo < lista[i]:
            numero_maximo = lista[i]
            bandera_maximo = False

    return numero_maximo

def buscar_negativo(lista: list) -> bool:
    bandera_negativo = False
    for i in range(len(lista)):
        if lista[i] < 0:
            bandera_negativo = True
            break

    return bandera_negativo

def buscar_reemplazar(lista: list, busqueda: int, reemplazo: int, reemplazo_todo: bool):
    retorno = False
    if type(lista) == list and type(busqueda) == int and type(reemplazo) == int:
        retorno = True
        for i in range(len(lista)):
            if lista[i] == busqueda:
                lista[i] = reemplazo
                if not reemplazo_todo:
                    break

    return retorno


lista = [15, 9, 1, 44]

# suma = sumar_posistivos(lista)
# if suma == -2:
#     print("El valor ingresado no es una lista")
# elif suma == -1:
#     print("La lista está vacía")
# else:
#     print(f"La suma de todos los valores de la lista es: {suma}")

# maximo = buscar_maximo(lista)
# print(f"El número más grande de la lista es: {maximo}")

# if buscar_negativo(lista):
#     print("Por lo menos se ha ingresado un negativo")
# else:
#     print("No se ingresó un negativo")

if buscar_reemplazar(lista, 44, 1000, False):
    for i in range(len(lista)):
        print(lista[i])
else:
    print("Hubo un error, no se pudo reemplazar")
