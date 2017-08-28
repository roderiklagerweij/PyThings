__author__ = 'Roderik'
import pygame
from pygame import Color
from pygame import Surface
from linearlayout import LinearLayout


class Circle(LinearLayout):

    def __init__(self, radius, *args, **kwargs):
        super().__init__("HORIZONTAL", width=radius*2, height=radius*2, *args, **kwargs)
        self.radius = radius

    def draw(self, screen):
        surface = Surface((self.width, self.height))
        # pygame.draw.polygon(surface, self.color, [(0, 0), (self.width, 0), (self.width/2, self.height)], 0)
        pygame.draw.circle(surface, self.color, [self.radius, self.radius], round(self.radius))
        return surface
        # screen.blit(surface, (self.offset_x, self.offset_y))