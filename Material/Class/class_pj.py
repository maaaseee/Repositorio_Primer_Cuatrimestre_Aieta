class Personaje:
    # ATRIBUTOS:

    #  Nombre
    #  Usa_nano
    #  Puede_volar
    #  Super_poder
    #  Poder_pelea

    def __init__(self, nombre: str, nano: bool, vuela: bool, poder: int, pelea: int):
        self.nombre = nombre
        self.nano = nano
        self.vuela = vuela
        self.poder = poder
        self.pelea = pelea

    # MÉTODOS:

    def describirse(self) -> str:
        cadena = f"{self.nombre} - {self.poder} - {self.pelea}"
        if self.nano:
            cadena += " - Usa nanotecnología"
        else:
            cadena += " - No usa nanotecnología"

        return cadena
    
    def volar(self, altura, velocidad):
        if self.vuela:
            print(f"{self.nombre} vuela a una altura de {altura} mts, a una velicidad de {velocidad} km/h")
        else:
            print(f"{self.nombre}, usted no puede volar")

    def atacar(self, enemigo: 'Personaje'):
        if self.pelea > enemigo.pelea:
            print(f"Ganó {self.nombre}")
            self.pelea -= enemigo.pelea
            enemigo.pelea = 0

        elif self.poder < enemigo.poder:
            print(f"Ganó {enemigo.nombre}")
            enemigo.pelea -= self.pelea
            self.pelea = 0

        else:
            print("Empate")
            enemigo.pelea *= 0.9
            self.pelea *= 0.9

    # @staticmethod = Metodo sin self / Metodo que no depende de la instancia