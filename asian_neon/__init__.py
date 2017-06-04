from asian_neon import board
from asian_neon.params import AsianNeonParams

__author__ = 'Roderik'

def get_instance():

    AsianNeonParams.init_params()

    return board.get_instance()