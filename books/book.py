from books.params import BookParams
from linearlayout import LinearLayout
from textview import TextView

__author__ = 'Roderik'


def get_instance():
    return LinearLayout(
        layout_type="HORIZONTAL",
        childs=[
            # LinearLayout(width=10, height=10, color=(255, 0, 0), gravity="center_vertical"),
            LinearLayout(color=BookParams.color, padding=10, rotation=270, childs=[
                TextView('mdnjf sjdkfnsd n', BookParams.title_color, None, 16)]),
            # LinearLayout(width=10, height=10, color=(255, 0, 0), gravity="center_vertical")
        ])


