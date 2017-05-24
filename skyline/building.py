__author__ = 'Roderik'

from linearlayout import LinearLayout
from triangle import Triangle
from skyline.params import SkylineParams
from skyline import floor


def get_instance():
    return [
        LinearLayout("VERTICAL", gravity="center"),
        [
            Triangle(width='fill',
                     height=50,
                     color=SkylineParams.wall_color,
                     rotation=180,
                     intensity=SkylineParams.intensity),

            LinearLayout("VERTICAL",
                         color=(0, 0, 128),
                         intensity=0.3,
                         padding=3,
                         repeat_include=(floor, SkylineParams.floor_count))
        ],


    ]