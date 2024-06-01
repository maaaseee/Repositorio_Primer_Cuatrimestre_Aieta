def calcular_promedio(lista: list) -> int|float|bool:
    retorno = True
    if type(lista) == list:
        retorno = False
        if len(lista) > 0:
            retorno = 0
            contador = 0
            for i in range(len(lista)):
                retorno += lista[i]
                contador += 1

    promedio = retorno / contador

    return promedio

def calcular_promedio_positivos(lista: list) -> int|float|bool:
    retorno = True
    if type(lista) == list:
        retorno = False
        if len(lista) > 0:
            retorno = 0
            contador = 0
            for i in range(len(lista)):
                if lista[i] > 0:
                    retorno += lista[i]
                    contador += 1

    promedio_positivos = retorno / contador

    return promedio_positivos

def calcular_producto(lista: list) -> int|float|bool:
    retorno = True
    if type(lista) == list:
        retorno = False
        if len(lista) > 0:
            retorno = 1
            for i in range(len(lista)):
                retorno *= lista[i]

    return retorno

def encontrar_maximo(lista: list) -> int|float|bool:
    retorno = True
    numero_maximo = 0
    if type(lista) == list:
        retorno = False

        if len(lista) > 0:
            retorno = 0
            posicion = 0
            bandera_maximo = True

            for i in range(len(lista)):
                retorno = lista[i]
                posicion += 1
                if bandera_maximo == True or retorno > numero_maximo:
                    numero_maximo = retorno
                    posicion_maximo = posicion
                    bandera_maximo = False

    return posicion_maximo

def mostrar_posicion(lista: list) -> int|float|bool:
    retorno = True
    numero_maximo = 0
    if type(lista) == list:
        retorno = False

        if len(lista) > 0:
            retorno = 0
            contador = 0
            bandera_maximo = True

            for i in range(len(lista)):
                retorno = lista[i]
                contador += 1

                if bandera_maximo == True or retorno > numero_maximo:
                    numero_maximo = retorno
                    contador_maximo = contador
                    bandera_maximo = False
            
            retorno = print(f"La posición es: {contador_maximo} y el número es {numero_maximo}")

    return retorno

lista = [4, 7, 3]

promedio_final = calcular_promedio(lista)

if promedio_final == True:
    print("El valor ingresado no es una lista")
elif promedio_final == False:
    print("La lista está vacía")
else:
    print(f"El promedio de la lista es igual a: {promedio_final}")

print("")

promedio_postivos = calcular_promedio_positivos(lista)

if promedio_postivos == True:
    print("El valor ingresado no es una lista")
elif promedio_postivos == False:
    print("La lista está vacía")
else:
    print(f"El promedio de la lista es igual a: {promedio_postivos}")

print("")

producto_final = calcular_producto(lista)

if producto_final == True:
    print("El valor ingresado no es una lista")
elif producto_final == False:
    print("La lista está vacía")
else:
    print(f"El producto de cada uno de los números de la lista es: {producto_final}")

print("")

posicion = encontrar_maximo(lista)

if posicion == True:
    print("El valor ingresado no es una lista")
elif posicion == False:
    print("La lista está vacía")
else:
    print(f"La posicion del número más alto es: {posicion}")

print("")

posicion_final = mostrar_posicion(lista)

if posicion_final == True:
    print("El valor ingresado no es una lista")
elif posicion_final == False:
    print("La lista está vacía")
else:
    pass
