c = 0
def swap(a: int, b: int):
    return b, a

def particionar(array, low, high):
    pivote = array[high] #El pivote sera el ultimo elemento de la lista
    i = low - 1
        
    for j in range(low, high):
        
        if array[j] <= pivote:
            i += 1
            array[i], array[j] = swap(array[i], array[j])
    
    array[i + 1], array[high] = swap(array[i + 1], array[high] )
    
    return i + 1

def quick_sort(array):
    low = 0                 # El primer elemento de la lista
    high = len(array) - 1   # El último elemento de la lista
    pila = [0] * (len(array))     # Pila auxiliar
    tope = -1    #Inicializar el tope de pila
    #Se añade el primer y ultimo elemento de la lista:
    tope += 1
    pila[tope] = low    # Se establece el punto más bajo de la pila
    tope += 1
    pila[tope] = high   # Se establece el punto más alto de la pila

    while tope >= 0: #Se desapilan elementos de la pila mientras haya alguno.
        global c
        c+= 1
        #Se sacan los valores actuales de low y high (en cada iteracion) de la pila (se hace un pop)
        high = pila[tope]
        tope -= 1
        low = pila[tope]
        tope -= 1

        pi = particionar(array, low, high)  # Ordenamiento  / #pi = pivot
        #Apilar para la izquierda de la pila
        if pi - 1 > low:
            tope += 1
            pila[tope] = low
            tope += 1
            pila[tope] = pi - 1
        #Apilar para la derecha de la pila
        if pi + 1 < high:
            tope += 1
            pila[tope] = pi + 1
            tope += 1
            pila[tope] = high

import time

vector = [5,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,1,9,7,3,1,9,7,3,1,9,7,
          3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,
          1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,
          1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3]
start = time.time()
quick_sort(vector)
end = time.time()
print(end)
print(start)
print(f"Tiempo: {(end - start)*1000}")
print(f"iteraciones: {c}")
print(len(vector))
print(vector)