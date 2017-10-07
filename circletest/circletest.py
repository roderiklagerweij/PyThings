from view.linearlayout import LinearLayout

__author__ = 'Roderik'


def get_instance():
    return LinearLayout(layout_type="HORIZONTAL", gravity='center', childs=[
        LinearLayout(width=25, height=25, color=(0, 255, 0)),
        LinearLayout(width=25, height=25, color=(0, 0, 255))
    ])
