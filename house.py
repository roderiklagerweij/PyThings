__author__ = 'Roderik'
from linearlayout import LinearLayout
from view import View
from triangle import Triangle
from pygame import Color


def get_instance():
    return [
        LinearLayout('VERTICAL'),
        [
            Triangle('fill', 100, color=(132, 31, 39), rotation=180),
            LinearLayout('HORIZONTAL', padding=25, color=(255, 0, 0)),
            [
                View(25, 25, color=Color(255, 255, 255), gravity='center_vertical'),
                View(10, 0),
                View(50, 100, color=Color(255, 255, 255))
            ]
        ]
    ]
