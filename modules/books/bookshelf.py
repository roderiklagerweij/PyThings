from modules.books import book
from view.linearlayout import LinearLayout

__author__ = 'Roderik'


def get_instance():
    return LinearLayout(layout_type="VERTICAL",
                        childs=[
                            LinearLayout(layout_type="HORIZONTAL",
                                         childs=get_books()),
                            LinearLayout(height=10, width=10, fill_width=True,
                                         color=(133, 96, 73)),
                            LinearLayout(height=15)
                        ])




def get_books():
    return [book.get_instance() for x in range(30)]
