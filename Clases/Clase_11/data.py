from class_video import Video

lista_videos = [
    Video("Trueno | Sesión #1", 25000000, 210, "https://www.youtube.com/watch?v=trueno1", "2020-06-05"),
    Video("Nathy Peluso | Sesión #36", 85000000, 180, "https://www.youtube.com/watch?v=nathypeluso36", "2020-11-27"),
    Video("Khea | Sesión #34", 65000000, 220, "https://www.youtube.com/watch?v=khea34", "2020-08-12"),
    Video("Nicki Nicole | Sesión #13", 130000000, 200, "https://www.youtube.com/watch?v=nicki13", "2019-04-23"),
    Video("YSY A | Sesión #37", 70000000, 210, "https://www.youtube.com/watch?v=ysya37", "2021-01-15"),
    Video("L-Gante | Sesión #38", 80000000, 190, "https://www.youtube.com/watch?v=lgante38", "2021-03-09"),
    Video("Duki | Sesión #50", 120000000, 210, "https://www.youtube.com/watch?v=duki50", "2022-05-14"),
    Video("Tiago PZK | Sesión #48", 95000000, 230, "https://www.youtube.com/watch?v=tiago48", "2022-02-20"),
    Video("Rauw Alejandro | Sesión #39", 110000000, 220, "https://www.youtube.com/watch?v=rauw39", "2021-05-15"),
    Video("Cazzu | Sesión #32", 72000000, 215, "https://www.youtube.com/watch?v=cazzu32", "2020-07-10"),
    Video("Nicky Jam | Sesión #40", 100000000, 195, "https://www.youtube.com/watch?v=nicky40", "2021-07-01"),
    Video("Anuel AA | Sesión #45", 115000000, 210, "https://www.youtube.com/watch?v=anuel45", "2021-11-05"),
    Video("Bad Bunny | Sesión #52", 150000000, 220, "https://www.youtube.com/watch?v=bunny52", "2022-06-10"),
    Video("Residente | Sesión #49", 90000000, 240, "https://www.youtube.com/watch?v=residente49", "2022-04-03"),
    Video("Ozuna | Sesión #44", 130000000, 215, "https://www.youtube.com/watch?v=ozuna44", "2021-10-25"),
    Video("Myke Towers | Sesión #43", 95000000, 200, "https://www.youtube.com/watch?v=myke43", "2021-09-30"),
    Video("Lunay | Sesión #47", 80000000, 205, "https://www.youtube.com/watch?v=lunay47", "2021-12-20"),
    Video("Jhay Cortez | Sesión #46", 100000000, 220, "https://www.youtube.com/watch?v=jhay46", "2021-11-30"),
    Video("Sech | Sesión #41", 95000000, 210, "https://www.youtube.com/watch?v=sech41", "2021-08-15"),
    Video("Arcángel | Sesión #42", 110000000, 225, "https://www.youtube.com/watch?v=arcangel42", "2021-09-01")
]
from funciones_decorativas import mensaje_programa

def menu():
    flag_1 = False
    continuar = True
    while continuar:
        mensaje_programa(1)
        inicio = input("Ingrese una opcion : A, B, C, D, E, F, G, H, X: ")
        inicio = inicio.upper()

        if inicio == "A":
            # A. NORMALIZAR OBJETOS
            if flag_1 == False:
                for i in range(len(lista_videos)):
                    lista_videos[i].dividir_titulo()
                    lista_videos[i].obtener_codigo_url()
                    lista_videos[i].formatear_fecha()
        
                if type(lista_videos) == list: 
                    flag_1 = True
                    mensaje_programa(4)
            else:
                mensaje_programa(5)    

        elif inicio == "B" and flag_1 == True:
            #B. MOSTRAR TEMAS
            print(f"{"*" * 60}")
            for x in range(len(lista_videos)):
                lista_videos[x].mostrar_tema()

        elif inicio == "C" and flag_1 == True:
            # C. ORDENAR TEMAS
            Video.ordenar_temas(lista_videos)
            print(f"{"*" * 60}")
            for x in range(len(lista_videos)):
                lista_videos[x].mostrar_tema()
            pass

        elif inicio == "D" and flag_1 == True:
            # D. PROMEDIO DE VISTAS
            Video.promediar_visitas(lista_videos)
    
        elif inicio == "E" and flag_1 == True:
            # MAXIMA REPRODUCCION: mostrar el o los videos con mayor cantidad de vistas.
            Video.calcular_maximo_reproducciones(lista_videos)
    
        elif inicio == "F" and flag_1 == True:
            # BUSQUEDA POR CODIGO: mostrar los videos cuyo código comiencen con la palabra "nick"
            Video.buscar_codigo_url(lista_videos,"nick")
    
        elif inicio == "G" and flag_1 == True:
            # LISTAR POR COLABORADOR: el usuario ingresa el nombre de un colaborador y el programa deberá listar todos los videos de
            colaborador = input("Ingrese nombre de colaborador: ") 
            colaborador = colaborador.strip()
            Video.buscar_colaborador(lista_videos, colaborador)
        
        elif inicio == "H":
            # H. LISTAR POR MES: el usuario ingresa un mes, y se deberán listar todos los temas lanzados en ese mes (sin importar el año)
            mes = input("Ingrese el mes en numeros: \n")
            print(f"{"*" * 60}")
            mes = mes.strip()
            Video.buscar_por_mes(lista_videos,mes)

        elif inicio == "X":
            # Cerrar programa(salir)
            mensaje_programa(3)
            continuar = False