import string
import random
import colorsys
from util import colorutil


class BookParams:

    padding = 0
    color = None
    title_color = None
    title_size = 16
    text = None
    angle = 0

    @staticmethod
    def init_params():
        BookParams.padding = random.randint(5, 13)

        colors = [
            (87, 86, 103),
            (178, 95, 84),
            (70, 64, 77),
            (181, 134, 82),
            (136, 56, 49),
            (178, 155, 157),
            (70, 83, 90),
            (54, 56, 92),
            (113, 75, 66)
        ]
        BookParams.color = random.choice(colors)
        BookParams.title_color = (random.randint(0, 255),
                            random.randint(0, 255),
                            random.randint(0, 255))

        # vary color a bit
        BookParams.color = colorutil.vary_color(BookParams.color, 20)

        # darken color a bit
        BookParams.color = colorutil.darken(BookParams.color, 1.1-(random.random()))

        BookParams.title_color = colorutil.darken(BookParams.title_color, 0.3)
        BookParams.title_size = random.randint(12,18)

        text = ''
        for i in range(random.randint(0, 5) + 8):
            text += random.choice(string.ascii_letters)

        BookParams.text = text

        BookParams.angle = 0
        if random.randint(0, 10) == 0:
            BookParams.angle = random.randint(0, 10) - 5