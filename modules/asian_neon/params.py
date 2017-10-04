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
    background_color = None
    border_color = None
    board_predrawer = None

    @staticmethod
    def init_params():

        AsianNeonParams.font = random.choice([
            "JLR-Chinese-Love.ttf",
            "ChineseWhisper.ttf",
            "DFKTL1B.ttf",
            "DFXSM1B.ttf",
            "GB5FS1B.ttf",
            "GoJuOn.ttf",
        ])

        AsianNeonParams.text = ''
        AsianNeonParams.sub_text = ''

        for i in range(random.randint(1, 9)):
            AsianNeonParams.text += random.choice(string.ascii_letters)

        for i in range(random.randint(1, len(AsianNeonParams.text))):
            AsianNeonParams.sub_text += random.choice(string.ascii_letters)

        text_colors = [
            (244, 220, 138),
            (225, 210, 220),
            (235, 175, 128),
            (121, 198, 227),
            (56, 154, 98),
            (250, 107, 82),
            (246, 217, 21)
        ]
        AsianNeonParams.text_color = random.choice(text_colors)
        AsianNeonParams.sub_text_color = random.choice(text_colors)

        AsianNeonParams.text_size = random.choice([
            16, 24, 36, 48
        ])
        AsianNeonParams.sub_text_size = int(AsianNeonParams.text_size * (random.random()*0.5 + 0.5))


        AsianNeonParams.background_color = random.choice([
            (8, 196, 22),
            (29, 32, 34),
            (219, 31, 49),
            (1, 0, 191),
            (10, 38, 83),
            (207, 225, 251)
        ])

        AsianNeonParams.border_color = random.choice([
            (255, 0, 0),
            (252, 235, 108),
            (255, 255, 0)
        ])

        if random.random() < 0.2:
            if random.choice([True, False]):
                AsianNeonParams.board_predrawer = HorizontalStripesDrawer(2, 15, (255, 0, 0))
            else:
                AsianNeonParams.board_predrawer = VerticalStripesDrawer(2, 15, (255, 0, 0))
        else:
            AsianNeonParams.board_predrawer = None