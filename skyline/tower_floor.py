__author__ = 'Roderik'

from linearlayout import LinearLayout
from skyline import tower_window
from skyline.params import SkylineParams


def get_instance():
    return LinearLayout(layout_type="HORIZONTAL", childs=[(tower_window, SkylineParams.horizontal_windows)])