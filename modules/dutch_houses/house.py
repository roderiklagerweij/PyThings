__author__ = 'Roderik'
from linearlayout import LinearLayout
from triangle import Triangle
from modules.dutch_houses.house_params import HouseParams
from modules.dutch_houses import window

def get_instance():

    return [
        LinearLayout('VERTICAL'),
        [
            Triangle('fill', 100, color=HouseParams.house_color, rotation=180),
            LinearLayout('HORIZONTAL', padding_left=25, padding_right=25, padding_top=25, color=HouseParams.house_color),
            [
                window.get_instance()
                # TODO: RESTORE
                # View(10, 0),
                # View(50, 100, color=Color(255, 255, 255))
            ]
        ]
    ]
