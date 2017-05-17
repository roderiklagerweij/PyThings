__author__ = 'Roderik'
import pygame
from pygame import Color

class View:

    def __init__(self, width, height, r, g, b):
        self.offset_x = 0
        self.offset_y = 0
        self.width = width
        self.height = height
        self.color = Color(r, g, b)

    def measure(self):
        pass

    def layout(self):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.offset_x, self.offset_y, self.width, self.height), 0)