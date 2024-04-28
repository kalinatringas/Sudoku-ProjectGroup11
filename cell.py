import pygame


class Cell:
    # init function
    def __init__(self, value, row, col, screen, cell_size=100):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.cell_size = cell_size
        self.sketched_value = None
        self.is_preset = True if value != 0 else False


    # setter for the cell's value
    def set_cell_value(self, value):
        self.value = str(value) if value != 0 else ""

    # setter for the value that will appear when the board is sketched
    def set_sketched_value(self, value):
        self.sketched_value = str(value) if value != 0 else ""

    # draws a cell
    def draw(self):
        if self.is_preset:
            color = (0, 0, 0)
        else:
            color = (125, 125, 125)
        num_font = pygame.font.Font(None, 100)
        num_surf = num_font.render(str(self.value), 0, color)
        num_rect = num_surf.get_rect(center=(self.col * 100 + 50, self.row * 100 + 50))
        self.screen.blit(num_surf, num_rect)