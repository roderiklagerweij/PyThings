# __author__ = 'Roderik'
import constraint_applyer
from skyline import tower
from skyline.params import SkylineParams
from skyline import tower_section
from skyline import tower_middlepart
from skyline import roof
from skyline import two_tower
import random

def get_instance():
    # gen parameters
    SkylineParams.init_params()

    # gen instance
    instance = random.choice([
        tower.get_instance(),
        two_tower.get_instance()
    ])

    # apply constraints
    constraint_applyer.apply_constraint(instance, [
        roof.TOWER_ROOF,
        tower_section.TOP_TOWER_SECTION,
        tower_middlepart.TOWER_MIDDLE_PART
    ])

    return instance

def get_name():
    return 'skyline'

def get_version():
    return '2'