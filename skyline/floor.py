__author__ = 'Roderik'

from linearlayout import LinearLayout
from skyline import window
from skyline.params import SkylineParams


def get_instance():
    return LinearLayout(layout_type="HORIZONTAL", childs=[(window, SkylineParams.horizontal_windows)])