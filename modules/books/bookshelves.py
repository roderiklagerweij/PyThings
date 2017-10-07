from view.layout import LinearLayout
from modules.books import bookshelf

__author__ = 'Roderik'


def get_instance():

    return LinearLayout(layout_type="VERTICAL",
                        childs=get_shelves())


def get_shelves():
    return [bookshelf.get_instance() for x in range(3)]
