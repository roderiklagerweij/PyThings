__author__ = 'Roderik'
import pygame
# from pygame import Rect, Surface, pygame


class Screen:

    def __init__(self, width, height):
        self.childs = []
        self.width = width
        self.height = height

    def measure(self):
        for child in self.childs:
            child.measure()

    def post_measure(self, parent_width, parent_height):
        for child in self.childs:
            child.post_measure(parent_width, parent_height)

    def apply_gravity(self, offset_x, offset_y, parent_width, parent_height):
        for child in self.childs:
            child.apply_gravity(0, 0, parent_width, parent_height)

    def add_child(self, child):
        self.childs.append(child)

    def draw(self, screen):
        surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA, 32)

        for child in self.childs:
            childsurface = child.draw()
            surface.blit(childsurface, (child.offset_x, child.offset_y))

        screen.blit(surface, (0, 0))

    def get_export_rect(self):
        x0 = max(0, self.childs[0].offset_x)
        y0 = max(0, self.childs[0].offset_y)
        x1 = min(self.width, self.childs[0].width)
        y1 = min(self.height, self.childs[0].height)

        return pygame.Rect(x0, y0, x1, y1)


    # blur test
    def blur_screen(self, surface, amt):
        if amt < 1.0:
            raise ValueError("Arg 'amt' must be greater than 1.0, passed in value is %s"%amt)
        scale = 1.0/float(amt)
        surf_size = surface.get_size()
        scale_size = (int(surf_size[0]*scale), int(surf_size[1]*scale))
        surf = pygame.transform.smoothscale(surface, scale_size)
        surf = pygame.transform.smoothscale(surf, surf_size)
        return surf
