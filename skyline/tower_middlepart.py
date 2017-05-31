__author__ = 'Roderik'

import random
from circle import Circle
from linearlayout import LinearLayout
from skyline.params import SkylineParams

TOWER_MIDDLE_PART = "tower_middle_part"

def get_instance():
    selection = random.randint(0, 2)

    if selection == 0:
        return LinearLayout(
            layout_type="HORIZONTAL",
            color=SkylineParams.wall_color,
            id=TOWER_MIDDLE_PART,
            intensity=SkylineParams.intensity,
            gravity="center_horizontal",
            padding=5,
            childs=[
                Circle(5, color=(255, 255, 0), gravity="center")
            ])
    elif selection == 1:
        return LinearLayout(
            id=TOWER_MIDDLE_PART,
            gravity="center_horizontal",
            height=5,
            color=(255, 255, 0),
            margin=5
        )
    elif selection == 2:
        return LinearLayout(
            layout_type="HORIZONTAL",
            id=TOWER_MIDDLE_PART,
            gravity="center_horizontal",
            color=SkylineParams.wall_color,
            intensity=SkylineParams.intensity,
            childs=[
                LinearLayout(fill_width=True),
                LinearLayout(width=2, height=10, color=(255, 255, 0), margin=2),
                LinearLayout(width=2, height=10, color=(255, 255, 0), margin=2),
                LinearLayout(width=2, height=10, color=(255, 255, 0), margin=2),
                LinearLayout(fill_width=True),
                LinearLayout(width=2, height=10, color=(255, 255, 0), margin=2),
                LinearLayout(width=2, height=10, color=(255, 255, 0), margin=2),
                LinearLayout(width=2, height=10, color=(255, 255, 0), margin=2),
                LinearLayout(fill_width=True)
            ]
        )