from modules.dutch_houses import HouseParams
from modules.dutch_houses.house_params import WindowTopDecoration
from view.layout import LinearLayout

__author__ = 'Roderik'


def get_instance():

    if HouseParams.top_decoration == WindowTopDecoration.top_decoration_none:
        return LinearLayout(width=0, height=0)
    elif HouseParams.top_decoration == WindowTopDecoration.top_decoration_3:
        return LinearLayout(
            layout_type="HORIZONTAL",
            fill_width=True,
            childs=[
                LinearLayout(height=8, color=HouseParams.frame_color, fill_width=True, rotation=10),
                LinearLayout(height=8, fill_width=True),
                LinearLayout(height=8, color=HouseParams.frame_color, fill_width=True),
                LinearLayout(height=8, fill_width=True),
                LinearLayout(height=8, color=HouseParams.frame_color, fill_width=True, rotation=-10),
                ]
        )
    elif HouseParams.top_decoration == WindowTopDecoration.top_decoration_5:
        return LinearLayout(
            layout_type="HORIZONTAL",
            fill_width=True,
            childs=[
                LinearLayout(height=8, color=HouseParams.frame_color, fill_width=True, rotation=20),
                LinearLayout(height=8, fill_width=True),
                LinearLayout(height=8, color=HouseParams.frame_color, fill_width=True, rotation=10),
                LinearLayout(height=8, fill_width=True),
                LinearLayout(height=8, color=HouseParams.frame_color, fill_width=True),
                LinearLayout(height=8, fill_width=True),
                LinearLayout(height=8, color=HouseParams.frame_color, fill_width=True, rotation=-10),
                LinearLayout(height=8, fill_width=True),
                LinearLayout(height=8, color=HouseParams.frame_color, fill_width=True, rotation=-20)
            ]
        )