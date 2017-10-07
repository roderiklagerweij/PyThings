from modules.dutch_houses.house_params import HouseParams
from modules.dutch_houses import house

__author__ = 'Roderik'


def get_instance():

    HouseParams.init_params()

    return house.get_instance()


def get_name():
    return 'dutch_houses'

def get_version():
    return '1'