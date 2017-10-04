from modules.books import book
from linearlayout import LinearLayout

__author__ = 'Roderik'


def get_instance():
    return LinearLayout(layout_type="VERTICAL",
                        childs=[
                            LinearLayout(layout_type="HORIZONTAL",
                                         childs=get_books()),
                            LinearLayout(height=10, width=10, fill_width=True,
                                         color=(255, 0, 0))
                        ])




def get_books():
    return [book.get_instance() for x in range(30)]
