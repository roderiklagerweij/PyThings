__author__ = 'Roderik'
import pygame
from pygame import Color

class View:

    def __init__(self, width, height,
                 color=None,
                 gravity=None,
                 rotation=0,
                 padding=0):
        self.offset_x = 0
        self.offset_y = 0
        self.fill_width = False
        self.fill_height = False
        try:
            self.width = int(width)
        except:
            self.width = 0
            if width == 'fill':
                self.fill_width = True
        try:
            self.height = int(height)
        except:
            self.height = 0
            if height == 'fill':
                self.fill_height = True

        self.color = color
        self.gravity = gravity
        self.rotation = rotation
        self.padding = padding

    def measure(self):
        # not need to measure
        pass

    def post_measure(self, parent_width, parent_height):
        if self.fill_width:
            self.width = parent_width
        if self.fill_height:
            self.height = parent_height

    def layout(self, offset_x, offset_y, parent_width, parent_height):
        self.offset_x = offset_x
        self.offset_y = offset_y

        if self.gravity == 'bottom':
            self.offset_y = self.offset_y + (parent_height-self.height)
        if self.gravity == 'right':
            self.offset_x = self.offset_x + (parent_width-self.width)
        if self.gravity == 'center_vertical':
            self.offset_y = self.offset_y + ((parent_height/2)-(self.height/2))

    def draw(self, screen):
        if self.color:
            pygame.draw.rect(screen, self.color, (
                self.offset_x+self.padding,
                self.offset_y+self.padding,
                self.width - (2*self.padding),
                self.height - (2*self.padding)), 0)