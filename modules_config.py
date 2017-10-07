__author__ = 'Roderik'
from modules import books
from modules import skyline
from modules import dutch_houses
from modules import asian_neon

def get_modules():
    return [asian_neon, books, skyline, dutch_houses]

def get_active_module():
    return asian_neon