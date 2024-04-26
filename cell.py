import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False
        self.sketched_value = 0

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        x = self.col * (self.screen.get_width() // 9)
        y = self.row * (self.screen.get_height() // 9)
        rect = pygame.Rect(x, y, self.screen.get_width() // 9, self.screen.get_height() // 9)
        pygame.draw.rect(self.screen, (255, 255, 255), rect)  # White background
        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), rect, 3)  # Red outline if selected
        else:
            pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)  # Black outline

        font = pygame.font.Font(None, 40)
        if self.value != 0:  # Draw the cell's value
            text = font.render(str(self.value), True, (0, 0, 0))
            self.screen.blit(text, (x + 20, y + 20))
        elif self.sketched_value != 0:  # Draw the sketched value
            text = font.render(str(self.sketched_value), True, (0, 0, 255))
            self.screen.blit(text, (x + 5, y + 5))
