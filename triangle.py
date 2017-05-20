__author__ = 'Roderik'
import pygame
from pygame import Color
from pygame import Surface
from view import View

class Triangle(View):

    def draw(self, screen):
        surface = Surface((self.width, self.height))

        # pygame.draw.polygon(surface, self.color, [[self.offset_x, self.offset_y],
        #                                          [self.offset_x + self.width, self.offset_y],
        #                                          [self.offset_x + (self.width/2), self.offset_y + (self.height/2)]], 0)
        pygame.draw.polygon(surface, self.color, [(0, 0), (self.width, 0), (self.width/2, self.height)], 0)
        new_surface = pygame.transform.rotate(surface, 90)
        # new_surface = util.rotate_center(surface, 180)
        screen.blit(new_surface, (self.offset_x, self.offset_y))