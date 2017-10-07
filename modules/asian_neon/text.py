from view.layout import LinearLayout

__author__ = 'Roderik'

from modules.asian_neon.params import AsianNeonParams
from view.textview import TextView
import random

def get_instance():

    if random.choice([True, False]):
        return LinearLayout(
            layout_type="VERTICAL",
            childs=[
                TextView(AsianNeonParams.text, AsianNeonParams.text_color, AsianNeonParams.font, AsianNeonParams.text_size),
                LinearLayout(height=random.random()*25+10), # some space inbetween
                TextView(AsianNeonParams.sub_text, AsianNeonParams.sub_text_color, AsianNeonParams.font, AsianNeonParams.sub_text_size, gravity="center_horizontal"),
            ]
        )

    else:
        return LinearLayout(layout_type="VERTICAL", childs=[
            TextView(x, AsianNeonParams.text_color, AsianNeonParams.font, AsianNeonParams.text_size) for x in AsianNeonParams.text
        ])