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
        color=SkylineParams.wall_color,
        intensity=SkylineParams.intensity,
        padding=3,
        gravity="center_horizontal",
        childs=
            [LinearLayout(
                layout_type="VERTICAL",
                fill_width=True,
                color=SkylineParams.wall_color,
                intensity=SkylineParams.intensity,
                gravity="center_horizontal",
                padding=5,
                visible=SkylineParams.has_section_divider,
                childs=
                [LinearLayout(
                    fill_width=True,
                    height=5,
                    color=(255, 255, 0))])
            ] + [get_floor(windows_horizontal) for x in range(windows_vertical)])



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