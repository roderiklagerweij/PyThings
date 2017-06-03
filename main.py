import skyline

__author__ = 'Roderik'
import pygame
import pygame.locals

from screen import Screen
from argument_parser import ArgumentParser

screen = pygame.display.set_mode((640, 480))
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

while not game_over:
    if new_instance:
        screen.fill((0, 0, 0))

        top_layout = Screen()
        view_hierarchy = []
        view_hierarchy.append(top_layout)

        # recurse_add_prog(house.get_instance(), top_layout)
        top_layout.add_child(skyline.get_instance())
        # recurse_add_prog(skyline.get_instance(), top_layout)

        for view in view_hierarchy:
            view.measure()

        for view in view_hierarchy:
            view.post_measure(640, 480)

        for view in view_hierarchy:
            view.layout(0, 0, 640, 480)

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
                print (pressed_key)


    pygame.time.delay(100)
    # pygame.time.delay(15000)

