__author__ = 'Roderik'

import random


class SkylineParams:

    horizontal_windows = round(random.random()*5) + 3
    floor_count = round(random.random()*10) + 4
    wall_color = (0, 0, 128)
    intensity = random.random() * 0.8