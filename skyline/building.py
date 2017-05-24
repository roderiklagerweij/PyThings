__author__ = 'Roderik'

from view import View
from linearlayout import LinearLayout
from skyline.params import SkylineParams


def get_instance():
    return [
        LinearLayout("HORIZONTAL", gravity="center"),
        [
            View(width=SkylineParams.width, height=SkylineParams.height, color=(0, 0, 255))
        ]

    ]