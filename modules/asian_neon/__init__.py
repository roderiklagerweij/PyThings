from modules.asian_neon import board
from modules.asian_neon.params import AsianNeonParams

__author__ = 'Roderik'



def get_instance():

    AsianNeonParams.init_params()

    return board.get_instance()


def get_name():
    return 'asian_neon'

def get_version():
    return '1'