__author__ = 'Roderik'

from modules.skyline import SkylineParams
from modules.skyline import tower
from linearlayout import LinearLayout


def get_instance():
    return LinearLayout(
        layout_type="HORIZONTAL",
        childs=[
            tower.get_instance(),
            LinearLayout(  # tower separator
                gravity="bottom",
                width=60,
                height=40,
                color=SkylineParams.wall_color,
                intensity=SkylineParams.intensity
            ),
            tower.get_instance()
        ]
    )
