import pygame
from cell import Cell
from sudoku_generator import SudokuGenerator


class Board:
    def __init__(self, screen_width, screen_height, screen, difficulty):
        self.screen_width = screen_width 
        self.screen_height = screen_height 
        self.cell_size = min(self.screen_width, self.screen_height) * 0.7 // 9  # Calculate cell size dynamically
        self.width = self.cell_size * 9
        self.height = self.cell_size * 9
        self.screen = screen
        self.difficulty = difficulty
        self.selected_cell = None
        row = []
        # creates a 2d list of cell objects
        self.cell_list = []

        if difficulty == 0:
            sudoku_generator = SudokuGenerator(row_length=9, removed_cells=30)  # Adjust parameters as needed
        elif difficulty == 1:
            sudoku_generator = SudokuGenerator(row_length=9, removed_cells=40)
        else:
            sudoku_generator = SudokuGenerator(row_length=9, removed_cells=50)
        sudoku_generator.fill_values()  # This generates a Sudoku puzzle
        sudoku_generator.remove_cells()  # This removes some cells based on the difficulty

        for i in range(9):
            cell_row = []
            for j in range(9):
                cell_value = sudoku_generator.get_board()[i][j]
                cell_row.append(Cell(cell_value, i, j, self.screen))  # Remove cell_size from arguments
            self.cell_list.append(cell_row)


        # self.update_board()
    # function to draw the lines and cells of the board
    def draw(self):
        # draws each line
        for i in range(1, 9):
            pygame.draw.line(
                self.screen,
                (100, 100, 100), #color
                (0, i * 100), #cordinates
                (900, i * 100), 
                3 #thickness
            )
        for i in range(1, 9):
            pygame.draw.line(
                self.screen,
                (100, 100, 100),
                (i * 100, 0),
                (i * 100, 900),
                3
            )
        for i in range(1, 3):
            pygame.draw.line(
                self.screen,
                (0, 0, 0),
                (0, i * 300),
                (900, i * 300),
                6
            )
        for i in range(1, 4):
            pygame.draw.line(
                self.screen,
                (0, 0, 0),
                (i * 300, 0),
                (i * 300, 900),
                6
            )

        # draws each cell
        for row in self.cell_list:
            for cell in row:
                cell.draw()

                # Redraw sketched number only for empty cells
                if not cell.value and not cell.is_preset:
                    num_font = pygame.font.Font(None, 30)
                    num_surf = num_font.render(cell.sketched_value, 0, (125, 125, 125))
                    num_rect = num_surf.get_rect(center=(cell.col * 100 + 20, cell.row * 100 + 20))
                    self.screen.blit(num_surf, num_rect)

    def print_board(self):
        for row in self.cell_list:
            for cell in row:
                print(cell.original_value if cell.original_value else '.', end=' ')
            print()

    # function to select and highlight a cell
    def select(self, row, col):
        if self.selected_cell:
            pygame.draw.rect(self.screen, (255, 255, 255), (self.selected_cell.col * 100, self.selected_cell.row * 100, 100, 100))
        self.selected_cell = self.cell_list[row][col]
        pygame.draw.rect(self.screen, (225, 225, 225), (col * 100, row * 100, 100, 100))

        # if not self.cell_list[row][col].is_preset:
        #     if self.selected_cell:
        #         pygame.draw.rect(self.screen, (255, 255, 255),
        #                          (self.selected_cell.col * 100, self.selected_cell.row * 100, 100, 100))
        #         self.selected_cell = self.cell_list[row][col]
        #         pygame.draw.rect(self.screen, (210, 210, 210), (col * 100, row * 100, 100, 100))

        # .is_preset locks in randomly generated values to be displayed
        # selected_cell checks whether the y
        # if self.selected_cell and not self.selected_cell.is_preset:
        #     pygame.draw.rect(self.screen, (255, 255, 255),
        #                      (self.selected_cell.col * 100, self.selected_cell.row * 100, 100, 100))
        #
        # self.selected_cell = self.cell_list[row][col]
        #
        # if not self.selected_cell.is_preset:
        #     pygame.draw.rect(self.screen, (210, 210, 210), (col * 100, row * 100, 100, 100))

    # function that determines which specific cell is clicked
    def click(self, x, y):
        if 0 < x < 900 and 0 < y < 900:
            row = y // 100
            col = x // 100
            return row, col
        else:
            return None

    # function that clears out a cell
    def clear(self):
        if not self.selected_cell.is_preset:
            self.selected_cell.set_cell_value(0)
            self.selected_cell.set_sketched_value(0)
            pygame.draw.rect(self.screen, (225, 225, 225),(self.selected_cell.col * 100, self.selected_cell.row * 100, 100, 100))
    
    def reset_board(self):
        for row in self.cell_list:
            for cell in row:
                if not cell.is_preset:
                    cell.set_cell_value(0)
                    cell.set_sketched_value(0)
                    pygame.draw.rect(self.screen, (255, 255, 255), (cell.col * 100, cell.row * 100, 100, 100))


    # function that adds a smaller number to the top left of a cell equal to user-entered value
    def sketch(self, value):
        # pygame.draw.rect(self.screen, (210, 210, 210),(self.selected_cell.col * 100, self.selected_cell.row * 100, 30, 30))
        # self.selected_cell.set_sketched_value(value)
        # num_font = pygame.font.Font(None, 30)
        # num_surf = num_font.render(self.selected_cell.sketched_value, 0, (0, 0, 0))
        # num_rect = num_surf.get_rect(center=(self.selected_cell.col * 100 + 20, self.selected_cell.row * 100 + 20))
        # self.screen.blit(num_surf, num_rect)
        if not self.selected_cell.is_preset:  # Only allow sketching on non-preset cells
            pygame.draw.rect(self.screen, (225, 225, 225),
                             (self.selected_cell.col * 100, self.selected_cell.row * 100, 30, 30))
            self.selected_cell.set_sketched_value(value)
            num_font = pygame.font.Font(None, 30)
            num_surf = num_font.render(self.selected_cell.sketched_value, 0, (125, 125, 125))
            num_rect = num_surf.get_rect(center=(self.selected_cell.col * 100 + 20, self.selected_cell.row * 100 + 20))
            self.screen.blit(num_surf, num_rect)




    # function that changes the value of the selected cell
    def place_number(self, value):
        # pygame.draw.rect(self.screen, (210, 210, 210),(self.selected_cell.col * 100, self.selected_cell.row * 100, 100, 100))
        # self.selected_cell.set_cell_value(value)
        # # self.update_board()
        if not self.selected_cell.is_preset:  # Only allow placing numbers on non-preset cells
            pygame.draw.rect(self.screen, (225, 225, 225),
                             (self.selected_cell.col * 100, self.selected_cell.row * 100, 100, 100))
            self.selected_cell.set_cell_value(value)

    def reset_to_original(self):
        for row in self.cell_list:
            for cell in row:
                if cell.original_value != "0":
                    cell.set_cell_value(cell.original_value)
                cell.set_sketched_value(
                    "0" if cell.original_value == "0" else "")  # Set sketched value to empty string for non-empty cells
                pygame.draw.rect(self.screen, (255, 255, 255), (cell.col * 100, cell.row * 100, 100, 100))

    def is_full(self):
        for row in self.cell_list:
            for cell in row:
                if cell.value == "":
                    return False  # Found an empty cell, board is not full
        return True  # No empty cells found, board is full

    def update_board(self):
        # Iterates over each cell in the list, and updates the value within the 2D board. Uses the original_value of each cell.

        for i in range(9):
            for j in range(9):
                self.cell_list[i][j].value = str(self.cell_list[i][j].original_value) if self.cell_list[i][j].original_value else ""

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.cell_list[i][j].value == "":
                    # Returns the row and column indices of the empty cell
                    return i,j
        # Returns None if no empty cell is found
        return None

    def check_board(self):

        # Checking rows
        for row in self.cell_list:
            values = set()
            for cell in row:
                cell_value = cell.value
                # If any cell in the row is empty, then the board is not solved yet.
                if cell_value == "":
                    return False
                # If there are any duplicate values in the row, then the board is not solved yet.
                if cell_value in values:
                    return False
                values.add(cell_value)

        # Checking columns
        for col in range(9):
            values = set()
            for row in range(9):
                cell_value = self.cell_list[row][col].value
                # If any duplicate values in the column, the board is not solved yet.
                if cell_value in values:
                    return False
                values.add(cell_value)

        # Checking 3x3 subgrids
        for i in range (0, 9, 3):
            for j in range(0, 9, 3):
                values = set()
                for row in range(3):
                    for col in range(3):
                        cell_value = self.cell_list[i + row][j + col].value
                        if cell_value in values:
                            return False
                        values.add(cell_value)
        return True