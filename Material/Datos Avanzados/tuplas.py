# tupla = tuple(5,6,[5,6,4])
tupla = (5,6,[5,1,9])

tupla[2][0] = 250   # [2] Index tupla | [0] Index lista

# tupla = (5, 6 ,4)
print(tupla)
# print(type(tupla))

# for elemento in tupla:
#     print(elemento)

# tupla = () # NO SE PUEDE MODIFICAR
# tupla = (5) # ES UN VALOR ENTERO, NO ES TUPLA

tupla = (4, 9, 6)
a = tupla[0]
b = tupla[1]
c = tupla[2]

a,b,c = tupla

print(a)
print(b)
print(c)

print("#"*60)

from input_paquete.input_func import *

colores = {"Blanco" : (255,255,255),
           "Negro" : (0,0,0),
           "Rojo" : (255,0,0),
           "Azul" : (0,0,255),
           "Verde" : (0,255,0),
           "Azul Claro" : (0,150,255)}
#endregion

#region Funciones para completar

def seleccionar_color(mensaje: str, diccionario: dict):
    #Desplegar en pantalla todos los colores. El usuario deberá seleccionar uno.
    color_retorno = None
    colores_lista = diccionario.keys()
    for clave in colores_lista:
        print(f"» {clave}")
    color = get_string_excluyente(mensaje, 4, 10, diccionario.keys(), "El color no pudo ser ingresado.", 3)
    for clave in colores_lista:
        if color == clave:
            color_retorno = diccionario[clave]
            break
    
        
    return color_retorno

print(seleccionar_color("Color: ", colores))

string = "Azul Claro"

segunda_string = string.strip(" ")

print(segunda_string.capitalize())
