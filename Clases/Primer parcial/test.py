from input_paquete.input_func import *
from menus import *
from dict_paquete.funciones import *
from pacientes import *
import json


# grupo_sanguineo = ["A", "B", "AB", "0"]
# get_string_excluyente_2("Ingrese: ", 1, 4, grupo_sanguineo, 3)

# lista = [
#     {
#     "ID": 103,
#     "Nombre": "Carlos",
#     "Apellido": "Rodríguez",
#     "DNI": "98765432",
#     "Tipo de Sangre": "B+",
#     "Edad": 40,
#     "Altura": 1.80,
#     "Peso": 85.0
# }]

# parser_csv("MOCK_DATA.csv", lista)

# verde_1 = "\033[38;5;22m"
# verde_2 = "\033[0;32m"
# violeta = "\033[0;35m"
# reset = "\033[0m"

# overwrite_csv("MOCK_DATA_2.csv", lista)

# def crear_menus(keys: list, color: str):
    
#     string = f"{color}"
#     for i in range(len(keys)):
#         if i + 1 == len(keys):
#             string += f"- {keys[i]}"
#         else:
#             string += f"- {keys[i]}\n"
#     string += f"{reset}"

#     return string


# def filtrar_dni(lista: list[dict], nuevo_dni: str):
#     lista_dnis = []

#     for i in range(len(lista)):
#         dni = lista[i]["DNI"]
#         lista_dnis.append(dni)

#     set_dni_lista = set(lista_dnis)
#     set_dni_nuevo = {nuevo_dni}

#     if len(set_dni_nuevo.intersection(set_dni_lista)) > 0:
#         return True
#     else:
#         return False

# lista = []
# parser_csv("MOCK_DATA", lista)

# print(filtrar_dni(lista, "05612424"))

# def buscar_dni(lista_pacientes: list):
#     ingreso = (input("que dni queres buscar: "))
#     for paciente in lista_pacientes:
#         if paciente["DNI"] == ingreso:
#             mostrar_paciente(paciente)

lista = [
{'ID': 1, 'Nombre': 'Joni', 'Apellido': 'Barensen', 'DNI': '88624337', 'Grupo sanguineo': 'A', 'Edad': 94, 'Altura': 98, 'Peso': 90.88}, {'ID': 2, 'Nombre': 'Lesly', 'Apellido': 'Georgeon', 'DNI': '81107613', 'Grupo sanguineo': 'B', 'Edad': 54, 'Altura': 126, 'Peso': 272.95}, {'ID': 3, 'Nombre': 'Cullen', 'Apellido': 'Everix', 'DNI': '83586341', 'Grupo sanguineo': 'B', 'Edad': 9, 'Altura': 227, 'Peso': 226.04}, {'ID': 4, 'Nombre': 'Jere', 'Apellido': 'Smart', 'DNI': '17936187', 'Grupo sanguineo': 'AB', 'Edad': 95, 'Altura': 137, 'Peso': 10.43}, {'ID': 5, 'Nombre': 'Dorey', 'Apellido': 'Starbucke', 'DNI': '95246768', 'Grupo sanguineo': 'AB', 'Edad': 21, 'Altura': 131, 'Peso': 201.87}, {'ID': 6, 'Nombre': 'Shelia', 'Apellido': 'Dacca', 'DNI': '54456561', 'Grupo sanguineo': 'B', 'Edad': 61, 'Altura': 52, 'Peso': 254.37}, {'ID': 7, 'Nombre': 'Chad', 'Apellido': 'Gogie', 'DNI': '93173172', 'Grupo sanguineo': 'A', 'Edad': 5, 'Altura': 115, 'Peso': 267.23}, {'ID': 8, 'Nombre': 'Anetta', 'Apellido': 'Inston', 'DNI': '80295918', 'Grupo sanguineo': '0', 'Edad': 6, 'Altura': 112, 'Peso': 155.6}, {'ID': 9, 'Nombre': 'Humfried', 'Apellido': 'Craker', 'DNI': '86588482', 'Grupo sanguineo': 'A', 'Edad': 84, 'Altura': 200, 'Peso': 280.15}, {'ID': 10, 'Nombre': 'Enrico', 'Apellido': 'Wale', 'DNI': '49207803', 'Grupo sanguineo': 'A', 'Edad': 4, 'Altura': 119, 'Peso': 206.19}, {'ID': 11, 'Nombre': 'Perice', 'Apellido': 'Lohrensen', 'DNI': '73665753', 'Grupo sanguineo': 'A', 'Edad': 91, 'Altura': 115, 'Peso': 147.54}, {'ID': 12, 'Nombre': 'Cornie', 'Apellido': 'Woodroofe', 'DNI': '75530791', 'Grupo sanguineo': 'AB', 'Edad': 111, 'Altura': 104, 'Peso': 78.49}, {'ID': 13, 'Nombre': 'Patty', 'Apellido': 
'Blessed', 'DNI': '79877753', 'Grupo sanguineo': 'A', 'Edad': 112, 'Altura': 182, 'Peso': 246.57}, {'ID': 14, 'Nombre': 'Ekaterina', 'Apellido': 'McLuckie', 'DNI': '17877645', 'Grupo sanguineo': 'B', 'Edad': 114, 'Altura': 66, 'Peso': 78.41}, {'ID': 15, 'Nombre': 'Osmond', 'Apellido': 'Botha', 'DNI': '42037036', 'Grupo sanguineo': 'AB', 'Edad': 65, 'Altura': 114, 'Peso': 23.53}, {'ID': 16, 'Nombre': 'Tarah', 'Apellido': 'Bowes', 'DNI': '15324372', 'Grupo sanguineo': 'AB', 'Edad': 30, 'Altura': 112, 'Peso': 154.68}, {'ID': 17, 'Nombre': 'Arleyne', 'Apellido': 'Blanchet', 'DNI': '56770519', 'Grupo sanguineo': 'B', 'Edad': 32, 'Altura': 81, 'Peso': 103.2}, {'ID': 18, 'Nombre': 'Selestina', 'Apellido': 'Verillo', 'DNI': '47255904', 'Grupo sanguineo': '0', 'Edad': 111, 'Altura': 78, 'Peso': 60.74}, {'ID': 19, 'Nombre': 'Marshal', 'Apellido': 'Rosenhaupt', 'DNI': '21243198', 'Grupo sanguineo': 'AB', 'Edad': 12, 'Altura': 86, 'Peso': 264.67}, {'ID': 20, 'Nombre': 'Gerik', 'Apellido': 'Prydden', 'DNI': '44169951', 'Grupo sanguineo': 'B', 'Edad': 40, 'Altura': 165, 'Peso': 24.93}, {'ID': 21, 'Nombre': 'Krystal', 'Apellido': 'Chominski', 'DNI': '48685796', 'Grupo sanguineo': '0', 'Edad': 
42, 'Altura': 166, 'Peso': 206.79}, {'ID': 22, 'Nombre': 'Irvin', 'Apellido': 'Spratley', 'DNI': '77638097', 'Grupo sanguineo': 'A', 'Edad': 74, 'Altura': 85, 'Peso': 264.64}, {'ID': 23, 'Nombre': 'Licha', 'Apellido': 'Mattevi', 'DNI': '61423877', 'Grupo sanguineo': '0', 'Edad': 69, 'Altura': 34, 'Peso': 194.91}, {'ID': 24, 'Nombre': 'Catlaina', 'Apellido': 'Oldridge', 'DNI': '99672242', 'Grupo sanguineo': 'B', 'Edad': 60, 'Altura': 102, 'Peso': 260.79}, {'ID': 25, 'Nombre': 'Hamel', 'Apellido': 'Lillecrap', 'DNI': '34371170', 'Grupo sanguineo': 'B', 'Edad': 70, 'Altura': 92, 'Peso': 229.84}, {'ID': 26, 'Nombre': 'Reta', 'Apellido': 'Deware', 'DNI': '58288031', 'Grupo sanguineo': '0', 'Edad': 42, 'Altura': 119, 'Peso': 278.32}, {'ID': 27, 'Nombre': 'Karney', 'Apellido': 'Dameisele', 'DNI': '57307075', 'Grupo sanguineo': '0', 'Edad': 65, 'Altura': 171, 'Peso': 172.22}, {'ID': 28, 'Nombre': 'Seana', 'Apellido': 'Matyashev', 'DNI': '95921968', 'Grupo sanguineo': '0', 'Edad': 102, 'Altura': 65, 'Peso': 67.61}, {'ID': 29, 'Nombre': 'Berkeley', 'Apellido': 'Leidl', 'DNI': '98870998', 'Grupo sanguineo': '0', 'Edad': 25, 'Altura': 217, 'Peso': 194.83}, {'ID': 30, 'Nombre': 'Brandon', 'Apellido': 'Stelle', 'DNI': '79579797', 'Grupo sanguineo': 'B', 'Edad': 3, 'Altura': 153, 'Peso': 196.64}, {'ID': 31, 'Nombre': 'Pate', 'Apellido': 'Sutter', 'DNI': '23200598', 'Grupo sanguineo': 'AB', 'Edad': 101, 'Altura': 68, 'Peso': 251.67}, {'ID': 32, 'Nombre': 'Piper', 'Apellido': 'Pawlik', 'DNI': '88852457', 'Grupo sanguineo': '0', 'Edad': 99, 'Altura': 214, 'Peso': 27.42}, {'ID': 33, 'Nombre': 'Chaddy', 'Apellido': 'Johncey', 'DNI': '07241518', 'Grupo sanguineo': 'A', 'Edad': 26, 'Altura': 82, 'Peso': 193.63}, {'ID': 34, 'Nombre': 'Jacobo', 'Apellido': 'Comettoi', 'DNI': '25885693', 'Grupo sanguineo': 'AB', 'Edad': 13, 'Altura': 110, 'Peso': 24.38}, {'ID': 35, 'Nombre': 'Stanly', 'Apellido': 'Samuels', 'DNI': '76877866', 'Grupo sanguineo': 'B', 'Edad': 114, 'Altura': 94, 'Peso': 44.77}, {'ID': 36, 'Nombre': 'Hobey', 'Apellido': 'Roullier', 'DNI': '61115623', 'Grupo sanguineo': '0', 'Edad': 99, 'Altura': 58, 'Peso': 236.31}, {'ID': 37, 'Nombre': 'Flora', 'Apellido': 'Beddoes', 'DNI': '32421528', 'Grupo sanguineo': 'A', 'Edad': 43, 'Altura': 88, 'Peso': 105.01}, {'ID': 38, 'Nombre': 'Heywood', 'Apellido': 'Gronw', 'DNI': '33636623', 'Grupo sanguineo': 'B', 'Edad': 82, 'Altura': 162, 'Peso': 186.57}, {'ID': 39, 'Nombre': 'Grove', 'Apellido': 'Notton', 'DNI': '12336540', 'Grupo sanguineo': 'AB', 'Edad': 67, 'Altura': 201, 'Peso': 123.92}, {'ID': 40, 'Nombre': 'Cyndy', 'Apellido': 'Chater', 'DNI': '39069303', 'Grupo sanguineo': 'A', 'Edad': 96, 'Altura': 114, 'Peso': 273.51}, {'ID': 41, 'Nombre': 'Bradford', 'Apellido': 'Dobinson', 'DNI': '14145993', 'Grupo sanguineo': '0', 'Edad': 40, 'Altura': 41, 'Peso': 72.21}, {'ID': 42, 'Nombre': 'Win', 'Apellido': 'Lacotte', 'DNI': '32826090', 'Grupo sanguineo': '0', 'Edad': 77, 'Altura': 73, 'Peso': 113.58}, {'ID': 43, 'Nombre': 'Reina', 'Apellido': 'Shutler', 'DNI': '95960396', 'Grupo sanguineo': 'B', 'Edad': 26, 'Altura': 165, 'Peso': 243.52}, {'ID': 44, 'Nombre': 'Cacilia', 'Apellido': 'Domange', 'DNI': '36939703', 'Grupo sanguineo': 'A', 'Edad': 76, 'Altura': 115, 'Peso': 136.12}, {'ID': 45, 'Nombre': 'Sanford', 'Apellido': 'Grelak', 'DNI': '29912381', 'Grupo sanguineo': 'A', 'Edad': 74, 'Altura': 45, 'Peso': 288.03}, {'ID': 46, 'Nombre': 'Juanita', 'Apellido': 'Ortell', 'DNI': '94182804', 'Grupo sanguineo': 'B', 'Edad': 21, 'Altura': 99, 'Peso': 182.17}, {'ID': 47, 'Nombre': 'Gayle', 'Apellido': 'Craisford', 'DNI': '48754205', 'Grupo sanguineo': 'A', 'Edad': 23, 'Altura': 68, 'Peso': 295.54}, {'ID': 48, 'Nombre': 'Christoffer', 'Apellido': 'Scardifield', 'DNI': '06119564', 'Grupo sanguineo': 'AB', 'Edad': 40, 'Altura': 182, 'Peso': 144.63}, {'ID': 49, 'Nombre': 'Dorry', 'Apellido': 'Mc Mechan', 'DNI': '21069553', 'Grupo sanguineo': 'B', 'Edad': 105, 'Altura': 138, 'Peso': 83.6}, {'ID': 50, 'Nombre': 'Jaime', 'Apellido': 'Clift', 'DNI': '95566509', 'Grupo sanguineo': '0', 'Edad': 104, 'Altura': 211, 'Peso': 
147.71}, {'ID': 51, 'Nombre': 'Stu', 'Apellido': 'Slocumb', 'DNI': '46074517', 'Grupo sanguineo': 'AB', 'Edad': 53, 'Altura': 221, 'Peso': 251.42}, {'ID': 52, 'Nombre': 'Dilly', 'Apellido': 'Gounard', 'DNI': '97985249', 'Grupo sanguineo': '0', 'Edad': 36, 'Altura': 93, 'Peso': 244.61}, {'ID': 53, 'Nombre': 'Averill', 'Apellido': 'Maryon', 'DNI': '22795515', 'Grupo sanguineo': 'B', 'Edad': 38, 'Altura': 142, 'Peso': 20.07}, {'ID': 54, 'Nombre': 'Dorey', 'Apellido': 'Schoroder', 'DNI': '66475975', 'Grupo sanguineo': 'AB', 'Edad': 107, 'Altura': 169, 'Peso': 34.48}, {'ID': 55, 'Nombre': 'Cherye', 'Apellido': 'Letherbury', 'DNI': '80131777', 'Grupo sanguineo': 'A', 'Edad': 72, 'Altura': 114, 'Peso': 59.04}, {'ID': 56, 'Nombre': 'Cosmo', 'Apellido': 'Fowell', 'DNI': '58315924', 'Grupo sanguineo': 'B', 'Edad': 113, 'Altura': 196, 'Peso': 210.21}, {'ID': 57, 'Nombre': 'Christiana', 'Apellido': 'Seabridge', 'DNI': '28833921', 'Grupo sanguineo': 'AB', 'Edad': 31, 'Altura': 165, 'Peso': 187.94}, {'ID': 58, 'Nombre': 'Jakob', 'Apellido': 'Innett', 'DNI': '61073994', 'Grupo sanguineo': '0', 'Edad': 54, 'Altura': 191, 'Peso': 125.91}, {'ID': 59, 'Nombre': 'Regan', 'Apellido': 'Courson', 'DNI': '90263906', 'Grupo sanguineo': 'B', 'Edad': 19, 'Altura': 68, 'Peso': 94.31}, {'ID': 60, 'Nombre': 'Caitlin', 'Apellido': 'Ginnety', 'DNI': '22160527', 'Grupo sanguineo': 'A', 'Edad': 68, 'Altura': 168, 'Peso': 108.98}, {'ID': 61, 'Nombre': 'Guthrey', 'Apellido': 'Owttrim', 'DNI': '82423700', 'Grupo sanguineo': 'B', 'Edad': 75, 'Altura': 207, 'Peso': 109.27}, {'ID': 62, 'Nombre': 'Vin', 'Apellido': 'Schrei', 'DNI': '43677272', 'Grupo sanguineo': 'A', 'Edad': 44, 'Altura': 31, 'Peso': 17.24}, {'ID': 63, 'Nombre': 'Howie', 'Apellido': 'Tendahl', 'DNI': '63081646', 'Grupo sanguineo': 'B', 'Edad': 100, 'Altura': 36, 'Peso': 122.66}, {'ID': 64, 'Nombre': 'Alfi', 'Apellido': 'Dohrmann', 'DNI': '20344337', 'Grupo sanguineo': 'A', 'Edad': 95, 'Altura': 116, 'Peso': 18.71}, {'ID': 65, 'Nombre': 'Guinna', 'Apellido': 'Peeke', 'DNI': '21437397', 'Grupo sanguineo': '0', 'Edad': 24, 'Altura': 223, 'Peso': 153.06}, {'ID': 66, 'Nombre': 'Mandel', 'Apellido': 'Rose', 'DNI': '75429887', 'Grupo sanguineo': 'AB', 'Edad': 112, 
'Altura': 174, 'Peso': 225.93}, {'ID': 67, 'Nombre': 'Kora', 'Apellido': 'Cocke', 'DNI': '98324116', 'Grupo sanguineo': 'A', 'Edad': 17, 'Altura': 225, 'Peso': 153.07}, {'ID': 68, 'Nombre': 'Giovanni', 'Apellido': 'Dulake', 'DNI': '79257609', 'Grupo sanguineo': '0', 'Edad': 18, 'Altura': 81, 'Peso': 236.95}, {'ID': 69, 'Nombre': 'Fidole', 'Apellido': 'Bauchop', 'DNI': '37415784', 'Grupo sanguineo': '0', 'Edad': 90, 'Altura': 76, 'Peso': 42.22}, {'ID': 70, 'Nombre': 'Goddard', 'Apellido': 'Lafond', 'DNI': '21891922', 'Grupo sanguineo': '0', 'Edad': 39, 'Altura': 71, 'Peso': 81.24}, {'ID': 71, 'Nombre': 'Abbie', 'Apellido': 'Jesse', 'DNI': '92481850', 'Grupo sanguineo': 'AB', 'Edad': 70, 'Altura': 92, 'Peso': 229.24}, {'ID': 72, 'Nombre': 'Friederike', 'Apellido': 'Domenget', 'DNI': '17675768', 'Grupo sanguineo': 'B', 'Edad': 81, 'Altura': 228, 
'Peso': 40.28}, {'ID': 73, 'Nombre': 'Porty', 'Apellido': 'Pither', 'DNI': '68787185', 'Grupo sanguineo': '0', 'Edad': 73, 'Altura': 48, 'Peso': 59.81}, {'ID': 74, 'Nombre': 'Goober', 'Apellido': 'Meeks', 'DNI': '54520968', 'Grupo sanguineo': 'A', 'Edad': 15, 'Altura': 191, 'Peso': 246.2}, {'ID': 75, 'Nombre': 'Cortney', 'Apellido': 'Parrin', 'DNI': '23330291', 'Grupo sanguineo': 'AB', 'Edad': 13, 'Altura': 113, 'Peso': 121.37}, {'ID': 76, 'Nombre': 'Normie', 'Apellido': 'Greenwood', 'DNI': '49957817', 'Grupo sanguineo': '0', 'Edad': 104, 'Altura': 227, 'Peso': 252.94}, {'ID': 77, 'Nombre': 'Theo', 'Apellido': 'Reinbech', 'DNI': '66266302', 'Grupo sanguineo': 'B', 'Edad': 99, 'Altura': 40, 'Peso': 43.45}, {'ID': 78, 'Nombre': 'Dagmar', 'Apellido': 'Mulqueeny', 'DNI': '61333980', 'Grupo sanguineo': 'B', 'Edad': 42, 'Altura': 138, 'Peso': 159.43}, {'ID': 79, 'Nombre': 'Rudiger', 'Apellido': 'Sapey', 'DNI': '52162890', 'Grupo sanguineo': 'A', 'Edad': 71, 'Altura': 51, 'Peso': 148.52}, {'ID': 80, 'Nombre': 'Annadiana', 'Apellido': 'Crofthwaite', 'DNI': '20074683', 'Grupo sanguineo': '0', 'Edad': 9, 'Altura': 128, 'Peso': 297.13}, {'ID': 81, 'Nombre': 'Siusan', 'Apellido': 'Welsh', 'DNI': '15872201', 'Grupo sanguineo': 'AB', 'Edad': 1, 'Altura': 128, 'Peso': 179.99}, {'ID': 82, 'Nombre': 'Grant', 'Apellido': 'Blaw', 'DNI': '72488206', 'Grupo sanguineo': 'B', 'Edad': 20, 'Altura': 122, 'Peso': 94.44}, {'ID': 83, 'Nombre': 'Magdalene', 'Apellido': 'Sorensen', 'DNI': '40777914', 'Grupo sanguineo': '0', 'Edad': 45, 'Altura': 87, 'Peso': 220.03}, {'ID': 84, 'Nombre': 'Gonzales', 'Apellido': 'Allin', 'DNI': '08593606', 'Grupo sanguineo': 'A', 'Edad': 29, 'Altura': 47, 'Peso': 163.05}, {'ID': 
85, 'Nombre': 'Barthel', 'Apellido': 'Struis', 'DNI': '05216630', 'Grupo sanguineo': 'B', 'Edad': 24, 'Altura': 33, 'Peso': 15.04}, {'ID': 86, 'Nombre': 'Miguelita', 'Apellido': 'Martinyuk', 'DNI': '49220687', 'Grupo sanguineo': 'A', 'Edad': 2, 'Altura': 208, 'Peso': 277.43}, {'ID': 87, 'Nombre': 'Darby', 'Apellido': 'Newark', 'DNI': '79893013', 'Grupo sanguineo': 'A', 'Edad': 7, 'Altura': 195, 'Peso': 95.14}, {'ID': 88, 'Nombre': 'Vernen', 'Apellido': 'Balharrie', 'DNI': '08130277', 'Grupo sanguineo': 'B', 
'Edad': 27, 'Altura': 205, 'Peso': 90.88}, {'ID': 89, 'Nombre': 'Philbert', 'Apellido': 'Grocutt', 'DNI': '91447554', 'Grupo sanguineo': 'B', 'Edad': 74, 'Altura': 64, 'Peso': 274.2}, {'ID': 90, 'Nombre': 'Avigdor', 'Apellido': 'Penhall', 'DNI': '52863301', 'Grupo sanguineo': 'B', 'Edad': 93, 'Altura': 168, 'Peso': 86.39}, {'ID': 91, 'Nombre': 'Bat', 'Apellido': 'Caret', 'DNI': '08593925', 'Grupo sanguineo': '0', 'Edad': 7, 'Altura': 176, 'Peso': 144.39}, {'ID': 92, 'Nombre': 'Yoshiko', 'Apellido': 'Pfeifer', 'DNI': '04085227', 'Grupo sanguineo': 'AB', 'Edad': 84, 'Altura': 64, 'Peso': 273.12}, {'ID': 93, 'Nombre': 'Heda', 'Apellido': 'Kensett', 'DNI': '13619717', 'Grupo sanguineo': 'AB', 'Edad': 8, 'Altura': 74, 'Peso': 216.8}, {'ID': 94, 'Nombre': 'Sly', 'Apellido': 'Guirardin', 'DNI': '22901974', 'Grupo sanguineo': 'B', 'Edad': 5, 'Altura': 69, 'Peso': 114.1}, {'ID': 95, 'Nombre': 'Giulietta', 'Apellido': 'Barbera', 'DNI': '77440027', 'Grupo sanguineo': 'B', 'Edad': 110, 'Altura': 60, 'Peso': 176.46}, {'ID': 96, 'Nombre': 'Claus', 'Apellido': 'Fidge', 'DNI': '51698674', 'Grupo sanguineo': 'B', 'Edad': 51, 'Altura': 195, 'Peso': 162.31}, {'ID': 97, 'Nombre': 'Ruthi', 'Apellido': 'Bercher', 'DNI': '04408176', 'Grupo sanguineo': '0', 'Edad': 48, 'Altura': 220, 'Peso': 279.32}, {'ID': 98, 'Nombre': 'Florian', 'Apellido': 'Ferie', 'DNI': '47220261', 'Grupo sanguineo': '0', 'Edad': 21, 'Altura': 47, 'Peso': 212.81}, {'ID': 99, 'Nombre': 'Loree', 'Apellido': 'Hallex', 'DNI': '05612424', 'Grupo sanguineo': 'B', 'Edad': 54, 'Altura': 218, 'Peso': 179.94}, {'ID': 100, 'Nombre': 'Pen', 'Apellido': 'Leith-Harvey', 'DNI': '72553966', 'Grupo sanguineo': 'A', 'Edad': 32, 'Altura': 98, 'Peso': 
58.04}, {'ID': 101, 'Nombre': 'Federico', 'Apellido': 'Aieta', 'DNI': '12484124', 'Grupo sanguineo': 'B-', 'Edad': 17, 'Altura': 172, 'Peso': 56.6}, {'ID': 102, 'Nombre': 
'Federiquin', 'Apellido': 'Aietin', 'DNI': '14884184', 'Grupo sanguineo': 'Ab-', 'Edad': 18, 'Altura': 172, 'Peso': 109.5}]

# lista = [{'ID': 105, 'Nombre': 'Joni', 'Apellido': 'Barensen', 'DNI': '88624337', 'Grupo sanguineo': 'A', 'Edad': 94, 'Altura': 98, 'Peso': 90.88},
#          {'ID': 105, 'Nombre': 'Joni', 'Apellido': 'Barensen', 'DNI': '88624337', 'Grupo sanguineo': 'A', 'Edad': 94, 'Altura': 98, 'Peso': 90.88}]

# def overwrite_csv(path, lista):
#     try:
#         with open(f"{path}.csv", 'w', encoding="utf8") as archivo:
#             cabecera = "ID,Nombre,Apellido,DNI,Tipo de Sangre,Edad,Altura,Peso\n"
#             string = ""
#             for linea in lista:
#                 valores = lista[linea].values()
                


#     except:
#         print("No se pudo realizar el reemplazo de información.")

# overwrite_csv("pacientes_datos copy", lista)

# def overwrite_csv(path, lista):
#     with open(path, "w", encoding= "utf-8") as archivo:
#         lista_keys = list(lista[0].keys())
#         registro_keys = ",".join(lista_keys) + "\n"
#         archivo.write(registro_keys)

#         for i in range(len(lista)):
#             if i != len(lista) - 1:
#                 string = (f"{lista[i]["ID"]},{lista[i]["Nombre"]},{lista[i]["Apellido"]},"
#                     f"{lista[i]["DNI"]},{lista[i]["Grupo sanguineo"]},{lista[i]["Edad"]},"
#                     f"{lista[i]["Altura"]},{lista[i]["Peso"]}\n")
#             else:
#                 string = (f"{lista[i]["ID"]},{lista[i]["Nombre"]},{lista[i]["Apellido"]},"
#                         f"{lista[i]["DNI"]},{lista[i]["Grupo sanguineo"]},{lista[i]["Edad"]},"
#                         f"{lista[i]["Altura"]},{lista[i]["Peso"]}")
                
#             archivo.write(string)

# # overwrite_csv("bellas_damas.csv", lista)

# # diccionario = {"last_id": 100, "bajas": 0}

# # def config_json(path, config: dict):
# #     with open(path, "w", encoding= "utf-8") as archivo:
# #         json.dump(config, archivo, indent=4)

# def extract_config_json(path):
#     try:
#         with open(f"{path}.json", 'r', encoding='utf-8') as archivo:
#             data = json.load(archivo)
#         extraccion = [data["config"]]
#         lista = [extraccion[0]]
#         return lista[0]

#     except FileNotFoundError:
#         data = {}
#         data["config"] = {"last_id": 0,
#                         "bajas": 0,
#                         "reportes_salario": 0,
#                         "reportes_apellido": 0}
        
#         with open(f"{path}.json", 'w', encoding="utf-8") as archivo:
#             json.dump(data, archivo, indent= 4)
        
#         return data["config"]
    

# config = extract_config_json("config")
# print(config)

# def editar_config_json(path:str , nuevo_diccionario: dict):
#     try:
#         with open(f"{path}.json", 'r', encoding='utf-8') as archivo:
#             data = json.load(archivo)
        
#         data['config'] = nuevo_diccionario
        
#         with open(f"{path}.json", 'w', encoding='utf-8') as archivo:
#             json.dump(data, archivo, indent=4)
    
#     except FileNotFoundError:
#         print(f"El archivo '{path}.json' no existe.")
#         data = {}
#         data["config"] = nuevo_diccionario
#         with open(f"{path}.json", 'w', encoding="utf-8") as archivo:
#             json.dump(data, archivo, indent= 4)
    
#     except json.JSONDecodeError:
#         print(f"El archivo '{path}' no está en formato JSON correcto.")


# def agregar_bajas_json(path: str, nuevas_bajas: list[dict]):
#     try:
#         with open(path, 'r', encoding='utf-8') as archivo:
#             data = json.load(archivo)
        
#         data["bajas"] += nuevas_bajas

#     except FileNotFoundError:
#         data = {}
#         data["bajas"] = nuevas_bajas
    
#     except json.JSONDecodeError:
#         data = {}
#         data["bajas"] = nuevas_bajas

#     with open(path, 'w', encoding='utf-8') as archivo:
#         json.dump(data, archivo, indent=4)


# agregar_bajas_json("bajas.json", lista)

lista = ["a", "b", "c"]
variable = "a"

for dato in lista:
    if dato == variable:
        print("z")