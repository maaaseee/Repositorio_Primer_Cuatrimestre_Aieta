from datetime import datetime
import datetime

class Video:
    def __init__(self, titulo: str, vistas: int, tiempo: int, url_youtube: str, fecha_lanzamiento: str):
        self.titulo = titulo
        self.vistas = vistas
        self.tiempo = tiempo
        self.url_youtube = url_youtube
        self.fecha_lanzamiento = fecha_lanzamiento
        self.sesion = None
        self.colaborador = None
        self.codigo_url = None
        
    def mostrar_tema(self):
        #Agregar los datos pertinentes para que a la hora de mostrar se vean los datos completos del video
        print(f"Titulo: {self.titulo}")
        print(f"Vistas: {self.vistas}")
        print(f"Duración: {self.tiempo} segundos")
        print(f"URL de YouTube: {self.url_youtube}")
        print(f"Fecha de Lanzamiento: {self.fecha_lanzamiento.strftime("%d-%m-%Y")}")
        print("*"*60)

    def dividir_titulo(self):
        titulo = self.titulo
        titulo_dividido = titulo.split("#")

        colaborador = titulo_dividido[0]
        colaborador_2 = colaborador.rstrip(" Sesión #")
        colaborador_3 = colaborador_2.strip("|")
        self.colaborador = colaborador_3

        sesion = titulo_dividido[1]
        self.sesion = int(sesion)
    
    def obtener_codigo_url(self):
        #Debe setear el atributo codigo_url con el codigo obtenido del atributo url_youtube
        #Por ej: si la url es https://www.youtube.com/watch?v=nicki13 
        #el codigo seria nicki13
        codigo_url = self.url_youtube
        codigo_dividido = codigo_url.lstrip("https://www.youtube.com/watch?v")
        self.codigo_url = codigo_dividido.strip("=")
    
    def formatear_fecha(self):
        #Necesitamos que la fecha de lanzamiento sea un objeto de la clase datetime (investigar).
        #Para ello deberán dividir la fecha (en formato string) en dia, mes y año y a partir de 
        #esos datos, crear la nueva fecha. 
        fecha = self.fecha_lanzamiento.split("-")

        año = fecha[0]
        mes = fecha[1]
        dia = fecha[2]
        self.fecha_lanzamiento = datetime.date(int(año), int(mes), int(dia))

    def ordenar_temas(lista):
        # Debe ordenar la lista de temas por número de sesion
        n = len(lista)
        for i in range(n):
            for j in range(0, n - i - 1):
                if lista[j].sesion > lista[j + 1].sesion:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

    def promediar_visitas(lista_videos: list):
        #Debe calcular el promedio de vistas de todos los temas de la lista
        visitas_totales = 0
        for i in range(len(lista_videos)):
            visitas_totales += lista_videos[i].vistas

        promedio_visitas = visitas_totales / len(lista_videos)

        print(f"Promedio: {int(promedio_visitas//1000)}k")

    def calcular_maximo_reproducciones(lista_videos: list):
        # Busca en el atributo de vistas, el de mayor cantidad, y muestra a que video pertenece
        bandera = True
        maximo_reproducciones = 0
        for i in range(len(lista_videos)):
            if bandera == True or maximo_reproducciones < lista_videos[i].vistas:
                maximo_reproducciones = lista_videos[i].vistas
                bandera = False

        for j in range(len(lista_videos)):
            if maximo_reproducciones == lista_videos[j].vistas:
                lista_videos[j].mostrar_tema()
    
    def buscar_codigo_url(lista_videos: list, subcadena: str):
        # Busca el código de la url que coincida
        for i in range(len(lista_videos)):
            ayuda = lista_videos[i].codigo_url
            if subcadena == ayuda[:len(subcadena)]:
                lista_videos[i].mostrar_tema()

    def buscar_colaborador(lista_videos: list, subcadena: str):
        for i in range(len(lista_videos)):
            ayuda = lista_videos[i].colaborador
            if len(ayuda) >= len(subcadena) and subcadena == ayuda[:len(subcadena)]:
                lista_videos[i].mostrar_tema()

    def buscar_por_mes(lista_videos: list, mes: int):
        flag = False
        if type(lista_videos) == list and mes.isdigit() == True:
            for i in range(len(lista_videos)): 
                mes_lanzamiento = lista_videos[i].fecha_lanzamiento
                mes_lanzamiento = mes_lanzamiento.month
                if mes_lanzamiento == int(mes):
                    lista_videos[i].mostrar_tema()
                    flag = True
            if flag == False:
                print("Prueba")