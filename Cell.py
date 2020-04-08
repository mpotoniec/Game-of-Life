import pygame, random

class Cell:
    def __init__(self, surface, x, y):

        self.alive = False
        self.surface = surface
        self.x = x
        self.y = y
        self.image = pygame.Surface((12,12))
        self.rect = self.image.get_rect()
        self.neighbours = []
        self.alive_neighbours = 0

    def update(self):
        self.rect.topleft = (self.x*12, self.y*12)

    def draw(self):
        if self.alive:
            self.image.fill((0, 0, 0))
        else:
            self.image.fill((0, 0, 0))
            pygame.draw.rect(self.image, (255, 255, 255), (1, 1, 18, 18))
        self.surface.blit(self.image, (self.x*12, self.y*12))