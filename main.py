##python3 sudoku.py
import pygame, sys
from pygame.locals import *

'''
Main (Required)
In addition to the above classes, students will have a sudoku.py file, where the main function will be run. This
file will contain code to create the different screens of the project (game start, game over, and game in
progress), and will form a cohesive project together with the rest of the code.
'''

import sudoku_generator as SG
pygame.init()
fps_clock = pygame.time.Clock()
red_color = pygame.Color(255, 0, 0)
green_color = pygame.Color(0, 255, 0)
blue_color = pygame.Color(0, 0, 255)
white_color = pygame.Color(255, 255, 255)
mousex, mousey = 0, 0

def draw_game_start(screen):
    start_title_font = pygame.font.Font(None, 100)
    bottom_font = pygame.font.Font(None, 70)

    # color background
    windos_surface_obj = pygame.display.set_mode((640, 480))
    size_x = 800
    size_y = 600
    screen_width = size_x
    screen_height = size_y
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill((255, 255, 255))

    pygame.display.update()
    fps_clock.tick(30)


