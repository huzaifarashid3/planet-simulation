import pygame

def draw_text(screen, text, font, color, x, y):
    text = font.render(text, True, color)
    screen.blit(text, (x, y))