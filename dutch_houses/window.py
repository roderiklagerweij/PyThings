__author__ = 'Roderik'

from linearlayout import LinearLayout
from pygame import Color


def get_instance():
    return LinearLayout(width=25, height=25, color=Color(255, 255, 255), gravity='center_vertical')