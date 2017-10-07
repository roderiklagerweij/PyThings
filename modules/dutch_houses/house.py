__author__ = 'Roderik'
from view.linearlayout import LinearLayout
from view.triangle import Triangle
from modules.dutch_houses.house_params import HouseParams
from modules.dutch_houses import window

def get_instance():
    return LinearLayout('VERTICAL', childs=[
        Triangle('fill', 100, color=HouseParams.house_color, rotation=180),
        LinearLayout('HORIZONTAL', padding_left=25, padding_right=25, padding_top=25, color=HouseParams.house_color, childs=[
            window.get_instance()
        ])
    ])

