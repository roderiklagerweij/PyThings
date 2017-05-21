__author__ = 'Roderik'
import pygame
from pygame import Color

class LinearLayout:

    HORIZONTAL = 1
    VERTICAL = 2

    def __init__(self, layout_type,
                 gravity=None,
                 padding=0,
                 color=None):

        if layout_type == "HORIZONTAL":
            self.layout_type = LinearLayout.HORIZONTAL
        elif layout_type == "VERTICAL":
            self.layout_type = LinearLayout.VERTICAL
        self.childs = []
        self.offset_x = 0
        self.offset_y = 0
        self.gravity = gravity
        self.padding = padding
        self.color = color

    def draw(self):
        pass

    def get_width(self):
        pass

    def get_height(self):
        pass

    def measure(self):
        self.width = 2*self.padding
        self.height = 2*self.padding

        for child in self.childs:
            child.measure()
            if self.layout_type == LinearLayout.HORIZONTAL:
                self.width += child.width
                if self.height < child.height:
                    self.height = child.height
            elif self.layout_type == LinearLayout.VERTICAL:
                self.height += child.height
                if self.width < child.width:
                    self.width = child.width

    def post_measure(self, parent_width, parent_height):
        for child in self.childs:
            child.post_measure(self.width, self.height)

    def layout(self, offset_x, offset_y, parent_width, parent_height):
        self.offset_x = offset_x
        self.offset_y = offset_y

        offset_x += self.padding
        offset_y += self.padding

        if self.gravity == 'top':
            offset_y -= (parent_height - self.height)
        elif self.gravity == 'right':
            offset_x -= (parent_width - self.width)

        for child in self.childs:
            child.layout(offset_x, offset_y, self.width, self.height)
            if self.layout_type == LinearLayout.HORIZONTAL:
                offset_x += child.width
            elif self.layout_type == LinearLayout.VERTICAL:
                offset_y += child.height

    def add_child(self, child):
        self.childs.append(child)

    def draw(self, screen):
        if self.color:
            pygame.draw.rect(screen, self.color, (self.offset_x, self.offset_y, self.width, self.height), 0)
        for child in self.childs:
            child.draw(screen)