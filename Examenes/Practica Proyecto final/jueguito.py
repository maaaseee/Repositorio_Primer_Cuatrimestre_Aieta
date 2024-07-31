import pygame
import random

# Inicio de Pygame
pygame.init()

# COLORES (RGB)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
AZUL_CLARO = (0, 150, 255)                                          
BLANCO = (255, 255, 255)

VIOLETA = (183, 109, 234)                               
VERDE_2 = (40, 114, 51)

# Resolucion de ventana
ANCHO = 1920
ALTO = 1060

# Inicialización de la resolucion de nuestra ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))          
# Titulo de ventana
pygame.display.set_caption("Mi primera chamba")              

# Rellana la pantalla con el color definiido
ventana.fill(VIOLETA)

# Traer un .jpg como icono
icono = pygame.image.load("imagenes/icono.jpg")
pygame.display.set_icon(icono)

# Traer un .jpg como imagen para la pantalla
imagen = pygame.image.load("imagenes/violet.jpg")
posXY = (150, 70)

# Litografía de texto, y su tamaño
fuente = pygame.font.SysFont("Arial", 60)
texto = fuente.render("Mi amooor", False, NEGRO, BLANCO)

# Reescalados de imagenes
kafka = pygame.image.load("imagenes/kafka.png")
reescalado_kafka = pygame.transform.scale(kafka, (172, 161))

gato = pygame.image.load("imagenes/gato.png")
rescalado_gato = pygame.transform.scale(gato, (500, 500))
rect_gato = rescalado_gato.get_rect()
rect_gato.topleft = (470, 220)

posiciones = []

boton = False
flag = True
while flag:

    lista_eventos = pygame.event.get()     # Evento = Suceso que ocurre según la accion del usuario
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:     # Salir del programa (BOTON X)
            flag = False
        elif evento.type == pygame.KEYUP:
            boton = True
        elif evento.type == pygame.KEYDOWN:
            boton = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # print(evento.pos)
            if rect_gato.collidepoint(evento.pos):
                pos_1 = random.randint(1, ANCHO)
                pos_2 = random.randint(1, ALTO)
                ventana.blit(rescalado_gato, (pos_1, pos_2))
    
    # Esto muestra las imagenes en pantalla
    if boton:
        mouse_pos = pygame.mouse.get_pos()
        m_x = mouse_pos[0]
        m_y = mouse_pos[1]
        ventana.blit(gato, [m_x, m_y])
    # ventana.blit(kafka, (100, 100))
    # ventana.blit(texto, (850, 100))
    # ventana.blit(kafka, (100, 100))
    # ventana.blit(reescalado_kafka, (700, 400))
    # ventana.blit(rescalado_gato, (0, 0))

    # for _ in range(5):
    #     pos_1 = random.randint(1, ANCHO)
    #     pos_2 = random.randint(1, ALTO)
    #     posiciones.append((pos_1, pos_2))

    # for pos in posiciones:
    #     pygame.draw.circle(ventana, NEGRO, pos, 5)

    pygame.display.update()                # Actualiza lo que está en pantalla (OBLIGATORIO)



pygame.quit()  # Cierra el programa, para evitar gasto de recursos