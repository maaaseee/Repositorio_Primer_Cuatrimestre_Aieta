import prueba_func

prueba_func.sumar_2(5, 9)
resultado = prueba_func.sumar_3()
print(resultado)

from prueba_func import *

resultado = sumar_2(9, 9)
print(resultado) 

from Prueba_funciones.prueba_func import *

sumar_2(2, 5)

import Prueba_funciones.prueba_func as SUMAR

SUMAR.sumar_2(2, 6)
