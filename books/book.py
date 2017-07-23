from books.params import BookParams
from linearlayout import LinearLayout
from textview import TextView

__author__ = 'Roderik'


def get_instance():
    return LinearLayout(layout_type="HORIZONTAL", childs=[
        LinearLayout(width=10, height=10, color=(255, 0, 0)),
        LinearLayout(layout_type="HORIZONTAL",
                        padding=10,
                        color=BookParams.color,
                        childs=get_text(), rotation=270),
        LinearLayout(width=10, height=10, color=(255, 0, 0)),
    ])


def get_text():
    return [TextView(x, BookParams.title_color, None, 16) for x in 'mdnjf sjdkfnsd n']