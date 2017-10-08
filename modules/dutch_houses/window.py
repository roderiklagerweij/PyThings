from modules.dutch_houses import HouseParams
from modules.dutch_houses.house_params import WindowLayout
from view.layout import LinearLayout

__author__ = 'Roderik'


def get_instance():

    if HouseParams.window_layout == WindowLayout.window_layout_3_3_3:
        return get_3_3_window()
    elif HouseParams.window_layout == WindowLayout.window_layout_1_2:
        return get_1_2_window()
    elif HouseParams.window_layout == WindowLayout.window_layout_2_2:
        return get_2_2_window()
    elif HouseParams.window_layout == WindowLayout.window_layout_2:
        return get_2_window()


def get_3_3_window():
    return LinearLayout(
        layout_type="VERTICAL", color=HouseParams.frame_color, padding=4, childs=[
            LinearLayout(
                layout_type="HORIZONTAL",
                childs=[
                    LinearLayout(width=8, height=14, color=HouseParams.window_color),
                    LinearLayout(width=2, height=10, color=HouseParams.frame_color),
                    LinearLayout(width=8, height=14, color=HouseParams.window_color),
                    LinearLayout(width=2, height=10, color=HouseParams.frame_color),
                    LinearLayout(width=8, height=14, color=HouseParams.window_color)
                ]
            ),
            LinearLayout(fill_width=True, height=4, color=HouseParams.frame_color),
            LinearLayout(
                layout_type="HORIZONTAL",
                childs=[
                    LinearLayout(width=8, height=14, color=HouseParams.window_color),
                    LinearLayout(width=2, height=10, color=HouseParams.frame_color),
                    LinearLayout(width=8, height=14, color=HouseParams.window_color),
                    LinearLayout(width=2, height=10, color=HouseParams.frame_color),
                    LinearLayout(width=8, height=14, color=HouseParams.window_color)
                ]
            ),
            LinearLayout(fill_width=True, height=4, color=HouseParams.frame_color),
            LinearLayout(
                layout_type="HORIZONTAL",
                childs=[
                    LinearLayout(width=8, height=14, color=HouseParams.window_color),
                    LinearLayout(width=2, height=10, color=HouseParams.frame_color),
                    LinearLayout(width=8, height=14, color=HouseParams.window_color),
                    LinearLayout(width=2, height=10, color=HouseParams.frame_color),
                    LinearLayout(width=8, height=14, color=HouseParams.window_color)
                ]
            )
        ]
    )


def get_1_2_window():
    return LinearLayout(
        layout_type="VERTICAL", color=HouseParams.frame_color, padding=4, childs=[
            LinearLayout(
                layout_type="HORIZONTAL",
                fill_width=True,
                childs=[
                    LinearLayout(fill_width=True, height=14, color=HouseParams.window_color),
                ]
            ),
            LinearLayout(fill_width=True, height=4, color=HouseParams.frame_color),
            LinearLayout(
                layout_type="HORIZONTAL",
                childs=[
                    LinearLayout(width=8, height=14, color=HouseParams.window_color),
                    LinearLayout(width=2, height=10, color=HouseParams.frame_color),
                    LinearLayout(width=8, height=14, color=HouseParams.window_color)
                ]
            )
        ]
    )


def get_2_2_window():
    return LinearLayout(
        layout_type="VERTICAL", color=HouseParams.frame_color, padding=4, childs=[
            LinearLayout(
                layout_type="HORIZONTAL",
                childs=[
                    LinearLayout(width=8, height=14, color=HouseParams.window_color),
                    LinearLayout(width=2, height=10, color=HouseParams.frame_color),
                    LinearLayout(width=8, height=14, color=HouseParams.window_color)
                ]
            ),
            LinearLayout(fill_width=True, height=4, color=HouseParams.frame_color),
            LinearLayout(
                layout_type="HORIZONTAL",
                childs=[
                    LinearLayout(width=8, height=14, color=HouseParams.window_color),
                    LinearLayout(width=2, height=10, color=HouseParams.frame_color),
                    LinearLayout(width=8, height=14, color=HouseParams.window_color)
                ]
            )
        ]
    )


def get_2_window():
    return LinearLayout(
        color=(255, 255, 255), padding=4, childs=[
            LinearLayout(
                layout_type="HORIZONTAL",
                childs=[
                    LinearLayout(width=8, height=14, color=(255, 0, 0)),
                    LinearLayout(width=2, height=10, color=(255, 255, 255)),
                    LinearLayout(width=8, height=14, color=(255, 0, 0))
                ]
            )
        ]
    )
