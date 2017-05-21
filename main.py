__author__ = 'Roderik'
import pygame
import pygame.locals
from pygame import Color
from linearlayout import LinearLayout
from view import View
from triangle import Triangle
from screen import Screen
import time
from argument_parser import ArgumentParser
import house

screen = pygame.display.set_mode((640, 480))
game_over = False

view_hierarchy = []
arg_parser = ArgumentParser()

# * all linearlayouts are wrap content now
# * view must take a dedicated space
# gravity?
# layout_weight?
# constraints

def recurse_add(lines, parent):
    leading_spaces = -1
    for idx, line in enumerate(lines):

        if line.strip() == '':
            continue

        if leading_spaces == -1:
            leading_spaces = len(line) - len(line.lstrip())

        if not len(line) - len(line.lstrip()) == leading_spaces:
            continue

        if line.strip().startswith('View'):
            args = arg_parser.parse(line)
            width = args['w']
            height = args['h']
            r = int(args['r'])
            g = int(args['g'])
            b = int(args['b'])
            rotation = 0
            if 'rotation' in args:
                rotation = int(args['rotation'])

            gravity = None
            if 'gravity' in args:
                gravity = args['gravity']
            v = View(width, height, r, g, b, gravity, rotation)
            parent.add_child(v)
        if line.strip().startswith('Triangle'):
            args = arg_parser.parse(line)
            width = args['w']
            height = args['h']
            r = int(args['r'])
            g = int(args['g'])
            b = int(args['b'])
            rotation = 0
            if 'rotation' in args:
                rotation = int(args['rotation'])

            gravity = None
            if 'gravity' in args:
                gravity = args['gravity']
            v = Triangle(width, height, r, g, b, gravity, rotation)
            parent.add_child(v)
        elif line.strip().startswith('LinearLayout'):
            args = arg_parser.parse(line)
            gravity = None
            if 'gravity' in args:
                gravity = args['gravity']
            padding = 0
            if 'padding' in args:
                padding = int(args['padding'])
            ll = LinearLayout(args['orientation'], gravity, padding)

            parent.add_child(ll)
            recurse_add(lines[idx+1:], ll)
        elif line.strip().startswith('end'):
            return

def recurse_add_prog(layout, parent):
    for item in layout:
        if type(item) is list:
            recurse_add_prog(item, parent.childs[-1])
        else:
            parent.add_child(item)

while not game_over:
    screen.fill((0, 0, 0))

    f = open('house.layout', 'r')
    layout = f.read()
    f.close()

    lines = layout.strip().split('\n')

    top_layout = Screen()
    view_hierarchy = []
    view_hierarchy.append(top_layout)

    # recurse_add(lines, top_layout)
    recurse_add_prog(house.get_instance(), top_layout)

    for view in view_hierarchy:
        view.measure()

    for view in view_hierarchy:
        view.post_measure(640, 480)

    for view in view_hierarchy:
        view.layout(0, 0, 640, 480)

    for view in view_hierarchy:
        view.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            game_over = True
        elif event.type == pygame.locals.KEYDOWN:
            pressed_key = event.key
            if pressed_key == 27:
                game_over = True

    pygame.display.flip()
    pygame.time.delay(100)

