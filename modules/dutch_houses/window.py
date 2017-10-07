__author__ = 'Roderik'

from pygame import Color

from view.layout import LinearLayout


def get_instance():
    return LinearLayout(width=25, height=25, color=Color(255, 255, 255), gravity='center_vertical')