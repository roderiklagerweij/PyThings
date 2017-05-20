__author__ = 'Roderik'
import pygame
from pygame import Color

class View:

    def __init__(self, width, height, r, g, b, gravity):
        self.offset_x = 0
        self.offset_y = 0
        self.width = width
        self.height = height
        self.color = Color(r, g, b)
        self.gravity = gravity

    def measure(self):
        pass

    def layout(self, offset_x, offset_y, parent_width, parent_height):
        self.offset_x = offset_x
        self.offset_y = offset_y

        if self.gravity == 'bottom':
            self.offset_y = parent_height-self.height

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.offset_x, self.offset_y, self.width, self.height), 0)