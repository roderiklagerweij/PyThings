__author__ = 'Roderik'
import pygame
from pygame import Color
import colorsys
from math import *


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
                 width=0,
                 height=0,
                 fill_width=False,
                 fill_height=False,
                 rotation=0,
                 color=None,
                 childs=[],
                 id=None,
                 debug_id=None,
                 intensity=1,
                 predrawer=None,
                 postdrawer=None,
                 visible=True):
        self.id = id

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

        self.fill_width = fill_width
        self.fill_height = fill_height
        self.width = width
        self.height = height
        self.width_before_rotation = 0
        self.height_before_rotation = 0
        self.rotation = rotation
        self.predrawer = predrawer
        self.postdrawer = postdrawer

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

        self.visible = visible

        # validation
        if layout_type is None and len(self.childs) > 1:
            raise ValueError("Layout type cannot be none when there is more than one child!")

        if self.width > 0:
            if self.padding_left > 0 or self.padding_right > 0:
                raise ValueError("Setting both padding and specific width is weird")
        if self.height > 0:
            if self.padding_top > 0 or self.padding_bottom > 0:
                raise ValueError("Setting both padding and specific height is weird")

        if not self.rotation == 0:
            if self.padding_bottom > 0 or self.padding_left > 0 or self.padding_right > 0 or self.padding_top > 0:
                raise ValueError("Setting rotation and padding is weird")

    # calculate own width and height
    def measure(self):
        if not self.visible:
            return

        measured_childs_width = 0
        measured_childs_height = 0

        for child in self.childs:
            child.measure()
            if self.layout_type == LinearLayout.HORIZONTAL:
                measured_childs_width += child.width
                if measured_childs_height < child.height:
                    measured_childs_height = child.height
            elif self.layout_type == LinearLayout.VERTICAL:
                measured_childs_height += child.height
                if measured_childs_width < child.width:
                    measured_childs_width = child.width
            else:  # should only be one child
                measured_childs_width = child.width
                measured_childs_height = child.height


        # add padding to childs measured and summed dimensions
        computed_width = measured_childs_width + self.padding_left + self.padding_right
        computed_height = measured_childs_height + self.padding_top + self.padding_bottom

        # finally, set the computed width and height, if provided dimension bigger then computed take those
        self.width_before_rotation = max(self.width, computed_width)
        self.height_before_rotation = max(self.height, computed_height)

        # adjust width/height to rotation
        topLeft = self.rotatePoint(self.rotation, (0, self.height_before_rotation), (0, 0))
        topRight = self.rotatePoint(self.rotation, (self.width_before_rotation, self.height_before_rotation), (0, 0))
        bottomLeft = self.rotatePoint(self.rotation, (0, 0), (0, 0))
        bottomRight = self.rotatePoint(self.rotation, (self.width_before_rotation, 0), (0, 0))
        mostLeft = min(topLeft[0], topRight[0], bottomLeft[0], bottomRight[0])
        mostRight = max(topLeft[0], topRight[0], bottomLeft[0], bottomRight[0])
        mostBottom = min(topLeft[1], topRight[1], bottomLeft[1], bottomRight[1])
        mostTop = max(topLeft[1], topRight[1], bottomLeft[1], bottomRight[1])

        self.width = abs(mostRight - mostLeft)
        self.height = abs(mostTop - mostBottom)

    #
    def post_measure(self, available_fill_width, available_fill_height):
        if not self.visible:
            return

        if self.fill_width:
            self.width = available_fill_width
            self.width_before_rotation = available_fill_width

        if self.fill_height:
            self.height = available_fill_height
            self.height_before_rotation = available_fill_height

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

            for child in self.childs:
                child.post_measure(
                    float((self.width - (used_width+self.padding_left+self.padding_right)) / float(width_weight_sum)),
                    self.height - (self.padding_top+self.padding_bottom))

        elif self.layout_type == LinearLayout.VERTICAL:
            for child in self.childs:
                if child.fill_height:
                    height_weight_sum += 1
                else:
                    used_height += child.height

            height_weight_sum = max(height_weight_sum, 1)

            for child in self.childs:
                child.post_measure(
                    self.width-(self.padding_left+self.padding_right),
                    float((self.height - (used_height+self.padding_bottom+self.padding_top)) / float(height_weight_sum)))

        else:  # no orientation supplied
            if len(self.childs) > 1:
                raise ValueError("Having more than one child does not make sense when not having an orientation!!")

            for child in self.childs:
                child.post_measure(self.width-(self.padding_left + self.padding_right), self.height-(self.padding_bottom+self.padding_top))

    def apply_gravity(self, offset_x, offset_y, available_width, available_height):
        if not self.visible:
            return

        self.offset_x = offset_x
        self.offset_y = offset_y

        if self.gravity == 'top':
            self.offset_y -= (available_height - self.height)
        elif self.gravity == 'right':
            self.offset_x -= (available_width - self.width)
        elif self.gravity == 'bottom':
            self.offset_y += (available_height - self.height)
        elif self.gravity == 'center_horizontal':
            self.offset_x += ((available_width/2) - (self.width / 2))
        elif self.gravity == 'center_vertical':
            self.offset_y += ((available_height/2) - (self.height/ 2))
        elif self.gravity == 'center':
            self.offset_x += ((available_width/2) - (self.width/ 2))
            self.offset_y += ((available_height/2) - (self.height / 2))

        draw_x = self.padding_left
        draw_y = self.padding_top

        for child in self.childs:
            child.apply_gravity(draw_x, draw_y, self.width-(self.padding_left+self.padding_right), self.height-(self.padding_top+self.padding_bottom))

            if self.layout_type == LinearLayout.HORIZONTAL:
                draw_x += child.width
            elif self.layout_type == LinearLayout.VERTICAL:
                draw_y += child.height

    def add_child(self, child):
        self.childs.append(child)

    def draw(self):
        surface = pygame.Surface((self.width_before_rotation, self.height_before_rotation), pygame.SRCALPHA, 32)

        if not self.visible:
            surface

        if self.color:
            pygame.draw.rect(surface, self.color, (
                0,
                0,
                self.width,
                self.height
            ), 0)

        if self.predrawer:
            self.predrawer.draw(surface, self.offset_x, self.offset_y, self.width, self.height)

        for child in self.childs:
            childsurface = child.draw()
            surface.blit(childsurface, (child.offset_x, child.offset_y))

        if self.postdrawer:
            self.postdrawer.draw(surface, self.offset_x, self.offset_y, self.width, self.height)

        if self.rotation is not 0:
            surface = pygame.transform.rotate(surface, self.rotation)

        return surface

    def rotatePoint(self, angle, point, origin):
        sinT = sin(radians(angle))
        cosT = cos(radians(angle))
        return (origin[0] + (cosT * (point[0] - origin[0]) - sinT * (point[1] - origin[1])),
                      origin[1] + (sinT * (point[0] - origin[0]) + cosT * (point[1] - origin[1])))
