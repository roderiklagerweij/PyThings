__author__ = 'Roderik'
import pygame
import math

class VerticalStripesDrawer:

    def __init__(self, width, space_between, color):
        self.width = width
        self.space_between = space_between
        self.color = color


    def draw(self, surface, offset_x, offset_y, width, height):
        for x in range(math.ceil(width / self.space_between)):
            pygame.draw.line(surface, self.color,
                             (offset_x+(x*self.space_between), offset_y),
                             (offset_x+(x*self.space_between), offset_y+height),
                             self.width)

