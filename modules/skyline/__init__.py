# __author__ = 'Roderik'
import random

from util import constraint_applyer
from modules.skyline.params import SkylineParams
from modules.skyline import roof, tower_middlepart, two_tower, tower, tower_section
from modules.skyline import two_tower


def get_instance():
    # gen parameters
    SkylineParams.init_params()

    # gen instance
    instance = random.choice([
        tower.get_instance(),
        two_tower.get_instance()
    ])

    # apply constraints
    constraint_applyer.apply_width_constraint(instance, [
        roof.TOWER_ROOF,
        tower_section.TOP_TOWER_SECTION,
        tower_middlepart.TOWER_MIDDLE_PART
    ])

    return instance

def get_name():
    return 'skyline'

def get_version():
    return '2'