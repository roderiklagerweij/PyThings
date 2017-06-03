__author__ = 'Roderik'

from linearlayout import LinearLayout
from triangle import Triangle
from skyline.params import SkylineParams
from skyline import tower_section
from skyline import tower_middlepart
from skyline import roof
import random

TOWER_SECTION = "tower_section"

def get_instance():

    return LinearLayout("VERTICAL", debug_id="tower", gravity="center", childs=[

        roof.get_instance(),

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
