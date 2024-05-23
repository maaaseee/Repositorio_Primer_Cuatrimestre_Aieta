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