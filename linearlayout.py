__author__ = 'Roderik'


class LinearLayout:

    HORIZONTAL = 1
    VERTICAL = 2

    def __init__(self, layout_type):
        if layout_type == "HORIZONTAL":
            self.layout_type = LinearLayout.HORIZONTAL
        elif layout_type == "VERTICAL":
            self.layout_type = LinearLayout.VERTICAL
        self.childs = []
        self.offset_x = 0
        self.offset_y = 0

    def draw(self):
        pass

    def get_width(self):
        pass

    def get_height(self):
        pass

    def measure(self):
        for child in self.childs:
            child.measure()

        self.width = 0
        self.height = 0

        for child in self.childs:
            if self.layout_type == LinearLayout.HORIZONTAL:
                self.width += child.width
                if self.height < child.height:
                    self.height = child.height
            elif self.layout_type == LinearLayout.VERTICAL:
                self.height += child.height
                if self.width < child.width:
                    self.width = child.width

    def layout(self):
        for child in self.childs:
            child.offset_x = self.offset_x
            child.offset_y = self.offset_y
            if self.layout_type == LinearLayout.HORIZONTAL:
                self.offset_x += child.width
            elif self.layout_type == LinearLayout.VERTICAL:
                self.offset_y += child.height


    def add_child(self, child):
        self.childs.append(child)

    def draw(self, screen):
        for child in self.childs:
            child.draw(screen)