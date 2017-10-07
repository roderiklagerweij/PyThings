__author__ = 'Roderik'

import random
from pygame import Color

class HouseParams:

    house_color = None

    def __init__(self):
        pass


    @staticmethod
    def init_params():
        HouseParams.house_color = random.choice([
            Color(132, 31, 39)
        ])