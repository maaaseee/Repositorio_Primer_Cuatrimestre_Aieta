"""
nombre: Federico
apellido: Aieta
Dojo 4
---
Clase 8: Tarea
---
Enunciado: 

Una empresa de colectivos tiene 3 líneas de coches cada una. En total tiene 15 choferes
(cada uno con un legajo distinto generado aleatoriamente)
Nos piden desarrollar un software que presente el siguiente menú de usuario:

Menú:
1. Cargar planillas. El chofer se debe identificar (el legajo debe existir dentro de una matriz de legajos).
Si el chofer existe cargará la recaudación del viaje indicando línea y coche 
(no necesariamente un chofer está asignado a una única línea y coche), estos datos deben estar validos.
Un chofer puede cargar más de una recaudación por día (para distintas líneas y distintos coches). 
Cada coche de cada línea puede tener varias recaudaciones diarias.
2. Mostrar la recaudación de todos los coches y líneas.
3. Calcular y mostrar recaudación por línea.
4. Calcular y mostrar recaudación por coche.
5. Calcular y mostrar recaudación por total.
6. Salir

"Todo el desarrollo tiene que estar modularizado: Ingreso de datos; Validaciones de líneas y coches;"
Generación y verificación de exitencia de legajo, cálculos, etc.

"""

import random
from funciones_colectivos import *

legajos = [[0] * 5 for _ in range(3)]

for i in range(len(legajos)):
    for j in range(len(legajos[i])):
        legajos[i][j] = random.randint(1, 20)

for i in range(len(legajos)):
    for j in range(len(legajos[i])):
        print(f"{legajos[i][j]:5}", end = "")
    print("")

bandera_seguir = True

recaudacion = [[0] * 5 for _ in range(3)]

while bandera_seguir:
    menu = mostrar_menu()

    match menu:
        case 1:
            primer_menu = cargar_planillas(legajos, recaudacion)
        case 2:
            segundo_menu = mostrar_planillas(recaudacion)
        case 3:
            tercer_menu = calcular_recaudacion_por_linea(recaudacion)
        case 4:
            cuarto_menu = calcular_recaudacion_por_coche(recaudacion)
        case 5:
            quinto_menu = calcular_recaudacion_total(recaudacion)
            print(quinto_menu)
        case 6:
            seguir = input("¿Está seguro que desea salir? Si/No \n")
            if seguir == "Si":
                bandera_seguir = False