from asian_neon.params import AsianNeonParams
from linearlayout import LinearLayout
from asian_neon import text
import random

__author__ = 'Roderik'


def get_instance():

    selection = random.randint(0, 2)
    if selection == 0:
        return get_inner_text_board()
    elif selection == 1:
        return LinearLayout(
            color=AsianNeonParams.background_color,
            padding=2,
            childs=[
                LinearLayout( # border
                              color=(255, 0, 0),
                              padding=2,
                              childs=[
                                  get_inner_text_board()
                              ])
            ]
        )
    elif selection == 2:
        return LinearLayout(
            color=AsianNeonParams.background_color,
            padding=2,
            childs=[
                # outer border
                LinearLayout(
                    color=AsianNeonParams.border_color,
                    padding=2,
                    childs=[
                        LinearLayout(
                            color=AsianNeonParams.background_color,
                            padding=2,
                            childs=[
                                # second inner border
                                LinearLayout(
                                    color=AsianNeonParams.border_color,
                                    padding=2,
                                    childs=[
                                        get_inner_text_board()
                                    ]
                                )
                            ]
                        )

                    ])
            ]
        )


def get_inner_text_board():
    return LinearLayout(
        color=AsianNeonParams.background_color,
        padding=16,
        childs=[
            text.get_instance()
        ])