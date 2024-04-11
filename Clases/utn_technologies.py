'''
UTN Technologies, una reconocida software factory se encuentra en la búsqueda de ideas para su próximo desarrollo en Python, que
promete revolucionar el mercado.

Las posibles aplicaciones son las siguientes:
Inteligencia artificial (IA),
Realidad virtual/aumentada (RV/RA),
Internet de las cosas (IOT)

Para ello, la empresa realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas.

A) Los datos a ingresar por cada empleado encuestado son:
nombre del empleado
edad (no menor a 18)
género (Masculino - Femenino - Otro)
tecnologia (IA, RV/RA, IOT)  

B) Cargar por terminal 10 encuestas.

C) Determinar:
Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive.
Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40.
Nombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese género.
'''

contador_empleados_m_iot_ia = 0

contador_not_ia = 0
contador_ia = 0

bandera = False
edad_maxima_m = 0

for encuesta in range(10):
    nombre = input("Su nombre es: ")

    edad = input("Su edad es de: ")
    edad = int(edad)
    while edad < 18:
        edad = input("Ingrese nuevamente su edad (Mayor a 18 años): ")
        edad = int(edad)

    genero = input("Su género es: ")
    while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
        genero = input("Ingrese nuevamente su género (Masculino, Femenino, u Otro): ")

    tecnologia = input("La tecnología que eligió fue: ")
    while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
        tecnologia = input("Ingrese nuevamente la tecnología que fue elegida: ")

    match genero:
        case "Masculino":
            if (edad > 25 and edad < 50) and (tecnologia == "IOT" or tecnologia == "IA"):
                contador_empleados_m_iot_ia += 1
            if bandera == False or edad_maxima_m < edad:
                edad_maxima_m = edad
                nombre_maximo_m = nombre
                tecnologia_maximo_m = tecnologia
                bandera = True

    match tecnologia:
        case "IOT" | "RV/RA":
            if genero == "Femenino":
                contador_ia += 1
            elif edad >= 33 and edad <= 40:
                contador_ia += 1
            else:
                contador_not_ia += 1
        case "IA":
            contador_ia += 1

total_contadores = contador_ia + contador_not_ia

porcentaje_not_ia = round((contador_not_ia * 100) / total_contadores, 2)

print(f"La cantidad de empleados que votaron por IA o IOT, y que se encuentran "
    f"entre los 25 y 50 años, es de: {contador_empleados_m_iot_ia}.")

print(f"El porcentaje de personas que no votaron por IA, o que pertenecen al "
    f"género Femenino, o se encuentran entre los 33 y 40 años, es del {porcentaje_not_ia}%.")

print(f"El nombre de la persona del género masculino y con mayor edad es: {nombre_maximo_m}.")
print(f"Y la tecnología que votó fue: {tecnologia_maximo_m}.")