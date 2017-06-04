from linearlayout import LinearLayout
from textview import TextView

__author__ = 'Roderik'


def get_instance():
    return TextView("Bla", (255, 0, 0), 72)
    # return LinearLayout(childs=[
    #     TextView("Bla", 72)
    # ])