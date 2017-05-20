__author__ = 'Roderik'
import pygame

def rotate_center(surface, angle):
    """rotate a Surface, maintaining position."""

    loc = surface.get_rect().center
    rot_sprite = pygame.transform.rotate(surface, angle)
    rot_sprite.get_rect().center = loc
    return rot_sprite
