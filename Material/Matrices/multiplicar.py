matriz = [[0, 1, 4],
        [7, 11, 13],
        [21, 32, 44]]

escalar = 5

M = len(matriz)
N = len(matriz[0])

matriz_resultado = [[0] * N for _ in range(M)]

for i in range(M):
    for j in range(N):
        matriz_resultado[i][j] = matriz[i][j] * escalar

for i in range(M):
    for j in range(N):
        print(f"{matriz_resultado[i][j]:5}", end = "")
    print("")
