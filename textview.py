from linearlayout import LinearLayout
from pygame import Surface
import pygame

class TextView(LinearLayout):

    def __init__(self, text, text_color, font_size, *args, **kwargs):
        self.font = pygame.font.SysFont("comicsansms", font_size)
        self.text_color = text_color
        self.text = text
        w, h = self.font.size(text)
        super().__init__(width=w, height=h, *args, **kwargs)

    def draw(self, screen):
        surface = Surface((self.width, self.height))
        text = self.font.render(self.text, True, self.text_color)
        # surface.fill((255, 0, 0))
        surface.blit(text, (0, 0))
        screen.blit(surface, (self.offset_x, self.offset_y))