import string
import random
import colorsys

class BookParams:

    width = 0
    height = 0
    color = None
    title_color = None
    text = None
    angle = 0

    @staticmethod
    def init_params():
        BookParams.width = random.randint(20, 60)
        BookParams.height = random.randint(120, 300)

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

        BookParams.title_color = colorsys.rgb_to_hsv(BookParams.title_color[0], BookParams.title_color[1], BookParams.title_color[2])
        BookParams.title_color = colorsys.hsv_to_rgb(BookParams.title_color[0], BookParams.title_color[1], BookParams.title_color[2]*0.3)

        text = ''
        for i in range(random.randint(0, 5) + 8):
            text += random.choice(string.ascii_letters)

        BookParams.text = text

        BookParams.angle = 0
        if random.randint(0, 10) == 0:
            BookParams.angle = random.randint(0, 10) - 5