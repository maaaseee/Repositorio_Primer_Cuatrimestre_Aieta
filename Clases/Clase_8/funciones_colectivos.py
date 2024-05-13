def ingreso_legajo() -> int:
    # Ingreso de dato (el legajo) para verificar en la función "cargar_planillas"
    # Devuelve un número entero
    legajo = int(input("Ingrese legajo: "))
    return legajo

def validar_legajo(ingreso_legajo: int, matriz: list) -> bool:
    # Se valida el legajo, buscando el mismo valor dentro de la matriz
    # Si el elemento de la matriz es válido devuelve True, de lo contrario, devuelve False
    # En caso de ya haber encontrado el legajo, rompe la iteracion de filas y columnas
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != ingreso_legajo:
                valor = False
            else:
                valor = True
                break
        if valor:
            break

    return valor

def ingresa_coche() -> int:
    # Ingreso de dato (la columna) para verificar en la función "cargar_planillas"
    # Devuelve un número entero
    coche = int(input("Ingrese coche: "))
    return coche

def validar_coche(coche: int, matriz: list) -> bool:    # COLUMNAS
    # Se validan los coches, buscando el mismo valor dentro de la matriz
    # Si la posicion de esa matriz es válida devuelve True, de lo contrario, devuelve False
    # En caso de ya haber encontrado el coche, rompe la iteracion de filas y columnas
    for i in range(1, len(matriz) + 1):
        for j in range(1, len(matriz[i - 1]) + 1):
            if j != coche:
                valor = False
            else:
                valor = True
                break
        if valor:
            break

    return valor

def ingresar_linea() -> int:
    # Ingreso de dato (la fila) para verificar en la función "cargar_planillas"
    # Devuelve un número entero
    return int(input("Ingrese la línea del colectivo: "))

def validar_linea(linea: int, matriz: list) -> bool:   # FILAS
    # Se validan las líneas, buscando el mismo valor dentro de la matriz
    # Si la posicion de esa matriz es válida devuelve True, de lo contrario, devuelve False
    # En caso de ya haber encontrado la línea, rompe la iteracion de filas y columnas
    for i in range(1, len(matriz) + 1):
        for j in range(1, len(matriz[i - 1]) + 1):
            if i != linea:
                valor = False
            else:
                valor = True
                break
        if valor:
            break

    return valor

def ingresar_recaudacion() -> float|int:
    # Se ingresa la cantidad de dinero recaudada en ese viaje
    # Si el número es menor que 0, o mayor a 100.000.000 se vuelve a pedir el ingreso de datos
    # Devuelve el valor de la recaudacion
    recaudacion = float(input("Ingrese la recaudación del viaje: "))
    while recaudacion < 0 and recaudacion > 100000000:
        recaudacion = float(input("Ingrese la recaudación del viaje: "))

    return recaudacion

def mostrar_menu() -> int:
    # Muestra el menú de opciones
    # Devuelve el valor de la opción seleccionada
    print("\nMenú:")
    print("1. Cargar planillas")
    print("2. Mostrar recaudación de todos los coches y líneas")
    print("3. Calcular y mostrar recaudación por línea")
    print("4. Calcular y mostrar recaudación por coche")
    print("5. Calcular y mostrar recaudación total")
    print("6. Salir\n")
    opcion = int(input("Seleccione una opción: "))
    return opcion

def cargar_planillas(matriz_legajos: list, matriz_recaudacion: list):
    # Se cargan las planillas de los choferes
    # Se pide el ingreso del legajo, y luego se verifica si está en la matriz
    # Luego, se pide el ingreso de la línea de colectivo a cargar
    # Despues, el ingreso del coche de esa misma línea
    # Por ultimo, se le pide ingresar la recaudacion de ese colectivo
    # Se coloca la recaudacion en la posicion de la matriz seleccionada
    # Si en alguno de estos casos, no se ingresa un número válido, se rompe la función
    bandera = True
    legajo = ingreso_legajo()
    verificar_legajo = validar_legajo(legajo, matriz_legajos)
    if verificar_legajo:
        print("Legajo valido\n")
        while bandera:
            linea = ingresar_linea()
            verificar_linea = validar_linea(linea, matriz_recaudacion)          # FILAS

            if verificar_linea == False:
                print("Linea invalida\n")
            else:
                coche = ingresa_coche()
                verificar_coche = validar_coche(coche, matriz_recaudacion)      # COLUMNAS

                if verificar_coche == False:
                    print("Coche invalido\n")
                else:
                    recaudacion_chofer = ingresar_recaudacion()
                    matriz_recaudacion[linea - 1][coche - 1] += recaudacion_chofer

            pregunta = input("DESEA CONTINUAR? SI/NO: ")
            if pregunta == "NO":
                bandera = False
    else:
        print("\nLegajo invalido\n")

def mostrar_planillas(matriz_recaudacion: list):
    # Muestra la planilla de recaudacion, segun las líneas y las columnas de la misma
    print("La recaudación de la empresa por cada línea y colectivo es... \n")

    for i in range(len(matriz_recaudacion)):
        for j in range(len(matriz_recaudacion[i])):
            print(f"{matriz_recaudacion[i][j]:25}", end = "")
        print("")

def calcular_recaudacion_total(matriz_recaudacion: list) -> str:
    # Se suma todos los elemtnos de la planilla de recaudacion
    acumulador = 0
    for i in range(len(matriz_recaudacion)):
        for j in range(len(matriz_recaudacion[i])):
            acumulador += matriz_recaudacion[i][j]

    mensaje = f"\nLa recaudación total de la empresa fue de {acumulador}"
    
    return mensaje

def calcular_recaudacion_por_linea(matriz_recaudacion: list):
    # Se suman los elementos dentro de cada fila, y se los separa en un vector
    # Cada elemento del vector representa una línea (fila) de recaudacion
    # Muestra el vector de filas
    vector_lineas = [[0] * 1 for _ in range(len(matriz_recaudacion))]

    for i in range(len(matriz_recaudacion)):
        acumulador_linea = 0
        for j in range(len(matriz_recaudacion[i])):
            acumulador_linea += matriz_recaudacion[i][j]
        vector_lineas[i][0] = acumulador_linea
    
    for i in range(len(vector_lineas)):
        for j in range(len(vector_lineas[i])):
            print(f"Recaudación linea {i+1}: ${vector_lineas[i][j]:8}", end = "")
        print("")

def calcular_recaudacion_por_coche(matriz_recaudacion: list):
    # Se suman los elementos dentro de cada columna, y se los separa en un vector
    # Cada elemento del vector representa una línea (columna) de recaudacion
    # Muestra el vector de columnas
    vector_columnas = [0] * len(matriz_recaudacion[0])

    for i in range(len(matriz_recaudacion[0])):
        acumulador_columna = 0
        for j in range(len(matriz_recaudacion)):
            acumulador_columna += matriz_recaudacion[j][i]
        vector_columnas[i] = acumulador_columna


    for i in range(len(matriz_recaudacion[0])):
        print(f"Recaudación coche {i+1}: ${vector_columnas[i]:8}\n", end = "")
    print("")