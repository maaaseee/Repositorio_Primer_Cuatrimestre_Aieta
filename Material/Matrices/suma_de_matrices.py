matriz_a = [[3, 1, 2],
            [4, 6, 8],
            [7, 9, 5]]

matriz_b = [[3, 1, 2],
            [4, 6, 8],
            [7, 9, 5]]

M = len(matriz_a)    # FILAS
N = len(matriz_a[0]) # COLUMNAS

matriz_resultado = [[0] * N for _ in range(M)]

for i in range(M):
    for j in range(N):
        matriz_resultado[i][j] = matriz_a[i][j] * matriz_b[i][j]

for i in range(M):
    for j in range(N):
        print(f"{matriz_resultado[i][j]:5}", end = "")
    print("")
