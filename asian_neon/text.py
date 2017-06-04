from linearlayout import LinearLayout

__author__ = 'Roderik'

from asian_neon.params import AsianNeonParams
from textview import TextView
import random

def get_instance():

    if random.choice([True, False]):
        return TextView(AsianNeonParams.text, AsianNeonParams.text_color, AsianNeonParams.font, AsianNeonParams.text_size)
    else:
        return LinearLayout(layout_type="VERTICAL", childs=[
            TextView(x, AsianNeonParams.text_color, AsianNeonParams.font, AsianNeonParams.text_size) for x in AsianNeonParams.text
        ])