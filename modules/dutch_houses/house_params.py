__author__ = 'Roderik'

import random

class HouseParams:

    house_color = None
    window_color = None
    frame_color = None
    floor_layout = None
    window_layout = None

    def __init__(self):
        pass

    @staticmethod
    def init_params():

        HouseParams.house_color = random.choice([
            (26, 26, 22),
            (50, 43, 36),
            (178, 130, 93),
            (166, 99, 72),
            (113, 57, 62),
            (177, 54, 32),
            (69, 37, 30)
        ])

        HouseParams.window_color = random.choice([
            (173, 216, 230),
            (26, 29, 36)
        ])

        HouseParams.frame_color = random.choice([
            (232, 233, 219),
            (221, 218, 182)
        ])

        if random.choice([True, False]):
            HouseParams.floor_layout = FloorLayout.layout2windows
        else:
            HouseParams.floor_layout = FloorLayout.layout3windows

        HouseParams.window_layout = random.choice([
            WindowLayout.window_layout_3_3_3,
            WindowLayout.window_layout_1_2,
            WindowLayout.window_layout_2_2,
            WindowLayout.window_layout_2])

class FloorLayout:
    layout2windows = 0
    layout3windows = 1

class WindowLayout:
    window_layout_3_3_3 = 0
    window_layout_1_2 = 1
    window_layout_2_2 = 2
    window_layout_2 = 3
