__author__ = 'Roderik'

import pygame
import pygame.locals

from view.layout import LinearLayout
from template import write_template
import settings
from view.screen import Screen
from exporter import export
import modules_config


pygame.init()

screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))

image_names = []

print ('Generating images')
for module in modules_config.get_modules():
    for i in range(10):
        screen.fill((0, 0, 0))

        top_layout = Screen(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
        view_hierarchy = []
        view_hierarchy.append(top_layout)

        top_layout.add_child(LinearLayout(gravity="center", childs=[module.get_instance()]))

        for view in view_hierarchy:
            view.measure()

        for view in view_hierarchy:
            view.post_measure(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)

        for view in view_hierarchy:
            view.layout(0, 0, settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)

        for view in view_hierarchy:
            view.draw(screen)

        pygame.display.flip()
        new_instance = False

        export_rect = top_layout.get_export_rect()
        image_name = export(screen.subsurface(export_rect), module, i)
        image_names.append(image_name)

print ('Writing template')
write_template.write_template(image_names)