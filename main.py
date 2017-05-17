__author__ = 'Roderik'
import pygame
import pygame.locals
from pygame import Color
from linearlayout import LinearLayout
from view import View
from screen import Screen
import time

screen = pygame.display.set_mode((640, 480))
game_over = False

view_hierarchy = []

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
            args = line.strip().split(' ')
            width = int(args[1])
            height = int(args[2])
            r = int(args[3])
            g = int(args[4])
            b = int(args[5])
            v = View(width, height, r, g, b)
            parent.add_child(v)
        elif line.strip().startswith('LinearLayout'):
            args = line.strip().split(' ')
            ll = LinearLayout(args[1])
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
        view.layout()

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

