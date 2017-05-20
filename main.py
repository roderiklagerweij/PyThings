__author__ = 'Roderik'
import pygame
import pygame.locals
from pygame import Color
from linearlayout import LinearLayout
from view import View
from screen import Screen
import time
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
            width = int(args['w'])
            height = int(args['h'])
            r = int(args['r'])
            g = int(args['g'])
            b = int(args['b'])
            gravity = None
            if 'gravity' in args:
                gravity = args['gravity']
            v = View(width, height, r, g, b, gravity)
            parent.add_child(v)
        elif line.strip().startswith('LinearLayout'):
            args = arg_parser.parse(line)
            gravity = None
            if 'gravity' in args:
                gravity = args['gravity']
            ll = LinearLayout(args['orientation'], gravity)

            parent.add_child(ll)
            recurse_add(lines[idx+1:], ll)
        elif line.strip().startswith('end'):
            return


while not game_over:
    screen.fill((0, 0, 0))

    f = open('test.layout', 'r')
    layout = f.read()
    f.close()

    lines = layout.strip().split('\n')

    top_layout = Screen()
    view_hierarchy = []
    view_hierarchy.append(top_layout)

    recurse_add(lines, top_layout)

    for view in view_hierarchy:
        view.measure()

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

