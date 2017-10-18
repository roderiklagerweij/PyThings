from modules.dutch_houses import HouseParams
from modules.dutch_houses.house_params import WindowTopDecoration
from view.layout import LinearLayout

__author__ = 'Roderik'

WINDOW_TOP_DECORATION = "window_top_decoration"

def get_instance():

    if HouseParams.window_top_decoration == WindowTopDecoration.top_decoration_none:
        return LinearLayout(width=0, height=0)
    elif HouseParams.window_top_decoration == WindowTopDecoration.top_decoration_3:
        return LinearLayout(
            layout_type="HORIZONTAL",
            id=WINDOW_TOP_DECORATION,
            fill_width=True,
            childs=[
                LinearLayout(height=8, color=HouseParams.frame_color, fill_width=True, rotation=0),
                LinearLayout(height=8, fill_width=True),
                LinearLayout(height=8, color=HouseParams.frame_color, fill_width=True),
                LinearLayout(height=8, fill_width=True),
                LinearLayout(height=8, color=HouseParams.frame_color, fill_width=True, rotation=0),
                ]
        )
    elif HouseParams.window_top_decoration == WindowTopDecoration.top_decoration_5:
        return LinearLayout(
            layout_type="HORIZONTAL",
            debug_id='top decoration',
            id=WINDOW_TOP_DECORATION,
            fill_width=True,
            childs=[
                LinearLayout(height=8, color=HouseParams.frame_color, fill_width=True, rotation=0),
                LinearLayout(height=8, fill_width=True),
                LinearLayout(height=8, color=HouseParams.frame_color, fill_width=True, rotation=0),
                LinearLayout(height=8, fill_width=True),
                LinearLayout(height=8, color=HouseParams.frame_color, fill_width=True),
                LinearLayout(height=8, fill_width=True),
                LinearLayout(height=8, color=HouseParams.frame_color, fill_width=True, rotation=0),
                LinearLayout(height=8, fill_width=True),
                LinearLayout(height=8, color=HouseParams.frame_color, fill_width=True, rotation=0)
            ]
        )