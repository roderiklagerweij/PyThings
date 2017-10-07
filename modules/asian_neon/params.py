from drawers.horizontal_stripes import HorizontalStripesDrawer

__author__ = 'Roderik'
import string
import random
from drawers.vertical_stripes import VerticalStripesDrawer

class AsianNeonParams:

    font = None
    text = None
    text_color = None
    text_size = None
    sub_text = None
    sub_text_color = None
    sub_text_size = None
    border_color = None
    border_width = 0
    board_predrawer = None

    @staticmethod
    def init_params():

        font_selection = random.choice([0, 1])
        if font_selection == 0:
            AsianNeonParams.font = "DFKTL1B.ttf"
            AsianNeonParams.text_size = random.choice([24, 36, 48])
        else:
            AsianNeonParams.font = "GoJuOn.ttf"
            AsianNeonParams.text_size = random.choice([36, 48, 60])


        AsianNeonParams.sub_text_size = int(AsianNeonParams.text_size * (random.random()*0.5 + 0.5))

        valid_characters = [x for x in string.ascii_lowercase]
        valid_characters.remove('y')

        AsianNeonParams.text = ''
        AsianNeonParams.sub_text = ''

        for i in range(random.randint(1, 9)):
            AsianNeonParams.text += random.choice(valid_characters)

        for i in range(random.randint(1, len(AsianNeonParams.text))):
            AsianNeonParams.sub_text += random.choice(valid_characters)

        AsianNeonParams.border_width = random.choice([
            2, 4, 6
        ])


        applicable_colors = [
            (250, 255, 234),
            (249, 105, 4),
            (255, 243, 29),
            (187, 255, 138)
        ]

        AsianNeonParams.text_color = random.choice(applicable_colors)
        AsianNeonParams.sub_text_color = random.choice(applicable_colors)

        AsianNeonParams.border_color = random.choice(applicable_colors)

        if random.random() < 0.2:
            if random.choice([True, False]):
                AsianNeonParams.board_predrawer = HorizontalStripesDrawer(2, 15, AsianNeonParams.border_color)
            else:
                AsianNeonParams.board_predrawer = VerticalStripesDrawer(2, 15, AsianNeonParams.border_color)
        else:
            AsianNeonParams.board_predrawer = None
