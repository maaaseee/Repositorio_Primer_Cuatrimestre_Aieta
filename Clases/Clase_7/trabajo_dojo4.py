"""
Miembros: Jerónimo Córdoba - Federico Aieta - Nadine Banegas - Rodrigo Yerahian
---
Clase 7: Desafio
---
Enunciado: 

Un programa que sea capaz de multiplicar dos matrices ingresadas por el usuario. 
Y validar las dimensiones de cada una para que sea consistente con el procedimiento 
"""

filas_A = int(input("Filas de la matriz A (Ingrese un número): "))  #1 INGRESO DE DATOS 
columnas_A = int(input("Columnas de la matriz A (Ingrese un número): ")) #1 PARCEO DE DATOS

filas_B = int(input("Filas de la matriz B (Ingrese un número): ")) #1 
columnas_B = int(input("Columnas de la matriz B (Ingrese un número): ")) #1 

if columnas_A == filas_B:
    matriz_a = [[0] * columnas_A for _ in range(filas_A)] #2 CREACION DE LA MATRIZ INICIALIZADA EN 0
    matriz_b = [[0] * columnas_B for _ in range(filas_B)] #2

    for i in range(len(matriz_a)): #1 PIDO VALORES DE LA MATRIZ A
        for j in range(len(matriz_a[i])):
            matriz_a[i][j] = int(input("Ingrese un número: "))
    print("Matriz A")

    for i in range(len(matriz_a)): #3 PRINTEO MATRIZ A
        for j in range(len(matriz_a[i])):
            print(f"{matriz_a[i][j]:5}", end = "")
        print("")

    for i in range(len(matriz_b)): #1 PIDO LOS VALORES DE LA MATRIZ B
        for j in range(len(matriz_b[i])):
            matriz_b[i][j] = int(input("Ingrese un número: "))
    print("Matriz B")

    for i in range(len(matriz_b)): #3 PRINTEO MATRIZ B
        for j in range(len(matriz_b[i])):
            print(f"{matriz_b[i][j]:5}", end = "")
        print("")

    #4 ASIGNACION DE VARIABLES
    print("Matriz C")

    M = len(matriz_a)    # FILAS 
    N = len(matriz_b[0]) # COLUMNAS

    #2 CREACION DE LA MATRIZ C INICIALIZADA EN 0
    matriz_c = [[0] * N for _ in range(M)]       # 0 se multipl. N veces para crear una fila, Esa fila se va a repetir M veces
                                    
    #4 CREO MATRIZ C
    for i in range(len(matriz_c)):                           
        for j in range(len(matriz_c[0])):                       
            for k in range(len(matriz_b)):       
                matriz_c[i][j] += matriz_a[i][k] * matriz_b[k][j]

    #3 PRINTEO MATRIZ C
    for i in range(len(matriz_c)):
        for j in range(len(matriz_c[0])):
            print(f"{matriz_c[i][j]:5}", end = "")
        print("")
else:
    print("No se pueden multiplicar estas matrices. El número de columnas de A debe ser igual al número de filas de B.")
