from linearlayout import LinearLayout
from textview import TextView

__author__ = 'Roderik'


def get_instance():
    return LinearLayout(layout_type="HORIZONTAL", width=50, height=50, color=(0, 255, 0), gravity='center', debug_id='inner_layout', childs=[
        # LinearLayout(width=25, height=25, color=(255, 0, 0)),
        # LinearLayout(width=25, height=25, color=(0, 0, 255))
    ])
