__author__ = 'Roderik'

class ArgumentParser():

    def __init__(self):
        pass


    def parse(self, line):
        args = {}
        for arg in line.strip().split(':')[1].split(','):
            att = arg.split('=')[0].strip()
            value = arg.split('=')[1].strip()
            args[att] = value

        return args
