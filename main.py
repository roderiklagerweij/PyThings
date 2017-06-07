from linearlayout import LinearLayout
import skyline
import asian_neon

__author__ = 'Roderik'
import pygame
import pygame.locals

from screen import Screen
from argument_parser import ArgumentParser
from exporter import export

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_over = False

view_hierarchy = []
arg_parser = ArgumentParser()

# * all linearlayouts are wrap content now
# * view must take a dedicated space
# gravity?
# layout_weight?
# constraints

def recurse_add_prog(layout, parent):
    for item in layout:
        parent.add_child(item)
        # if type(item) is list:
        #     recurse_add_prog(item, parent.childs[-1])
        # else:
        #     parent.add_child(item)

new_instance = True

export_mode = True
export_counter = 0

module = asian_neon

while not game_over:
    if new_instance:
        screen.fill((0, 0, 0))

        top_layout = Screen()
        view_hierarchy = []
        view_hierarchy.append(top_layout)

        top_layout.add_child(LinearLayout(gravity="center", childs=[module.get_instance()]))

        for view in view_hierarchy:
            view.measure()

        for view in view_hierarchy:
            view.post_measure(SCREEN_WIDTH, SCREEN_HEIGHT)

        for view in view_hierarchy:
            view.layout(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

        for view in view_hierarchy:
            view.draw(screen)
            
        pygame.display.flip()
        new_instance = False

        if export_mode:
            export_rect = top_layout.get_export_rect()
            export(screen.subsurface(export_rect), module, export_counter)
            export_counter += 1
            new_instance = True
            if export_counter == 50:
                game_over = True

    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            game_over = True
        elif event.type == pygame.locals.KEYDOWN:
            pressed_key = event.key
            if pressed_key == 27:
                game_over = True
            else:
                new_instance = True
                print (pressed_key)

    pygame.time.delay(100)
