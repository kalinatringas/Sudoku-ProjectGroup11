import pygame, sys
from board import Board

# Initialize pygame
pygame.init()

# Set up the screen
WIDTH = 900
HEIGHT = 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Game")

font = pygame.font.Font(None, 36)
large_font = pygame.font.Font(None, 48)

# Game states
START_SCREEN = 0
GAME_SCREEN = 1
WIN_SCREEN = 2
GAME_OVER = 3

# Initialize game state
game_state = START_SCREEN

def draw_game_over_screen(screen):
    screen.fill((255, 255, 255))
    game_over_text = large_font.render("Game Over", True, (255, 0, 0))
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))

def draw_win_screen(screen):
    screen.fill((255, 255, 255))
    win_text = large_font.render("Congratulations! You Won!", True, (0, 255, 0))
    screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2))


# Function to draw the start screen


# Set up the game board
difficulty = 0  # Set the difficulty level (0: Easy, 1: Medium, 2: Hard)
board = Board(WIDTH, HEIGHT, screen, difficulty)

# Function to draw the game board
def draw_board():
    screen.fill((255, 255, 255))  # Fill the screen with white color
    board.draw()  # Draw the Sudoku board
board_drawn = False

# Define button parameters
button_width = 150
button_height = 50
button_spacing = 20
button_x = (WIDTH - 3 * button_width - 2 * button_spacing) // 2
button_y = HEIGHT - 100

# Define button colors
button_color = (100, 100, 100)
hover_color = (150, 150, 150)

# Define button texts
button_texts = ["Reset", "Restart", "Exit"]

# Function to draw buttons
def draw_buttons():
    for i, text in enumerate(button_texts):
        button_rect = pygame.Rect(button_x + i * (button_width + button_spacing), button_y, button_width, button_height)
        pygame.draw.rect(screen, button_color, button_rect)
        # Check if mouse is hovering over the button
        if button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, hover_color, button_rect)
        # Render and blit button text
        button_font = pygame.font.Font(None, 30)
        text_surface = button_font.render(text, True, hover_color)
        text_rect = text_surface.get_rect(center=button_rect.center)
        screen.blit(text_surface, text_rect)

def draw_start_screen(BOOL):
    
    if BOOL == True:
        screen.fill((255, 255, 255))  # Fill the screen with white color
        
        title_text = large_font.render("Sudoku Game :3", True, (0, 0, 0))
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))

        easy_text = font.render("Easy (Press 1)", True, (0, 0, 0))
        screen.blit(easy_text, (WIDTH // 2 - easy_text.get_width() // 2, HEIGHT // 2))

        medium_text = font.render("Medium (Press 2)", True, (0, 0, 0))
        screen.blit(medium_text, (WIDTH // 2 - medium_text.get_width() // 2, HEIGHT // 2 + 40))

        hard_text = font.render("Hard (Press 3)", True, (0, 0, 0))
        screen.blit(hard_text, (WIDTH // 2 - hard_text.get_width() // 2, HEIGHT // 2 + 80))
    
        pygame.display.update()
    else:
        pass



# Main game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_state == START_SCREEN:
            
            draw_start_screen(True)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    difficulty = 0
                    game_state = GAME_SCREEN
                    board = Board(WIDTH, HEIGHT - 100, screen, difficulty)  # Adjusted height to accommodate the board
                elif event.key == pygame.K_2:
                    difficulty = 1
                    game_state = GAME_SCREEN
                    board = Board(WIDTH, HEIGHT - 100, screen, difficulty)  # Adjusted height to accommodate the board
                elif event.key == pygame.K_3:
                    difficulty = 2
                    game_state = GAME_SCREEN
                    board = Board(WIDTH, HEIGHT - 100, screen, difficulty)  # Adjusted height to accommodate the board

        elif game_state == GAME_SCREEN:
            screen.fill((255, 255, 255)) 
            board.draw()
            draw_buttons()

            # Handle mouse click events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    x, y = pygame.mouse.get_pos()
                    row, col = board.click(x, y)
                    if row is not None and col is not None:
                        board.select(row, col)
                elif event.button == 3:  # Right mouse button
                    if WIDTH // 2 - 60 <= event.pos[0] <= WIDTH // 2 + 60 and HEIGHT - 60 <= event.pos[1] <= HEIGHT - 20:
                        if board.check_board():
                            print("Board is solved!")
                        else:
                            print("Board is not solved yet.")

            # Handle key press events
            elif event.type == pygame.KEYDOWN:
                if board.selected_cell is not None and not board.selected_cell.is_preset:
                    if pygame.K_KP1 <= event.key <= pygame.K_KP9:
                        board.sketch(event.key - pygame.K_KP0)  # Input number from number pad
                    elif pygame.K_1 <= event.key <= pygame.K_9:
                        board.sketch(event.key - pygame.K_0)  # Input number from top row of keyboard
                    elif event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                        board.clear()  # Clear cell if backspace or delete is pressed
                    elif event.key == pygame.K_RETURN:
                        # Finalize the sketching
                        board.place_number(board.selected_cell.sketched_value)
                    board.move_selection(event)
                if board.selected_cell is not None and not board.selected_cell.is_preset:
                    # Check if the board is full after each key press
                    if board.is_full():
                        if board.check_board():
                            game_state = WIN_SCREEN
                        else:
                            game_state = GAME_OVER

            # Handle button clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                for i, text in enumerate(button_texts):
                    button_rect = pygame.Rect(button_x + i * (button_width + button_spacing), button_y, button_width, button_height)
                    if button_rect.collidepoint(mousex, mousey):
                        if text == "Reset":
                            board.reset_board()
                            pass
                        elif text == "Restart":
                            # Go back to the Game Start screen
                            game_state = START_SCREEN
                        elif text == "Exit":
                            # End the program
                            pygame.quit()
                            sys.exit()
             
        elif game_state == WIN_SCREEN:
            draw_win_screen(screen)
        elif game_state == GAME_OVER:
            draw_game_over_screen(screen)
   
          
        
# Inside the pygame event loop

    pygame.display.update()

pygame.quit()