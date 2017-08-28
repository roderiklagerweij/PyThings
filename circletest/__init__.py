from circletest import circletest
from circletest.params import CircleTestParams

__author__ = 'Roderik'


def get_instance():

    CircleTestParams.init_params()

    return circletest.get_instance()


def get_name():
    return 'circletest'

def get_version():
    return '1'