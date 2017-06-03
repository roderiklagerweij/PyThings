import constraint_applyer

__author__ = 'Roderik'
from skyline import tower
from skyline.params import SkylineParams
from skyline import tower_section
from skyline import tower_middlepart
from skyline import roof

def get_instance():
    # gen parameters
    SkylineParams.init_params()

    # gen instance
    instance = tower.get_instance()

    # apply constraints
    constraint_applyer.apply_constraint(instance, [
        roof.TOWER_ROOF,
        tower_section.TOP_TOWER_SECTION,
        tower_middlepart.TOWER_MIDDLE_PART
    ])

    return instance