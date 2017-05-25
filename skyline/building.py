__author__ = 'Roderik'

from linearlayout import LinearLayout
from triangle import Triangle
from skyline.params import SkylineParams
from skyline import floor
from skyline import tower_middlepart


def get_instance():
    return [
        LinearLayout("VERTICAL", gravity="center", childs=[

            Triangle(width='fill',
                     height=50,
                     color=SkylineParams.wall_color,
                     rotation=180,
                     intensity=SkylineParams.intensity),

            tower_middlepart.get_instance(),

            LinearLayout("VERTICAL",
                         color=SkylineParams.wall_color,
                         intensity=SkylineParams.intensity,
                         padding=3,
                         childs=[
                             (floor, SkylineParams.floor_count)
                         ])
        ]),
    ]