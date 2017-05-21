__author__ = 'Roderik'
from linearlayout import LinearLayout
from view import View
from triangle import Triangle

# LinearLayout: orientation=VERTICAL
#     Triangle: w=fill, h=100, r=132, g=31, b=39, rotation=180
#
#     LinearLayout: orientation=HORIZONTAL, r=132, g=31, b=39, padding=25
#         View: w=25, h=25, r=255, g=255, b=255, gravity=center_vertical
#         View: w=10, h=0, r=0, g=0, b=0
#         View: w=50, h=100, r=255, g=255, b=255

def get_instance():
    return [
        LinearLayout('VERTICAL', None, 0),
        [
            Triangle('fill', 100, 132, 31, 39, None, 180),
            LinearLayout('HORIZONTAL', None, 25),
            [
                View(25, 25, 255, 255, 255, 'center_vertical', 0),
                View(10, 0, 0, 0, 0, None, 0),
                View(50, 100, 255, 255, 255, None, 0)
            ]

        ]
    ]
