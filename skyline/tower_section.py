from skyline.params import SkylineParams

__author__ = 'Roderik'

from linearlayout import LinearLayout
import random

TOP_TOWER_SECTION = "top_tower_section"

def get_instance(section_index, windows_horizontal, windows_vertical):
    id = None
    if section_index == 0:
        id = TOP_TOWER_SECTION

    return LinearLayout(
        layout_type="VERTICAL",
        id=id,
        gravity="center_horizontal",
        childs=[get_floor(windows_horizontal) for x in range(windows_vertical)])


def get_floor(windows_horizontal):
    return LinearLayout(
        layout_type="HORIZONTAL",
        childs=[get_tower_window() for x in range(windows_horizontal)])


def get_tower_window():
    return LinearLayout(
        padding=5,
        childs=[
            LinearLayout(width=10, height=10, color=(255, 255, 0), intensity=random.random())
        ])