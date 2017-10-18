from modules.dutch_houses.house_params import HouseParams
from modules.dutch_houses import house
from modules.dutch_houses import window
from modules.dutch_houses import window_side_decoration
from modules.dutch_houses import window_top_decoration
from util import constraint_applyer
from view.layout import LinearLayout

__author__ = 'Roderik'


def get_instance():

    HouseParams.init_params()

    instance = house.get_instance()

    # apply constraints
    constraint_applyer.apply_height_constraint(instance, [
        window.WINDOW,
        window_side_decoration.WINDOW_SIDE_HATCH
    ])

    constraint_applyer.apply_width_constraint(instance, [
        window.WINDOW,
        window_top_decoration.WINDOW_TOP_DECORATION
    ])


    return instance

def get_name():
    return 'dutch_houses'

def get_version():
    return '1'