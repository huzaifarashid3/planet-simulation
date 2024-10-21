import pygame
from components import Slider
from constants import *
from utils import draw_text
from game_server import start_server
import threading
import asyncio
from math import sin

pygame.init()
running = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

inc, dec = False, False

# cloud slider
slider = Slider(200, 500, 400, 20, 0, 100, 1)

font = pygame.font.Font(None, 36)

second = 0

def parabola(time, rain=2):
    return max(0, -(time-2)**2 + 4) + sinf(rain)

def sinf(t):
    return max(0, sin(t))

t = 0
prev = pygame.time.get_ticks()
while running:

    second += (pygame.time.get_ticks() - prev)
    prev = pygame.time.get_ticks()
    if second > 100:
        t += 1
        second = 0
    
    if t > 4:
        t = 0
    
    


    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_DOWN:
                dec = True
            if event.key == pygame.K_UP:
                inc = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                dec = False
            if event.key == pygame.K_UP:
                inc = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if slider.slider_button.collidepoint(mouse_x, mouse_y):
                slider.slider_selected = not(slider.slider_selected)



    mouse_x, mouse_y = pygame.mouse.get_pos()

    if slider.slider_selected:
        if inc: slider.increase()
        if dec: slider.decrease()

    slider.slider_color = yellow if slider.slider_selected else red
    
    screen.fill(black)

    draw_text(screen, f"Value: {slider.get_value()}", font, yellow, 10, 10)



    # async def server_coroutine():
    #     return await start_server()
    # loop = asyncio.get_event_loop()
    # x = loop.run_until_complete(server_coroutine())

    # x = parabola(t)
    x = start_server()
    slider.set_value(x)
    # slider.set_value(x*100 + 30)


    slider.draw(screen)
    pygame.display.flip()
    clock.tick(60)
        
pygame.quit()  

