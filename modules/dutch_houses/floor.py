from modules.dutch_houses import HouseParams
from modules.dutch_houses.house_params import FloorLayout
from modules.dutch_houses import window

__author__ = 'Roderik'

from view.layout import LinearLayout


def get_instance():
    if HouseParams.floor_layout == FloorLayout.layout2windows:
        return get_2_window_floorlayout()
    elif HouseParams.floor_layout == FloorLayout.layout3windows:
        return get_3_window_floorlayout()


def get_2_window_floorlayout():
    return LinearLayout(
        layout_type="HORIZONTAL", padding=4, childs=[
            get_window(),
            LinearLayout(width=4, height=1),
            get_window()])


def get_3_window_floorlayout():
    return LinearLayout(
        layout_type="HORIZONTAL", padding=4, childs=[
            get_window(),
            LinearLayout(width=4, height=1),
            get_window(),
            LinearLayout(width=4, height=1),
            get_window()])


def get_window():
    return window.get_instance()
