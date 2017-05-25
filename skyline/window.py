__author__ = 'Roderik'
from view import View
import random
from linearlayout import LinearLayout

def get_instance():
    return LinearLayout("HORIZONTAL", width=10, height=10, color=(255, 255, 0), margin=5, intensity=random.random())