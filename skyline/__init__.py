__author__ = 'Roderik'
from skyline import tower
from skyline.params import SkylineParams



def get_instance():
    # gen parameters
    SkylineParams.init_params()

    # gen instance
    instance = tower.get_instance()

    # apply constraints


    return instance