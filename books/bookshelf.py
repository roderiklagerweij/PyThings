from books import book
from linearlayout import LinearLayout

__author__ = 'Roderik'


def get_instance():
    return LinearLayout(layout_type="HORIZONTAL",
                        childs=get_books())


def get_books():
    return [book.get_instance() for x in range(30)]
