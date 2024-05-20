from class_pj import *


personaje_1 = Personaje("Iron Man", True, True, "Tener plata", 500)
personaje_2 = Personaje("Thor", False, True, "Trueno", 700)
personaje_3 = Personaje("Spider Man", True, False, "Muerte instantánea", 300)
personaje_4 = Personaje("Groot", False, False, "Ser un arbol", 900)

# # print(type(personaje_1))
# # DESCRIBIR PERSONAJE
# print(personaje_1.describirse())
# print(personaje_2.describirse())

# # APTITUDES

# personaje_1.volar(1000, 200)
# personaje_3.volar(100, 50)
# # ACCIONES

# personaje_1.atacar(personaje_2)
# print(personaje_1.describirse())
# print(personaje_2.describirse())

# DESPUES DE APRENDER LISTAS AVANZADAS #

lista_heroes: list[Personaje] = []
lista_heroes.append(personaje_1)
lista_heroes.append(personaje_2)
lista_heroes.append(personaje_3)
lista_heroes.append(personaje_4)

for heroe in lista_heroes:
    print(heroe.describirse())