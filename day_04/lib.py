import numpy as np
from pathlib import Path

BOARD_SIZE = 5


class BingoBoard:

    def __init__(self, board_array):
        self.array = board_array
        self.marked = np.zeros_like(board_array, dtype=bool)

        self.coordinates = dict()
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                value = board_array[i][j]
                self.coordinates[value] = (i, j)

        self.col_totals = np.zeros(BOARD_SIZE)
        self.row_totals = np.zeros(BOARD_SIZE)
        self._wins = False

    def update(self, number):
        if number in self.coordinates:
            i, j = self.coordinates[number]
            self.marked[i, j] = True
            
            self.row_totals[i] += 1
            self.col_totals[j] += 1
            
            if self.row_totals[i] == BOARD_SIZE or self.col_totals[j] == BOARD_SIZE:
                self._wins = True
                self.winning_number = number

    def wins(self):
        return self._wins


class BingoGame:

    def __init__(self, boards):
        self.boards = boards
        self.found = False
        self.product = None

    def update(self, number):
        
        for i, board in enumerate(self.boards):
            board.update(number)
            if board.wins():
                self.found = True
                sum_of_unmarked = np.sum(board.array[~board.marked])
                self.product = sum_of_unmarked * number
                
                print(f'Board {i} wins with number {board.winning_number}')
                print(f'Sum of unmarked numbers: {sum_of_unmarked}')
                print(f'Product: {self.product}')

                break


def file_path(basename):
    return  Path('.') / 'data' / basename


def read_bingo_data(filename):

    with open(filename) as f:
        numbers = parse_numbers(f.readline(), sep=',')

        return parse_boards(f), numbers


def parse_numbers(line, sep=None):
    return list(map(int, line.strip().split(sep)))


def parse_boards(file):
    
    def line_is_empty(line):
        return line.strip() == ''

    boards = []
    board = []
    for line in file:

        is_empty = line_is_empty(line)
        
        if not is_empty:
            row = parse_numbers(line)
            board.append(row)
            continue

        if is_empty and len(board) > 0:
            board_object = BingoBoard(np.array(board))
            boards.append(board_object)
            board = []

    board_object = BingoBoard(np.array(board))
    boards.append(board_object)

    return boards
