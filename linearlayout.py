__author__ = 'Roderik'
import pygame
from pygame import Color
import colorsys

class LinearLayout:

    HORIZONTAL = 1
    VERTICAL = 2

    def __init__(self, layout_type,
                 gravity=None,
                 padding=0,
                 padding_left=None,
                 padding_right=None,
                 padding_top=None,
                 padding_bottom=None,
                 color=None,
                 repeat_include=None,
                 intensity=1):

        if layout_type == "HORIZONTAL":
            self.layout_type = LinearLayout.HORIZONTAL
        elif layout_type == "VERTICAL":
            self.layout_type = LinearLayout.VERTICAL
        self.childs = []
        self.offset_x = 0
        self.offset_y = 0
        self.gravity = gravity
        self.padding_left = padding
        self.padding_right = padding
        self.padding_top = padding
        self.padding_bottom = padding
        if padding_left:
            self.padding_left = padding_left
        if padding_right:
            self.padding_right = padding_right
        if padding_top:
            self.padding_top = padding_top
        if padding_bottom:
            self.padding_bottom = padding_bottom

        if color:
            hsv = colorsys.rgb_to_hsv(color[0], color[1], color[2])
            self.color = colorsys.hsv_to_rgb(hsv[0], hsv[1], hsv[2]*intensity)
        else:
            self.color = None

        if repeat_include:
            for i in range(repeat_include[1]):
                self.add_child(repeat_include[0].get_instance())

    def draw(self):
        pass

    def get_width(self):
        pass

    def get_height(self):
        pass

    def measure(self):
        self.width = 0
        self.height = 0

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

        self.width += self.padding_left + self.padding_right
        self.height += self.padding_top + self.padding_bottom

    def post_measure(self, parent_width, parent_height):
        for child in self.childs:
            child.post_measure(self.width, self.height)

    def layout(self, offset_x, offset_y, parent_width, parent_height):
        self.offset_x = offset_x
        self.offset_y = offset_y

        if self.gravity == 'top':
            self.offset_y -= (parent_height - self.height)
        elif self.gravity == 'right':
            self.offset_x -= (parent_width - self.width)
        elif self.gravity == 'center':
            self.offset_x = (parent_width/2) - self.width / 2
            self.offset_y = (parent_height/2) - self.height / 2

        draw_x = self.offset_x + self.padding_left
        draw_y = self.offset_y + self.padding_top

        for child in self.childs:
            child.layout(draw_x, draw_y, self.width-(self.padding_left+self.padding_right), self.height-(self.padding_top+self.padding_bottom))
            if self.layout_type == LinearLayout.HORIZONTAL:
                draw_x += child.width
            elif self.layout_type == LinearLayout.VERTICAL:
                draw_y += child.height

    def add_child(self, child):
        self.childs.append(child)

    def draw(self, screen):
        if self.color:
            pygame.draw.rect(screen, self.color, (self.offset_x, self.offset_y, self.width, self.height), 0)

        for child in self.childs:
            child.draw(screen)