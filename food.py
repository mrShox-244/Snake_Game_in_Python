import pygame
import random

class Food:
    def __init__(self, screen_width, screen_height, size):
        self.size = size
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = random.randint(0, screen_width - size)
        self.y = random.randint(0, screen_height - size)

    def draw(self, screen):
        pygame.draw.rect(screen, "red", (self.x, self.y, self.size, self.size))

    def respawn(self):
        self.x = random.randint(0, self.screen_width - self.size)
        self.y = random.randint(0, self.screen_height - self.size)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)



