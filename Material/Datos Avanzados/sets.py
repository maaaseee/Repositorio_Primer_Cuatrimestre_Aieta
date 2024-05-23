# mi_set = {5,7,13,45,6,8,3,5,8,1,4,2,56,444}

# print(mi_set)

# for elemento in mi_set:
#     print(elemento)

# mi_set.add(112) # {1, 2, 3, 4, 5, 6, 7, 8, 13, 45, 112, 56, 444}
# print(mi_set)

# mi_set.remove(112) # CUIDADO, MEJOR USAR .DISCARD
# print(mi_set)

# mi_set.discard(56)
# print(mi_set)

# elemento = mi_set.pop()
# print(elemento)
# print(mi_set)

# mi_set.clear()
# print(mi_set)

################################################################################################

set_a = {3, 4, 5}
set_b = {6, 2, 3}

union = set_a.union(set_b)         # A U B
print(union)

interseccion = set_a.intersection(set_b)  # A n B
print(interseccion)

diferencia = set_a.difference(set_b)  # A - B
print(diferencia)