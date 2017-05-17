__author__ = 'Roderik'


class LinearLayout:

    HORIZONTAL = 1
    VERTICAL = 2

    def __init__(self, layout_type, layout_id):
        if layout_type == "HORIZONTAL":
            self.layout_type = LinearLayout.HORIZONTAL
        elif layout_type == "VERTICAL":
            self.layout_type = LinearLayout.VERTICAL
        self.childs = []
        self.offset_x = 0
        self.offset_y = 0
        self.layout_id = layout_id

    def draw(self):
        pass

    def get_width(self):
        pass

    def get_height(self):
        pass

    def measure(self):
        self.width = 0
        self.height = 0

        for child in self.childs:
            child.measure()
            if self.layout_type == LinearLayout.HORIZONTAL:
                self.width += child.width
                if self.height < child.height:
                    self.height = child.height
            elif self.layout_type == LinearLayout.VERTICAL:
                self.height += child.height
                if self.width < child.width:
                    self.width = child.width
        print (self.layout_id, self.width, self.height)

    def layout(self, offset_x, offset_y):
        for child in self.childs:
            child.layout(offset_x, offset_y)
            if self.layout_type == LinearLayout.HORIZONTAL:
                offset_x += child.width
            elif self.layout_type == LinearLayout.VERTICAL:
                offset_y += child.height


    def add_child(self, child):
        self.childs.append(child)

    def draw(self, screen):
        for child in self.childs:
            child.draw(screen)