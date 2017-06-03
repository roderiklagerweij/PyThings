__author__ = 'Roderik'

from linearlayout import LinearLayout
from triangle import Triangle
from skyline.params import SkylineParams
from skyline import tower_section
from skyline import tower_middlepart
import random

TOWER_ROOF = "tower_roof"
TOWER_SECTION = "tower_section"

def get_instance():

    return LinearLayout("VERTICAL", gravity="center", childs=[

        LinearLayout(
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
                ]),

        LinearLayout(
            layout_type="VERTICAL",
            childs=[
                tower_middlepart.get_instance(),
                LinearLayout(
                    layout_type="VERTICAL",
                    childs=
                    [
                        tower_section.get_instance(
                            x,
                            SkylineParams.get_horizontal_window_count_for_floor(x),
                            SkylineParams.get_vertical_window_count_for_floor(x)) for x in range(0, SkylineParams.section_count)])

            ])

    ])
