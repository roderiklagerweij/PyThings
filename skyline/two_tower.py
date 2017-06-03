__author__ = 'Roderik'

from skyline import tower
from linearlayout import LinearLayout

def get_instance():
    return LinearLayout(
        layout_type="HORIZONTAL",
        debug_id="two_tower",
        # gravity="center",
        childs=[
            tower.get_instance(),
            LinearLayout(
                debug_id="middle_separator",
                gravity="center_vertical",
                width=15,
                height=3,
                color=(255, 0, 0)
            ),
            tower.get_instance()
        ]
    )
