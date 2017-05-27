__author__ = 'Roderik'
import pygame
from pygame import Color
import colorsys


class LinearLayout:

    HORIZONTAL = 1
    VERTICAL = 2

    def __init__(self,
                 layout_type=None,
                 gravity=None,
                 padding=0,
                 padding_left=None,
                 padding_right=None,
                 padding_top=None,
                 padding_bottom=None,
                 margin=0,
                 width=0,
                 height=0,
                 fill_width=False,
                 fill_height=False,
                 rotation=0,
                 color=None,
                 childs=[],
                 debug_id=None,
                 intensity=1):

        if layout_type == "HORIZONTAL":
            self.layout_type = LinearLayout.HORIZONTAL
        elif layout_type == "VERTICAL":
            self.layout_type = LinearLayout.VERTICAL
        else:
            self.layout_type = None

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

        self.debug_id = debug_id
        self.margin = margin

        self.fill_width = fill_width
        self.fill_height = fill_height
        self.width = width
        self.height = height
        self.rotation = rotation

        if color:
            hsv = colorsys.rgb_to_hsv(color[0], color[1], color[2])
            self.color = colorsys.hsv_to_rgb(hsv[0], hsv[1], hsv[2]*intensity)
        else:
            self.color = None

        for child in childs:
            if type(child) is tuple:
                for i in range(child[1]):
                    self.add_child(child[0].get_instance())
            else:
                self.add_child(child)

    def draw(self):
        pass

    def get_width(self):
        pass

    def get_height(self):
        pass

    def measure(self):
        width = 0
        height = 0

        for child in self.childs:
            child.measure()
            if self.layout_type == LinearLayout.HORIZONTAL:
                width += child.width
                if height < child.height:
                    height = child.height
            elif self.layout_type == LinearLayout.VERTICAL:
                height += child.height
                if width < child.width:
                    width = child.width

        width += self.padding_left + self.padding_right
        height += self.padding_top + self.padding_bottom

        # assign to self
        # if provided dimension is more than calculated, keep the provided
        if self.width < width:
            self.width = width
        if self.height < height:
            self.height = height

        # add the margin
        self.width += 2 * self.margin
        self.height += 2 * self.margin

    def post_measure(self, available_fill_width, available_fill_height):
        if self.fill_width:
            self.width = available_fill_width
        if self.fill_height:
            self.height = available_fill_height

        width_weight_sum = 0
        height_weight_sum = 0
        used_width = 0
        used_height = 0
        if self.layout_type == LinearLayout.HORIZONTAL:
            for child in self.childs:
                if child.fill_width:
                    width_weight_sum += 1
                else:
                    used_width += child.width

            width_weight_sum = max(width_weight_sum, 1)

            # if self.debug_id:
            #     print (self.debug_id, 'Post measure:', available_fill_width, self.width, used_width, self.fill_width, float(self.width - used_width) / float(width_weight_sum))

            for child in self.childs:
                child.post_measure(
                    float(self.width - used_width) / float(width_weight_sum),
                    self.height)

        elif self.layout_type == LinearLayout.VERTICAL:
            for child in self.childs:
                if child.fill_height:
                    height_weight_sum += 1
                else:
                    used_height += child.height

            height_weight_sum = max(height_weight_sum, 1)

            # if self.debug_id:
            #     print (self.debug_id, 'Post measure:', available_fill_height, self.height, used_height, self.fill_height, float(self.height - used_height) / float(height_weight_sum))

            for child in self.childs:
                child.post_measure(
                    self.width,
                    float(self.height - used_height) / float(height_weight_sum))

    def layout(self, offset_x, offset_y, available_width, available_height):
        self.offset_x = offset_x
        self.offset_y = offset_y

        if self.gravity == 'top':
            self.offset_y -= (available_height - self.height)
        elif self.gravity == 'right':
            self.offset_x -= (available_width - self.width)
        elif self.gravity == 'center':
            self.offset_x += ((available_width/2) - (self.width / 2))
            self.offset_y += ((available_height/2) - (self.height / 2))

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
            pygame.draw.rect(screen, self.color, (
                self.offset_x+self.margin,
                self.offset_y+self.margin,
                self.width - (self.margin + self.margin),
                self.height - (self.margin + self.margin)
            ), 0)

        for child in self.childs:
            child.draw(screen)