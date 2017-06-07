__author__ = 'Roderik'
import pygame
import math

class HorizontalStripesDrawer:

    def __init__(self, line_height, space_between, color):
        self.line_height = line_height
        self.space_between = space_between
        self.color = color


    def draw(self, surface, offset_x, offset_y, width, height):
        for y in range(math.ceil(height / self.space_between)):
            pygame.draw.line(surface, self.color,
                             (offset_x, (offset_y+(y*self.space_between))),
                             (offset_x+width, (offset_y+(y*self.space_between))),
                             self.line_height)

