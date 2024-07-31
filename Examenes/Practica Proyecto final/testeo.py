import pygame
import random

# Inicio de Pygame
pygame.init()

### ---------------------------------------------------------------- ###

# COLORES (RGB)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
AZUL_CLARO = (0, 150, 255)                                          
BLANCO = (255, 255, 255)

VIOLETA = (183, 109, 234)                               
VERDE_2 = (40, 114, 51)


### ---------------------------------------------------------------- ###
# Resolucion de ventana
ANCHO = 1600
ALTO = 900
RESOLUCION = (ANCHO, ALTO)

# Inicialización de la resolucion de nuestra ventana
ventana = pygame.display.set_mode(RESOLUCION)

# Titulo de ventana
pygame.display.set_caption("Mi primera chamba")              

### ---------------------------------------------------------------- ###

# Traer un .jpg como icono
# icono = pygame.image.load("imagenes/icono.jpg")
# pygame.display.set_icon(icono)

#CUADRO TEXTO

input_box = pygame.Rect(50, 50, 200, 128)     # LOGICO

color_activo = VERDE_2
color_inactivo = ROJO
color_actual = color_inactivo
activo = False

fuente = pygame.font.SysFont("Cambria", 60)
text = ""

# Rellana la pantalla con el color definiido
ventana.fill(VIOLETA)

jueguito = True
while jueguito:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jueguito = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(evento.pos):
                activo = not activo
            
            if activo:
                color_actual = color_activo
            else:
                color_actual = color_inactivo
        
        elif evento.type == pygame.KEYDOWN:

            if activo:
                if evento.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                
                elif evento.key == pygame.K_ESCAPE:
                    text = ""
                
                else:
                    text += evento.unicode

        ventana.fill(VIOLETA)
        text_surface = fuente.render(text, True, NEGRO)
        ventana.blit(text_surface, (input_box.x + 5, input_box.y + 5))

    pygame.draw.rect(ventana, color_actual, input_box, 3)      # FISICO

    pygame.display.update()


pygame.quit()