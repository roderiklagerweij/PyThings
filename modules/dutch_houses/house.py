__author__ = 'Roderik'
from view.layout import LinearLayout
from view.triangle import Triangle
from modules.dutch_houses.house_params import HouseParams
from modules.dutch_houses import floor


def get_instance():
    return LinearLayout('VERTICAL', childs=[
        # roof
        Triangle(fill_width=True, height=100, color=HouseParams.house_color, rotation=180),
        # house
        LinearLayout('VERTICAL', color=HouseParams.house_color, childs=[
            floor.get_instance(),
            floor.get_instance(),
            floor.get_instance()
        ])
    ])

