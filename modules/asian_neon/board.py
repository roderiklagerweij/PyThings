import random

from modules.asian_neon.params import AsianNeonParams
from view.layout import LinearLayout
from modules.asian_neon import text


__author__ = 'Roderik'


def get_instance():

    selection = random.randint(1, 2)

    if selection == 0:
        return get_inner_text_board()
    elif selection == 1:  # 1 border
        return LinearLayout(
            color=AsianNeonParams.border_color,
            padding=AsianNeonParams.border_width,
            childs=[
                get_inner_text_board()
            ]
        )
    elif selection == 2: # 2 borders
        return LinearLayout(
            color=AsianNeonParams.border_color,
            padding=AsianNeonParams.border_width,
            childs=[
                # outer border
                LinearLayout(
                    color=(0, 0, 0),
                    padding=AsianNeonParams.border_width,
                    childs=[
                        LinearLayout(
                            color=AsianNeonParams.border_color,
                            padding=AsianNeonParams.border_width,
                            childs=[
                                get_inner_text_board()
                            ]
                        )

                    ])
            ]
        )


def get_inner_text_board():
    return LinearLayout(
        color=(0, 0 , 0),
        padding=16,
        predrawer=AsianNeonParams.board_predrawer,
        childs=[
            text.get_instance()
        ])