__author__ = 'Roderik'
import string
import random

class AsianNeonParams:

    font = None
    text = None
    text_color = None
    text_size = None
    background_color = None
    border_color = None

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
        for i in range(random.randint(1, 6)):
            AsianNeonParams.text += random.choice(string.ascii_letters)

        AsianNeonParams.text_color = random.choice([
            (244, 220, 138),
            (225, 210, 220),
            (235, 175, 128),
            (121, 198, 227),
            (56, 154, 98),
            (250, 107, 82),
            (246, 217, 21)
        ])

        AsianNeonParams.text_size = random.choice([
            36, 48, 64, 72
        ])

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
