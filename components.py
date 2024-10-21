import pygame
from constants import *

class Slider():
    def __init__(self, x, y, width, height, min_value=0, max_value=10, increment=1):
        self.slider_bar = pygame.Rect(x, y, width, height)
        self.slider_button = pygame.Rect(x, y, height, height)
        self.slider_selected = False
        self.slider_color = red
        self.min_value = min_value 
        self.max_value = max_value 
        self.value = min_value
        self.increment = increment 

    def draw(self, screen):
        pygame.draw.rect(screen, blue, self.slider_bar)


        range = self.max_value - self.min_value
        unit = (self.slider_bar.width-self.slider_button.width) / range
        self.slider_button.x = unit * self.value + self.slider_bar.x 
        pygame.draw.rect(screen, self.slider_color, self.slider_button)

    def increase(self, value=None):
        value = value or self.increment
        self.value = min(self.value + value, self.max_value)
        
    def decrease(self, value=None):
        value = value or self.increment
        self.value = max(self.value - value, self.min_value)

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value


