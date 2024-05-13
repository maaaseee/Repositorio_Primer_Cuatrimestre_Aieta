M = 3
N = 2


matriz = [[0] * N for _ in range(M)]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = int(input("Ingrese un número: "))

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"{matriz[i][j]:5}", end = "")
    print("")

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = int(input("Ingrese un número: "))
        matriz[i][j] = matriz[i][j] * 2