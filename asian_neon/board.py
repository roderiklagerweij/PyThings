from asian_neon.params import AsianNeonParams
from linearlayout import LinearLayout
from textview import TextView

__author__ = 'Roderik'


def get_instance():
    return LinearLayout(
        color=AsianNeonParams.background_color,
        padding=16,
        childs=[
            TextView(AsianNeonParams.text, AsianNeonParams.text_color, AsianNeonParams.font, AsianNeonParams.text_size)
        ])