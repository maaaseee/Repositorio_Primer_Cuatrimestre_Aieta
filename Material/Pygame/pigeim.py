import pygame

# Inicializar Pygame
pygame.init()

# Configurar la ventana
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Dibujar Círculo")

# Definir la figura
figura = {
    "color": (255, 0, 0),         # Rojo en formato RGB
    "posicion": (400, 300),       # Centro de la ventana
    "dimensiones": [50]           # Radio del círculo
}

# Dibujar el círculo
pygame.draw.circle(ventana, figura["color"], figura["posicion"], figura["dimensiones"][0])

# Actualizar la pantalla
pygame.display.flip()

# Mantener la ventana abierta
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Cerrar Pygame
pygame.quit()