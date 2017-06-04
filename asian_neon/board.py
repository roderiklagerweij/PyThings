from asian_neon.params import AsianNeonParams
from linearlayout import LinearLayout
from asian_neon import text

__author__ = 'Roderik'


def get_instance():

    return LinearLayout(
        color=AsianNeonParams.background_color,
        padding=16,
        childs=[
            text.get_instance()
        ])