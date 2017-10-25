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
            id=WINDOW_SIDE_HATCH,
            padding=4,
            color=(37, 37, 37),
            gravity="bottom",
            childs=[
                LinearLayout(
                    layout_type="VERTICAL",
                    fill_height=True,
                    color=HouseParams.classic_window_side_decoration_background_color,
                    childs=[
                        Triangle(fill_height=True, width=10, rotation=180, color=HouseParams.classic_window_side_decoration_triangle_color),
                        Triangle(fill_height=True, width=10, color=HouseParams.classic_window_side_decoration_triangle_color)
                    ]
                )
            ]
        )