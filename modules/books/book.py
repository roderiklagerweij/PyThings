from modules.books.params import BookParams
from view.layout import LinearLayout
from view.textview import TextView

__author__ = 'Roderik'


def get_instance():
    BookParams.init_params()
    return LinearLayout(
        layout_type="HORIZONTAL",
        gravity="bottom",
        childs=[
            LinearLayout(
                rotation=270 + BookParams.angle,
                childs=[
                    LinearLayout(
                        padding=BookParams.padding,
                        color=BookParams.color,
                        childs=[
                            TextView(BookParams.text, BookParams.title_color, "DFKTL1B.ttf", BookParams.title_size)])
                ]
            )
        ])
