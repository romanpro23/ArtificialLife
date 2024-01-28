import pygame
import sys
from function.project_config import *
from game.food import Food

pygame.init()

# Включення вертикальної синхронізації (V-Sync)
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption(CAPTION)

# Set up colors
white = (255, 255, 255)

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(white)

    food = Food()
    food.draw(screen)

    # Update the display
    pygame.display.flip()

    # Add a delay to control the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
