__author__ = 'Roderik'
import pygame
from pygame import Color
from pygame import Surface
from view import View


class Circle(View):

    def __init__(self, radius, *args, **kwargs):
        super().__init__(radius*2, radius*2, *args, **kwargs)
        self.radius = radius

    def draw(self, screen):
        surface = Surface((self.width, self.height))
        # pygame.draw.polygon(surface, self.color, [(0, 0), (self.width, 0), (self.width/2, self.height)], 0)
        pygame.draw.circle(surface, self.color, [self.radius, self.radius], round(self.radius))
        new_surface = pygame.transform.rotate(surface, self.rotation)
        screen.blit(new_surface, (self.offset_x, self.offset_y))