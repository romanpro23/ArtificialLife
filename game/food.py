import random

import pygame

from function.fuction import BLACK
from function.project_config import *


class Food:
    x: int
    y: int

    energy: float
    radius: float

    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)

        self.energy = random.random() * (FOOD_MAX_ENERGY - FOOD_MIN_ENERGY) + FOOD_MIN_ENERGY
        self.radius = FOOD_MIN_RADIUS + (FOOD_MAX_RADIUS - FOOD_MIN_RADIUS) * self.energy / FOOD_MAX_ENERGY

    def draw(self, screen):
        pygame.draw.circle(screen, BLACK, (self.x, self.y), self.radius)
