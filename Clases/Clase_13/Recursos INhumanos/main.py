from empleados import *
from os import system

# lista_empleados_rrhh = [
# {"id":1,"nombre":"Cynthea","apellido":"Zarfai","dni":8510287,"puesto":"VP Marketing","salario":1480693.9},
# {"id":2,"nombre":"Gisela","apellido":"Felstead","dni":5637974,"puesto":"Business Systems Development Analyst","salario":1495869.57},
# {"id":3,"nombre":"Sophey","apellido":"Bernollet","dni":7435874,"puesto":"Senior Sales Associate","salario":1449795.04},
# {"id":4,"nombre":"Pieter","apellido":"Cominello","dni":5725298,"puesto":"Operator","salario":398865.62},
# {"id":5,"nombre":"Colleen","apellido":"Awmack","dni":8463930,"puesto":"Registered Nurse","salario":355302.98},
# {"id":6,"nombre":"Ravi","apellido":"Eller","dni":9588904,"puesto":"Account Coordinator","salario":421655.32},
# {"id":7,"nombre":"Kerk","apellido":"Renon","dni":7589187,"puesto":"Nuclear Power Engineer","salario":274067.25},
# {"id":8,"nombre":"Zach","apellido":"Theseira","dni":6210134,"puesto":"Safety Technician IV","salario":848155.45},
# {"id":9,"nombre":"Perren","apellido":"Bollen","dni":6987462,"puesto":"Chief Design Engineer","salario":1008071.31},
# {"id":10,"nombre":"Pollyanna","apellido":"Thebeaud","dni":6773503,"puesto":"Geological Engineer","salario":975500.41},
# {"id":11,"nombre":"Roderic","apellido":"Merington","dni":6126389,"puesto":"Executive Secretary","salario":915265.29},
# {"id":12,"nombre":"Delinda","apellido":"Gerb","dni":6434457,"puesto":"Geological Engineer","salario":916305.17},
# {"id":13,"nombre":"Jocelin","apellido":"Hannan","dni":6099296,"puesto":"Account Executive","salario":1023710.91},
# {"id":14,"nombre":"Dori","apellido":"Toth","dni":8008983,"puesto":"Media Manager III","salario":874456.77},
# {"id":15,"nombre":"Hastings","apellido":"Mace","dni":7270435,"puesto":"Civil Engineer","salario":706397.11},
# {"id":16,"nombre":"Martha","apellido":"Larive","dni":6029079,"puesto":"Sales Representative","salario":1070157.98},
# {"id":17,"nombre":"Beckie","apellido":"Klimt","dni":8474227,"puesto":"Payment Adjustment Coordinator","salario":817468.77},
# {"id":18,"nombre":"Lurline","apellido":"Adelberg","dni":6033389,"puesto":"Database Administrator III","salario":1360247.16},
# {"id":19,"nombre":"Robena","apellido":"Ullrich","dni":6905629,"puesto":"Geologist II","salario":1314243.84},
# {"id":20,"nombre":"Xylina","apellido":"Avrahamov","dni":6164631,"puesto":"Assistant Professor","salario":434321.31}
# ]

lista_empleados_rrhh = [
{'ID': 1, 'Nombre':'Juan', 'Apellido': 'Perez', 'DNI': 12345678, 'Puesto': 'Ingeniero', 'Salario': 50000.0},
{'ID': 2, 'Nombre':'Maria', 'Apellido': 'Gomez', 'DNI': 87654321, 'Puesto': 'Analista', 'Salario': 45000.0},
{'ID': 3, 'Nombre':'Carlos', 'Apellido': 'Sanchez', 'DNI': 23456789, 'Puesto': 'Gerente', 'Salario': 70000.0},
{'ID': 4, 'Nombre':'Ana', 'Apellido': 'Lopez', 'DNI': 98765432, 'Puesto': 'Desarrollador', 'Salario': 55000.0},
{'ID': 19, 'Nombre':'Luis', 'Apellido': 'Martinez', 'DNI': 34567890, 'Puesto': 'Diseñador', 'Salario': 40000.0}
]

lista_despedidos_rrhh = [
{"id": 17, "Nombre": "Robena", "Apellido": "Ullrich", "DNI": 6905629, "Puesto": "Geologist II", "Salario": 1314243.84},
{"id": 18, "Nombre": "Xylina", "Apellido": "Avrahamov", "DNI": 6164631, "Puesto": "Assistant Professor", "Salario": 434321.31}
]


keys_lista_rrhh = list(lista_empleados_rrhh[0].keys())
# print(keys_lista_rrhh)

# ingresar_empleado_lista(lista_empleados_rrhh)

# ayuda = modificar_empleado(lista_empleados_rrhh, keys_lista_rrhh)

# ayuda2 = eliminar_empleado(lista_empleados_rrhh, lista_despedidos_rrhh)

# for empleado in lista_empleados_rrhh:
#     print(empleado)

# print("="*40)

# for despedido in lista_despedidos_rrhh:
#     print(despedido)

# mostrar_lista_empleados(lista_empleados_rrhh)

# promedio = calcular_promedio_salario(lista_empleados_rrhh)
# print(promedio)

# mostrar_empleado(lista_empleados_rrhh[0])

ordenar_lista_empleados(lista_empleados_rrhh, keys_lista_rrhh)


