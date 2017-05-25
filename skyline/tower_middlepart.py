__author__ = 'Roderik'

import random
from view import View
from circle import Circle
from linearlayout import LinearLayout


def get_instance():
    return
        LinearLayout("HORIZONTAL", fill_width=True),
        [
            Circle(5, color=(255, 255, 0), gravity="center_horizontal")
        ]

    # selection = random.randint(0, 1)
    # if selection == 0:
    #
    # elif selection == 1:
    #     pass
    # elif selection == 2:
    #     pass