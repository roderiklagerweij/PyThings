__author__ = 'Roderik'

import random
import math


class SkylineParams:

    horizontal_windows = None
    vertical_windows = None
    section_count = 2
    wall_color = None
    intensity = None

    @staticmethod
    def init_params():
        SkylineParams.horizontal_windows = round(random.random()*5) + 3
        SkylineParams.vertical_windows = round(random.random()*5) + 3
        SkylineParams.wall_color = (0, 0, 128)
        SkylineParams.intensity = (random.random() * 0.5) + 0.2
        SkylineParams.decrease_factor = (random.random() * 0.5) + 0.5

    @staticmethod
    def get_horizontal_window_count_for_floor(section_index):
        # print(section_index, round(math.pow(SkylineParams.decrease_factor, section_index+1) * SkylineParams.horizontal_windows))
        # return round(math.pow(SkylineParams.decrease_factor, section_index+1) * SkylineParams.horizontal_windows)
        return section_index*2

    @staticmethod
    def get_vertical_window_count_for_floor(section_index):
        # print (round(math.pow(SkylineParams.decrease_factor, section_index+1) * SkylineParams.vertical_windows))
        # return round(math.pow(SkylineParams.decrease_factor, section_index+1) * SkylineParams.vertical_windows)
        return section_index*2