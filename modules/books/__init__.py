from modules.books import bookshelf
from modules.books import bookshelves
from modules.books.params import BookParams

__author__ = 'Roderik'


def get_instance():

    BookParams.init_params()

    return bookshelves.get_instance()


def get_name():
    return 'books'

def get_version():
    return '1'