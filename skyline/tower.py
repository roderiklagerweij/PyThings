__author__ = 'Roderik'

from linearlayout import LinearLayout
from triangle import Triangle
from skyline.params import SkylineParams
from skyline import tower_section
from skyline import tower_middlepart

TOWER_ROOF = "tower_roof"
TOWER_SECTION = "tower_section"

def get_instance():

    return LinearLayout("VERTICAL", gravity="center", childs=[

            Triangle(
                fill_width=True,
                height=50,
                color=SkylineParams.wall_color,
                id=TOWER_ROOF,
                rotation=180,
                intensity=SkylineParams.intensity),

            LinearLayout(
                layout_type="VERTICAL",
                debug_id="one level deeper",
                childs=[
                    tower_middlepart.get_instance(),
                    LinearLayout(
                        layout_type="VERTICAL",
                        padding=3,
                        childs=
                        [
                            tower_section.get_instance(
                                x,
                                SkylineParams.get_horizontal_window_count_for_floor(x),
                                SkylineParams.get_vertical_window_count_for_floor(x)) for x in range(0, SkylineParams.section_count)])

                ])

        ])
