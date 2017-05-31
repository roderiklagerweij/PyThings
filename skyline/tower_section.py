from skyline.params import SkylineParams

__author__ = 'Roderik'

from linearlayout import LinearLayout
import random


def get_instance(windows_horizontal, windows_vertical):
    return LinearLayout(
        layout_type="VERTICAL",
        color=SkylineParams.wall_color,
        intensity=SkylineParams.intensity,
        gravity="center_horizontal",
        childs=[get_floor(windows_horizontal) for x in range(windows_vertical)])

def get_floor(windows_horizontal):
    return LinearLayout(layout_type="HORIZONTAL", childs=[get_tower_window() for x in range(windows_horizontal)])


def get_tower_window():
    return LinearLayout(width=6, height=6, color=(255, 255, 0), margin=3, intensity=random.random())