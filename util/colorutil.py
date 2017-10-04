__author__ = 'Roderik'

import random
import colorsys


def vary_color(color, variation):

    return (color[0] + random.randint(0, variation) - (variation/2),
            color[1] + random.randint(0, variation) - (variation/2),
            color[2] + random.randint(0, variation) - (variation/2))


def darken(color, intensity):
    hsv = colorsys.rgb_to_hsv(color[0], color[1], color[2])
    return colorsys.hsv_to_rgb(hsv[0], hsv[1], hsv[2] * intensity)