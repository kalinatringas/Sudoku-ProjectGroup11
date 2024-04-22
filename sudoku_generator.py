
import math,random

class SudokuGenerator:
	
    def __init__(self, row_length, removed_cells):
        row_length = 9   
	removed_cells = 0
        self.row_length = row_length 
        self.removed_cells = removed_cells 
        self.board = [[0]] * row_length for _ in range(row_length)
    
   def __init__(self, row_length = 9, removed_cells = 30):
	self.row_length = row_length
	self.removed_cells = removed_cells
	self.board = [[0]] * row_length for _ in range(row_length)]
	self.box_length = int(math.sqrt(row_length))
	self.fill_values()
	    

    def get_board(self):
        return self.board

	
    def print_board(self):

        for i in range(self.row_length):
            for j in range(self.row_length):

    def print_board(self):
        for row in self.board:
            print(" ".join(str(num) for num in row))

	
    def valid_in_row(self, row, num):
	    return num not in self.board[row]

	
    def valid_in_col(self, col, num):
	    for row in self.board:
		    if row[col] == num:
			    return False
		return True
	
def valid_in_col(self, col, num):
	return all(self.board[row][col] != num for row in range(self.row_length))


    def valid_in_box(self, row_start, col_start, num):
	    for i in range(3):
		    for j in range(3):
			    if self.board[row_start + i][col_start + j] == num:
				    return False
		return True 


    def is_valid(self, row, col, num):
	return self.valid_in_row(row, num) and \
               self.valid_in_col(col, num) and \
               self.valid_in_box(row - row % 3, col - col % 3, num)

    def is_valid(self, row, col, num):
        return ((self.valid_in_row(row, num)) and
                (self.valid_in_col(col, num)) and
                self.valid_in_box(row - row % 3, col - col % 3, num))


    def fill_box(self, row_start, col_start):
	nums = random.sample(range(1, 10), 9)
	for i in range(3):
		for j in range(3):
			self.board[row_start + i][col_start + j] = nums.pop()

    def fill_box(self, row_start, col_start):
        nums = list(range(1, self.box_length + 1))
        random.shuffle(nums)
        for i in range(3):
            for j in range(3):
                self.board[row_start + i][col_start + j] = nums.pop()


    def fill_diagonal(self):
        for i in range(0, self.row_length, self.box_length):
            self.fill_box(i, i)


    def fill_remaining(self, row, col):
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
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)



    def remove_cells(self):
	for _ in range(self.removed_cells):
		row = random.randint(0, self.row_length - 1)
		col = random.randint(0, self.row_length - 1)
		self.board[row][col] = 0
        pass

    def remove_cells(self):
        count = self.removed_cells
        while count > 0:
            row = random.randint(0, self.row_length - 1)
            col = random.randint(0, self.row_length - 1)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                count -= 1

def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board

=======

import math
import random

class SudokuGenerator:

	
    def __init__(self, row_length = 9, removed_cells = 30):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0] * row_length for _ in range(row_length)]
        self.box_length = int(math.sqrt(row_length))
        self.fill_values()



    def print_board(self):
        for row in self.board:
            print(" ".join(str(num) for num in row))

	
    def valid_in_col(self, col, num):
        return all(self.board[row][col] != num for row in range(self.row_length))
    

    def is_valid(self, row, col, num):
        return ((self.valid_in_row(row, num)) and
                (self.valid_in_col(col, num)) and
                self.valid_in_box(row - row % 3, col - col % 3, num))


    def fill_box(self, row_start, col_start):
        nums = list(range(1, self.box_length + 1))
        random.shuffle(nums)
        for i in range(3):
            for j in range(3):
                self.board[row_start + i][col_start + j] = nums.pop()


    def remove_cells(self):
        count = self.removed_cells
        while count > 0:
            row = random.randint(0, self.row_length - 1)
            col = random.randint(0, self.row_length - 1)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                count -= 1

>>>>>>> 132a72528b6782d60b0f0e75213a625a0e6e5fcc



"""
import math
import random

class SudokuGenerator:
    def __init__(self, row_length=9, removed_cells=30):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0] * row_length for _ in range(row_length)]
        self.box_length = int(math.sqrt(row_length))
        self.fill_values()

    def get_board(self):
        return self.board

    def print_board(self):
        for row in self.board:
            print(" ".join(str(num) for num in row))

    def valid_in_row(self, row, num):
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        return all(self.board[row][col] != num for row in range(self.row_length))

    def valid_in_box(self, row_start, col_start, num):
        for r in range(3):
            for c in range(3):
                if self.board[row_start + r][col_start + c] == num:
                    return False
        return True

    def is_valid(self, row, col, num):
        return (self.valid_in_row(row, num) and
                self.valid_in_col(col, num) and
                self.valid_in_box(row - row % 3, col - col % 3, num))

    def fill_box(self, row_start, col_start):
        nums = list(range(1, 10))
        random.shuffle(nums)
        for i in range(3):
            for j in range(3):
                self.board[row_start + i][col_start + j] = nums.pop()

    def fill_diagonal(self):
        for i in range(0, self.row_length, self.box_length):
            self.fill_box(i, i)

    def fill_remaining(self, row, col):
        if col >= self.row_length and row < self.row_length - 1:
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
        self.fill_diagonal()
        self.fill_remaining(0, 0)  # Start from the first cell after diagonal

    def remove_cells(self):
        count = self.removed_cells
        while count > 0:
            row = random.randint(0, self.row_length - 1)
            col = random.randint(0, self.row_length - 1)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                count -= 1

def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board

"""
