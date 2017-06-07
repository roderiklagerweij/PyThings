__author__ = 'Roderik'

import pygame

def export(image, module, export_counter):
    name = '_'.join([module.get_name(), 'v' + module.get_version(), str(export_counter)])
    pygame.image.save(image, './images/' + name + '.png')