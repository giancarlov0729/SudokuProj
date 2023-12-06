import pygame
from constants import *

class Cell:
    def __init__(self, value, row, col, screen):  # constructor
        self.value = value
        self.sketched_value = None
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):  # set cell value
        self.value = value

    def set_sketched_value(self, value):  # set sketched cell value
        self.sketched_value = value

    def draw(self, color= ((0,0,0)) ):
        # draw cell and inside value
        # if value > 0, display value
        # if value is negative, no value is displayed
        # currently selected cell to be outlined in red
        # sketched cell to be outlined in green
        num_font = pygame.font.SysFont(None, 36)
        if self.value != 0:
            num_surf = num_font.render(str(self.value), 0, color)
            num_rect = num_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            self.screen.blit(num_surf, num_rect)
        elif self.sketched_value is not None:
            print('I AM DRAWING THE SKETCHED VALUE!!')
            num_surf = num_font.render(str(self.sketched_value), 0, PINK)
            num_rect = num_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            self.screen.blit(num_surf, num_rect)

