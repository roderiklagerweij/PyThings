__author__ = 'Roderik'

import random
import math


class SkylineParams:

    horizontal_windows = None
    vertical_windows = None
    section_count = 0
    wall_color = None
    intensity = None
    middle_part_height = 0
    has_section_divider = False

    @staticmethod
    def init_params():
        SkylineParams.section_count = random.choice([1, 2, 3, 4, 5])
        SkylineParams.horizontal_windows = round(random.random()*6) + 3
        SkylineParams.vertical_windows = round(random.random()*5) + 3
        SkylineParams.wall_color = (0, 0, 128)
        SkylineParams.intensity = (random.random() * 0.5) + 0.2
        SkylineParams.horizontal_decrease_factor = (random.random() * 0.3) + 0.7
        SkylineParams.vertical_decrease_factor = (random.random() * 0.3) + 0.7
        SkylineParams.middle_part_height = random.choice([8, 12, 16])
        SkylineParams.has_section_divider = random.choice([True, False])

    @staticmethod
    def get_horizontal_window_count_for_floor(section_index):
        return round(math.pow(SkylineParams.horizontal_decrease_factor, (SkylineParams.section_count - section_index) - 1) * SkylineParams.horizontal_windows)


    @staticmethod
    def get_vertical_window_count_for_floor(section_index):
        value = round(math.pow(SkylineParams.vertical_decrease_factor, (SkylineParams.section_count - section_index) - 1) * SkylineParams.vertical_windows)
        return value

