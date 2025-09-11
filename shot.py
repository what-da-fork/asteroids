import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 1).rotate(rotation) * PLAYER_SHOOT_SPEED

    # from asteroid.py
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, 2)

    # from asteroid.py
    def update(self, dt):
        self.position += self.velocity * dt