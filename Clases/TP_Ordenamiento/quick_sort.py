c = 0
def swap(a: int, b: int):
    return b,a

def particionar(array, low, high):
    pivote = array[high] #El pivote sera el ultimo elemento de la lista
    i = low - 1
        
    for j in range(low, high):
        
        if array[j] <= pivote:
            i += 1
            array[i], array[j] = swap(array[i], array[j])
    
    array[i + 1], array[high] = swap(array[i + 1], array[high] )
    
    return i + 1
    
def quick_sort(array, low, high):
    global c
    c += 1
    if low < high:
        pi = particionar(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)
        

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
quick_sort(vector, 0 , len(vector) - 1)
end = time.time()
print(end)
print(start)
print(f"Tiempo: {(end - start)*1000}")
print(f"iteraciones: {c}")
print(len(vector))
print(vector)
