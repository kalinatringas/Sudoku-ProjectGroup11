##python3 sudoku.py
import pygame, sys
from pygame.locals import *
import cell, board 
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
font = pygame.font.Font(None, 36)
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

selected_box = None

#(source_surf, (posx, posy), cropped_region)

mousex, mousey = 0, 0
pygame.display.update()

box_size = 66
box_spacing = 5
num_rows = 3
num_cols = 3
bigbox_spacing = 2

start_x = 76
start_y = 99

mini_grid_size = 3* (box_size + box_spacing) + box_spacing

def draw_mini_grids():
    for row in range(3):
        for col in range(3):
            mini_grid_x =  col * (mini_grid_size + bigbox_spacing)
            mini_grid_y =  row * (mini_grid_size + bigbox_spacing)
            draw_mini_grid(mini_grid_x, mini_grid_y)

def draw_mini_grid(x,y):
    for row in range(num_rows):
        for col in range(num_cols):
            box_x = x + col * (box_size + box_spacing)
            box_y = y + row * (box_size + box_spacing)
            pygame.draw.rect(screen, (red_color), (box_x + start_x, box_y + start_y, box_size, box_size), 2) #this will draw some boxes!!


#i need to load images!! 
while True: #main game loop
    screen.blit(sudoku_board, (image_x, image_y))
    draw_mini_grids()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                print("escape key pressed!")
                pygame.quit()
                sys.exit()
            elif event.key == K_SPACE:
                print(pygame.mouse.get_pos())
        elif event.type == MOUSEBUTTONDOWN:
            mousex, mousey = pygame.mouse.get_pos()
            clicked_box_col = mousex // (box_size + box_size)
            clicked_box_row = mousex // (box_size + box_size)
            selected_box = (clicked_box_row, clicked_box_col)
            input_text = ""
        elif event.type == KEYUP:
            pass

        elif event.type == pygame.KEYDOWN:
            if selected_box is not None:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key in range(pygame.K_0, pygame.K_9 + 1):
                    input_text += event.unicode
    
    if selected_box is not None:
        box_x = selected_box[1] * (box_size + box_spacing)
        box_y = selected_box[0] * (box_size + box_spacing)
        pygame.draw.rect(screen, (255, 0, 0), (box_x, box_y, box_size, box_size), 2)

        # Render and blit the input text onto the selected box
        text_surface = font.render(input_text, True, (255, 255, 255))
        screen.blit(text_surface, (box_x + 10, box_y + 10))

    pygame.display.update()
