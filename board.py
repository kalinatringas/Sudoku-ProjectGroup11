import pygame
import numpy as np

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.grid = np.zeros((9, 9), dtype=int)  # Assuming a 9x9 Sudoku board
        self.selected_cell = None
    
    def draw(self):
        for row in range(9):
            for col in range(9):
                self.draw_cell(row, col)
    
    def draw_cell(self, row, col):
        x = col * self.width // 9
        y = row * self.height // 9
        rect = pygame.Rect(x, y, self.width // 9, self.height // 9)
        pygame.draw.rect(self.screen, (255, 255, 255), rect)  # White cell
        if self.grid[row][col] != 0:
            font = pygame.font.Font(None, 40)
            text = font.render(str(self.grid[row][col]), True, (0, 0, 0))
            self.screen.blit(text, (x + 20, y + 20))
    
    def select(self, row, col):
        self.selected_cell = (row, col)
    
    def click(self, x, y):
        row = y // (self.height // 9)
        col = x // (self.width // 9)
        if row >= 0 and col >= 0 and row < 9 and col < 9:
            self.select(row, col)
            return (row, col)
        return None
    
    def clear(self):
        if self.selected_cell:
            row, col = self.selected_cell
            self.grid[row][col] = 0
    
    def sketch(self, value):
        if self.selected_cell:
            row, col = self.selected_cell
            self.grid[row][col] = value  # Temporarily set the value
    
    def place_number(self, value):
        if self.selected_cell and self.is_valid_placement(value):
            row, col = self.selected_cell
            self.grid[row][col] = value
    
    def reset_to_original(self):
        self.grid = np.zeros((9, 9), dtype=int)  # Reset the grid
    
    def is_full(self):
        return np.all(self.grid != 0)
    
    def update_board(self):
        # Additional logic to update the board based on game rules
        pass
    
    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return (i, j)
        return None
    
    def check_board(self):
        # Check if the current board state is a valid solution
        return all(self.valid_in_row(row) and self.valid_in_col(col) and self.valid_in_box(row - row % 3, col - col % 3) for row in range(9) for col in range(9))
    
    def valid_in_row(self, row):
        return len(set(self.grid[row])) == 9
    
    def valid_in_col(self, col):
        return len(set(self.grid[:, col])) == 9
    
    def valid_in_box(self, row_start, col_start):
        box = self.grid[row_start:row_start + 3, col_start:col_start + 3]
        return len(set(box.flatten())) == 9

    def is_valid_placement(self, value):
        row, col = self.selected_cell
        if value not in self.grid[row] and value not in self.grid[:, col]:
            box_start_row, box_start_col = 3 * (row // 3), 3 * (col // 3)
            box = self.grid[box_start_row:box_start_row+3, box_start_col:box_start_col+3]
            if value not in box:
                return True
        return False
