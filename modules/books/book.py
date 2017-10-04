from modules.books.params import BookParams
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
                padding=BookParams.padding,
                rotation=270 + BookParams.angle,
                childs=[
                    TextView(BookParams.text, BookParams.title_color, "DFKTL1B.ttf", BookParams.title_size)])
        ])
