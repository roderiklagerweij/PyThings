__author__ = 'Roderik'

from linearlayout import LinearLayout
from triangle import Triangle
from skyline.params import SkylineParams
from skyline import tower_floor
from skyline import tower_middlepart


def get_instance():
    return [
        LinearLayout("VERTICAL", gravity="center", childs=[

            Triangle(
                fill_width=True,
                height=50,
                color=SkylineParams.wall_color,
                rotation=180,
                intensity=SkylineParams.intensity),

            LinearLayout(
                layout_type="VERTICAL",
                color=SkylineParams.wall_color,
                intensity=SkylineParams.intensity,
                childs=[
                    tower_middlepart.get_instance(),
                    LinearLayout(
                        layout_type="VERTICAL",
                        padding=3,
                        childs=[
                            (tower_floor, SkylineParams.floor_count)
                        ])
                ])

        ]),
        ]