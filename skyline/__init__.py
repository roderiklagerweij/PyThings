__author__ = 'Roderik'
from skyline import tower
from skyline.params import SkylineParams
from skyline import tower_section

import view_finder

def get_instance():
    # gen parameters
    SkylineParams.init_params()

    # gen instance
    instance = tower.get_instance()

    # apply constraints

    tower_roof_views = view_finder.find_views_with_id(tower.TOWER_ROOF, instance)
    top_section_views = view_finder.find_views_with_id(tower_section.TOP_TOWER_SECTION, instance)


    return instance