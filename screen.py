__author__ = 'Roderik'


class Screen:

    def __init__(self):
        self.childs = []

    def measure(self):
        for child in self.childs:
            child.measure()

    def layout(self):
        for child in self.childs:
            child.layout()

    def add_child(self, child):
        self.childs.append(child)

    def draw(self, screen):
        for child in self.childs:
            child.draw(screen)
