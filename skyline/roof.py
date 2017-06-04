from linearlayout import LinearLayout
from skyline.params import SkylineParams
from triangle import Triangle

__author__ = 'Roderik'

import random

TOWER_ROOF = "tower_roof"

def get_instance():
    selection = random.randint(0, 3)

    if selection == 0:
        return LinearLayout()
    elif selection == 1: # roof with single pole
        return LinearLayout(
            id=TOWER_ROOF,
            layout_type="VERTICAL",
            gravity="center_horizontal",
            childs=[

                LinearLayout(
                    width=3,
                    height=10,
                    color=SkylineParams.wall_color,
                    intensity=SkylineParams.intensity,
                    gravity="center_horizontal",
                    visible=random.choice([True, False])
                ),

                Triangle(
                    height=50,
                    fill_width=True,
                    color=SkylineParams.wall_color,
                    gravity="center_horizontal",
                    rotation=180,
                    intensity=SkylineParams.intensity),
                ])
    elif selection == 2: # roof with 2 poles
        return LinearLayout(
            id=TOWER_ROOF,
            layout_type="VERTICAL",
            gravity="center_horizontal",
            padding_left=10,
            padding_right=10,
            childs=[
                LinearLayout( # poles
                    layout_type="HORIZONTAL",
                    fill_width=True,
                    childs=[
                        LinearLayout(fill_width=True),
                        LinearLayout(height=25, width=5, color=SkylineParams.wall_color, intensity=SkylineParams.intensity),
                        LinearLayout(fill_width=True),
                        LinearLayout(height=25, width=5, color=SkylineParams.wall_color, intensity=SkylineParams.intensity),
                        LinearLayout(fill_width=True)
                    ]
                ),
                LinearLayout(
                    color=SkylineParams.wall_color,
                    intensity=SkylineParams.intensity,
                    fill_width=True,
                    height=15
                )
            ]
        )
    elif selection == 3:
        return LinearLayout(
                    width=3,
                    height=10,
                    color=SkylineParams.wall_color,
                    intensity=SkylineParams.intensity,
                    gravity="center_horizontal"
                )

