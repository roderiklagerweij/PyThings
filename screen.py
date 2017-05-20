__author__ = 'Roderik'


class Screen:

    def __init__(self):
        self.childs = []

    def measure(self):
        for child in self.childs:
            child.measure()

    def post_measure(self, parent_width, parent_height):
        for child in self.childs:
            child.post_measure(parent_width, parent_height)

    def layout(self, offset_x, offset_y, parent_width, parent_height):
        for child in self.childs:
            child.layout(offset_x, offset_y, parent_width, parent_height)

    def add_child(self, child):
        self.childs.append(child)

    def draw(self, screen):
        for child in self.childs:
            child.draw(screen)
