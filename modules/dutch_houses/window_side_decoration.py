from modules.dutch_houses.house_params import WindowSideDecoration, HouseParams
from view.layout import LinearLayout
from view.triangle import Triangle

__author__ = 'Roderik'

WINDOW_SIDE_HATCH = "window_side_hatch"

def get_instance():

    if HouseParams.window_side_decoration == WindowSideDecoration.side_decoration_none:
        return LinearLayout(width=0, height=0)
    elif HouseParams.window_side_decoration == WindowSideDecoration.side_decoration_hatch_regular or True:
        return LinearLayout(
            layout_type="VERTICAL",
            id=WINDOW_SIDE_HATCH,
            padding=4,
            color=(255, 0, 0),
            gravity="bottom",
            childs=[
                Triangle(fill_height=True, width=20, color=(0, 255, 0), rotation=180),
                Triangle(fill_height=True, width=20, color=(0, 255, 0))
            ]

        )