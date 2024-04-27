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
pygame.display.set_caption("Sudoku!")
fps_clock = pygame.time.Clock()
red_color = pygame.Color(255, 0, 0)
green_color = pygame.Color(0, 255, 0)
size_x = 800
size_y = 800
screen_width = size_x
screen_height = size_y
blue_color = pygame.Color(0, 0, 255)
black_color = pygame.Color(0,0,0)
white_color = pygame.Color(255, 255, 255)
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((white_color))


sudoku_board = pygame.image.load("assets/Sudoku.png")
sudoku_board = pygame.transform.scale(sudoku_board, (screen_width-50, screen_height-50))
image_rect = sudoku_board.get_rect()
image_x = (screen_width - image_rect.width) // 2
image_y = (screen_height - image_rect.height) // 2

sudoku_0 = pygame.image.load("assets/0.png")
sudoku_1 = pygame.image.load("assets/1.png")
sudoku_2 = pygame.image.load("assets/2.png")
sudoku_3 = pygame.image.load("assets/3.png")
sudoku_4 = pygame.image.load("assets/4.png")
sudoku_5 = pygame.image.load("assets/5.png")
sudoku_6 = pygame.image.load("assets/6.png")
sudoku_7 = pygame.image.load("assets/7.png")
sudoku_8 = pygame.image.load("assets/8.png")
sudoku_9 = pygame.image.load("assets/9.png")

#(source_surf, (posx, posy), cropped_region)
screen.blit(sudoku_board, (image_x, image_y))
mousex, mousey = 0, 0
pygame.display.update()

#i need to load images!! 
while True: #main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
