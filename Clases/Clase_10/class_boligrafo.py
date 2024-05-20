class Lapicera:
    
    def __init__(self, color: str, grosor_punta: str):
        self.capacidad_tinta_maxima = 100
        self.grosor_punta = grosor_punta
        self.color = color
        self.capacidad_tinta = 80

    def escribir(self, texto: str) -> str:
        # Empiezo la funcion pidiendo la cadena a escribir.
        # A esa cadena le saco los espacios para compararla.
        texto_sin_espacios = texto.strip(" ")

        # Despues, reviso primero que tipo de grosor tiene la lapicera.
        # Armo una condicional para cada caso.
        if self.grosor_punta == "Fino":
            # Si el grosor es "Fino", le resto a la capacidad de tinta
            # la cantidad de caracteres que tiene la cadena.
            # Si no alcanza, muestra "No alcanza la tinta".
            if self.capacidad_tinta >= len(texto_sin_espacios):
                self.capacidad_tinta -= len(texto_sin_espacios)
                mensaje = texto
            else:
                mensaje = "No alcanza la tinta."

        elif self.grosor_punta == "Grueso":
            # Si el grosor es "Grueso", le resto a la capacidad de tinta
            # el doble de la cantidad de caracteres que tiene la cadena.
            # Si no alcanza, muestra "No alcanza la tinta".
            if self.capacidad_tinta >= len(texto_sin_espacios) * 2:
                self.capacidad_tinta -= len(texto_sin_espacios) * 2
                mensaje = texto.upper()
            else:
                mensaje = "No alcanza la tinta."

        return mensaje
    
    def recargar(self, cantidad: int) -> str:
        cantidad_a_recargar = self.capacidad_tinta # Asigno variable con el valor actual de la tinta
        cantidad_a_recargar += cantidad # Le sumo la cantidad de tinta a recargar

        # Abro un condicional que revise si la cantidad de tinta a recargar
        # excede la cantidad de tinta maxima.
        if cantidad_a_recargar > self.capacidad_tinta_maxima: 
            # Si la cantidad a recargar es mayor a la capacidad maxima
            # 1) Se le asigna a la capacidad de la tinta el mismo valor que la capacidad maxima
            # 2) Se resta la capacidad maxima a la suma de la capacidad maxima + capacidad actual
            # 3) Muestro el mensaje indicando que la accion fue realizada,
            #    junto al excedente de tinta
            self.capacidad_tinta = self.capacidad_tinta_maxima
            cantidad_excedente = cantidad_a_recargar - self.capacidad_tinta_maxima
            mensaje = f"Se recargó la lapicera al máximo, y sobró {cantidad_excedente} cantidad de tinta."

        else:
            self.capacidad_tinta = cantidad_a_recargar
            mensaje = f"Se recargó la lapicera"

        return mensaje
    

def mostrar_menu() -> int:
    print("1. Escribir con el bolígrafo")
    print("2. Recargar el bolígrafo")
    print("3. Mostrar la tinta del bolígrafo")
    print("4. Salir\n")
    opcion = int(input("Seleccione una opción: "))
    
    return opcion