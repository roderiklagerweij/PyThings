from view.layout import LinearLayout

__author__ = 'Roderik'
import pygame
import pygame.locals

from view.screen import Screen
from util.argument_parser import ArgumentParser
import settings
import modules_config

pygame.init()

screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
game_over = False

view_hierarchy = []
arg_parser = ArgumentParser()


new_instance = True

module = modules_config.get_active_module()

while not game_over:
    if new_instance:
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
            view.apply_gravity(0, 0, settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)

        for view in view_hierarchy:
            view.draw(screen)

        pygame.display.flip()
        new_instance = False

    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            game_over = True
        elif event.type == pygame.locals.KEYDOWN:
            pressed_key = event.key
            if pressed_key == 27:
                game_over = True
            else:
                new_instance = True

    # pygame.time.delay(100)
