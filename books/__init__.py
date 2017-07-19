from books import book
from books.params import BookParams

__author__ = 'Roderik'


def get_instance():

    BookParams.init_params()

    return book.get_instance()


def get_name():
    return 'books'

def get_version():
    return '1'