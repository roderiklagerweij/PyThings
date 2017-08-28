__author__ = 'Roderik'
import pygame
from pygame import Surface
from linearlayout import LinearLayout

class Triangle(LinearLayout):

    def draw(self, screen):
        surface = Surface((self.width, self.height))
        pygame.draw.polygon(surface, self.color, [(0, 0), (self.width, 0), (self.width/2, self.height)], 0)
        new_surface = pygame.transform.rotate(surface, self.rotation)
        return new_surface
