__author__ = 'Roderik'

from linearlayout import LinearLayout
from skyline.params import SkylineParams
from skyline import floor


def get_instance():
    return [
        LinearLayout("VERTICAL", gravity="center", color=(0, 0, 255), padding=3, repeat_include=(floor, SkylineParams.floor_count))
    ]