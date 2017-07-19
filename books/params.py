import string
import random

class BookParams:

    width = 0
    height = 0
    color = None
    title_color = None

    @staticmethod
    def init_params():
        BookParams.width = random.randint(20, 60)
        BookParams.height = random.randint(120, 300)

        BookParams.color = (random.randint(0, 255),
                            random.randint(0, 255),
                            random.randint(0, 255))

        BookParams.title_color = (random.randint(0, 255),
                            random.randint(0, 255),
                            random.randint(0, 255))
