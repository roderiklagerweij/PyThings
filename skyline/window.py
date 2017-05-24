__author__ = 'Roderik'
from view import View
import random

def get_instance():
    return View(width=15, height=15, color=(255, 255, 0), padding=3, intensity=random.random())