import random

def sumar_1():
    un_numero = input("Ingrese su numero: ")
    un_numero = int(un_numero)
    otro_numero = input("Ingrese su numero: ")
    otro_numero = int(otro_numero)

    suma = un_numero + otro_numero

    print(f"La suma es: {suma}")

def sumar_2(un_numero, otro_numero):
    suma = un_numero + otro_numero

    print(f"La suma es: {suma}")

def sumar_3():
    un_numero = input("Ingrese su numero: ")
    un_numero = int(un_numero)
    otro_numero = input("Ingrese su numero: ")
    otro_numero = int(otro_numero)

    suma = un_numero + otro_numero

    return suma

def sumar_4(un_numero, otro_numero):
    suma = un_numero + otro_numero

    return suma

def sumar_5(primer_numero, segundo_numero, tercer_numero = 0):
    suma = primer_numero + segundo_numero + tercer_numero

    return suma

def resta(primer_numero:int, segundo_numero:int = 5):
    return primer_numero - segundo_numero

print(resta(primer_numero = int(input("Ingrese el número: "))))


# print("Bienvenidos al programa.")
# sumar_1()       #NO recibe parametros, y NO devuelve nada.
# print("Fin del programa.")

# sumar_2(2, 4)

# un_numero = input("Ingrese su numero: ")
# un_numero = int(un_numero)
# otro_numero = input("Ingrese su numero: ")
# otro_numero = int(otro_numero)

# sumar_2(un_numero, otro_numero) #NO recibe nada y RETORNA el resultado

# un_numero = random.randint(1, 100)
# otro_numero = random.randint(500, 700)
# sumar_2(un_numero, otro_numero)

# resultado = sumar_3()
# print(f"La suma es: {resultado}.") 

# resultado = sumar_4(8, 99)
# print(f"El resultado es: {resultado}.") #RECIBE parametros y RETORNA el resultado

# resultado = sumar_5(4, 3)

# print(resultado)

# segundo_resultado = sumar_5(4, 3, 9)

# print(segundo_resultado)