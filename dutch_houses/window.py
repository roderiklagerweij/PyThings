__author__ = 'Roderik'

from view import View
from pygame import Color


def get_instance():
    return View(25, 25, color=Color(255, 255, 255), gravity='center_vertical')