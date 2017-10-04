from books.params import BookParams
from linearlayout import LinearLayout
from textview import TextView

__author__ = 'Roderik'


def get_instance():
    BookParams.init_params()
    return LinearLayout(
        layout_type="HORIZONTAL",
        gravity="bottom",
        childs=[
            LinearLayout(
                color=BookParams.color,
                padding=10,
                rotation=270 + BookParams.angle,
                childs=[
                    TextView(BookParams.text, BookParams.title_color, "DFKTL1B.ttf", 16)])
        ])
