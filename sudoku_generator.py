import math
import random


class SudokuGenerator:
    # row_length default value: 9 ; removed_cells must be determined using difficulty
    def __init__(self, removed_cells, row_length=9):
        # row_length is always 9
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = []
        self.box_length = int(math.sqrt(row_length))
        # initialize board w zeros...
        for i in range(row_length):
            row = []
            for j in range(row_length):
                row.append(0)
            self.board.append(row)

    def get_board(self):  # 2D list to represent board
        return self.board

    def print_board(self):  # displays board in console
        list = []
        for row in self.board:
            obj = []
            for part in row:
                print(part, end=" ")
                obj.append(part)
            list.append(obj)
            print()
        return list

    def valid_in_row(self, row, num):
        # Returns a Boolean value.
        # Determines if num is contained in the given row of the board.
        for i in self.board[row]:
            if num in self.board[row]:
                return False
            return True

    def valid_in_col(self, col, num):
        # Returns a Boolean value.
        # Determines if num is contained in the given column of the board.
        for row in range(len(self.board)):
            if num == self.board[row][col]:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        # Returns a Boolean value.
        # Determines if num is contained in the 3x3 box from
        # (row_start, col_start) to (row_start+2, col_start+2)
        for i in range(3):
            for j in range(3):
                if self.board[i + row_start][j + col_start] == num:
                    return False
        return True

    def is_valid(self, row, col, num):
        # Returns if it is valid to enter num at (row, col) in the board.
        # This is done by checking the appropriate row, column, and box.
        return (
                self.valid_in_row(row, num) and
                self.valid_in_col(col, num) and
                self.valid_in_box(row - (row % self.box_length), col - (col % self.box_length), num)
        )

    def fill_box(self, row_start, col_start):
        # use unused_in_box to make sure no value is repeated
        # fills with random values
        for i in range(3):
            for j in range(3):
                fill_number = random.randint(1, 9)
                while self.valid_in_box(row_start, col_start, fill_number) == False:
                    fill_number = random.randint(1, 9)
                self.board[row_start + i][col_start + j] = fill_number
        return None

    def fill_diagonal(self):
        # fills three boxes along the diagonal
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)
        return None

    def fill_remaining(self, row, col):
        # provided
        # returns the solution, completed board
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        # calls fill_diagonal and fill_remaining
        # fills the board with values
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        # removes cells
        # randomly generate (row,col), value set to 0
        # only remove a cell once
        while self.removed_cells > 0:
            row = random.randint(0, self.row_length - 1)
            col = random.randint(0, self.row_length - 1)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                self.removed_cells -= 1


# generates a sudoku board with rando the desired ammount of removed cells
def generate_sudoku(removed, size):
    sudoku = SudokuGenerator(removed, size)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board