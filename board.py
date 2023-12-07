import pygame, sys
from cell import Cell
from constants import *
from sudoku_generator import *

class Board():
    current_cell = Cell(None, None, None, None)

    def __init__(self, difficulty,  width=WIDTH, height=HEIGHT):
        self.width = width  # width is 900 so each box is 90 pix wide
        self.height = height  # height is 900 so each box is 90 pix tall
        self.screen = pygame.display.set_mode((width, height + 150))
        self.difficulty = difficulty

        # generates the values for the sudoku board
        self.board_values = generate_sudoku(difficulty, BOARD_ROWS)
        # for each value in the sudoku board create a matching cell with the same values
        self.cells = [[Cell(self.board_values[i][j], i, j, self.screen) for j in range(9)] for i in range(9)]

    def draw(self, cell_color= (0,0,0)):
        self.screen.fill((255, 255, 255))

        # draw in the cell values
        for i in range(9):
            for j in range(9):
                self.cells[i][j].draw(cell_color)

        for i in range(1, BOARD_ROWS):
            pygame.draw.line(
                self.screen,
                (140, 140, 140),
                (0, i * SQUARE_SIZE),
                (WIDTH, i * SQUARE_SIZE),
                LINE_WIDTH
            )
        # draw vertical lines
        for j in range(1, BOARD_COLS):
            pygame.draw.line(
                self.screen,
                (140, 140, 140),
                (j * SQUARE_SIZE, 0),
                (j * SQUARE_SIZE, HEIGHT),
                LINE_WIDTH

            )
        # draw the darkened lines every 3 rows and columns
        for i in range(0, 10):
            if i % 3 == 0:
                pygame.draw.line(
                    self.screen,
                    (100, 100, 100),
                    (i * SQUARE_SIZE, 0),
                    (i * SQUARE_SIZE, HEIGHT),
                    LINE_WIDTH
                )
                pygame.draw.line(
                    self.screen,
                    (100, 100, 100),
                    (0, i * SQUARE_SIZE),
                    (WIDTH, i * SQUARE_SIZE),
                    LINE_WIDTH
                )
        pygame.display.update()


    def select(self, row, col):
        # loops through the 2D array of cells and returns the selected cell based on user input
        for i in self.cells:
            for cell in i:
                if cell.row == row and cell.col == col:
                    return cell

    # returns the current collumn and cell clicked on by the user
    def click(self, x, y):
        row = y // 80
        col = x // 80
        return row, col

    # draws a circle around box that user selected
    def draw_select(self, curr_cell):
        row = curr_cell.row
        col = curr_cell.col
        x = row * SQUARE_SIZE
        y = col * SQUARE_SIZE
        select_rect = pygame.Rect(y, x, SQUARE_SIZE + 2, SQUARE_SIZE + 2)
        pygame.draw.rect(self.screen, RED, select_rect, 10)

    # clears the value of the current cell
    def clear(self, current_cell):
        current_cell.set_cell_value(0)

    # "sketches" in a value into the current cell
    def sketch_number(self, value, current_cell):
        current_cell.set_sketched_value(value)

    # places the value into the cell
    def place_number(self, value, current_cell):
        current_cell.set_cell_value(value)

    # resets the board to the original values (deletes user input)
    def reset_to_original(self):
        self.cells = [[Cell(self.board_values[i][j], i, j, self.screen) for j in range(9)] for i in range(9)]

    # checks if board if full
    def is_full(self):
        for row in self.cells:
            for cell in row:
                if cell.value == 0:
                    return False
        return True

    # finds first empty cell and returns its row and col as a tuple
    def find_empty(self):
        for row in range(len(self.cells)):
            for col in range(len(self.cells[row])):
                if self.cells[row][col].value == 0:
                    return (row, col)

    def update_board(self):
        # loops through the 2D array of cells and updates the values in the board
        for row in self.cells:
            for cell in row:
                self.board[cell.row][cell.col] = cell.value

    # the following functions are used to check if the board is solved

    @staticmethod
    def solved_row(row):
        for i in range(len(row)):
            for j in range(i + 1, len(row)):
                if row[i] == row[j]:
                    return False
        return True

    @staticmethod
    def solved_col(col):
        for val in col:
            if col.count(val) > 1:
                return False
        return True

    # note: solved_board is a 2D list
    @staticmethod
    def solved_box(solved_board):
        for row_of_box in range(0, 9, 3):
            for col_of_box in range(0, 9, 3):
                temp = set()
                for box_row in range(0, 3):
                    for box_col in range(0, 3):
                        value = solved_board[box_row + row_of_box][box_col + col_of_box]
                        if value in temp:
                            return False
        return True

    def check_board(self):
        # Check if the board is filled
        if self.is_full():
            # Check rows
            for row in self.board_values:
                if not Board.solved_row(row):
                    return False

            # Check columns
            for col in range(9):
                column_values = [self.board_values[row][col] for row in range(9)]
                if not Board.solved_col(column_values):
                    return False

            # Check boxes
            if not Board.solved_box(self.board_values):
                return False

            return True

        return False
