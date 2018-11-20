# Version 1 of Conway's game of life in Python

import random
import time
import os

random.seed()

board = []

def initialize_board(starting_board):
    for row in range(56):
        init_line = []
        for col in range(192):
            if random.randint(0,1) == 1:
                init_line.append('+')
            else:
                init_line.append(' ')
        starting_board.append(init_line)
    return starting_board


def print_board(game_board):
    os.system('cls')
    print('\n')
    print('-----------------------------------------------------------------')
    print()
    for row in range(56):
        for col in range(192):
            print(game_board[row][col], end = '')
        print()
    print()
    print('-----------------------------------------------------------------')
    print('\n')
    pass


def conway_rules(game_board):
    '''Any live cell with fewer than two live neighbors dies.
    Any live cell with two or three live neighbors lives on.
    Any live cell with more than three neighbors dies.
    Any dead cell with exactly three live neighbors lives on.'''
    # First check for neighbors
    for row in range(56):
        for col in range(192):
            num_of_neighbors = 0

            # This whole thing needs to be in try/except sections cause of index errors
            try:
                if game_board[row][col - 1] == '+':
                    num_of_neighbors += 1
            except IndexError:
                pass

            try:
                if game_board[row][col + 1] == '+':
                    num_of_neighbors += 1
            except IndexError:
                pass

            try:
                if game_board[row - 1][col] == '+':
                    num_of_neighbors += 1
            except IndexError:
                pass

            try:
                if game_board[row + 1][col] == '+':
                    num_of_neighbors += 1
            except IndexError:
                pass

            try:
                if game_board[row - 1][col - 1] == '+':
                    num_of_neighbors += 1
            except IndexError:
                pass

            try:
                if game_board[row - 1][col + 1] == '+':
                    num_of_neighbors += 1
            except IndexError:
                pass

            try:
                if game_board[row + 1][col - 1] == '+':
                    num_of_neighbors += 1
            except IndexError:
                pass

            try:
                if game_board[row + 1][col + 1] == '+':
                    num_of_neighbors += 1
            except IndexError:
                pass

            # Now check for rule 1
            if game_board[row][col] == '+' and num_of_neighbors < 2:
                game_board[row][col] = ' '

            # Check for rule 3 (rule 2 requires no changes)
            if game_board[row][col] == '+' and num_of_neighbors > 3:
                game_board[row][col] = ' '

            # Check for rule 4
            if game_board[row][col] == ' ' and num_of_neighbors == 3:
                game_board[row][col] = '+'

    return game_board

board = initialize_board(board)
print_board(board)

for i in range(500):
    board = conway_rules(board)
    print_board(board)
    time.sleep(0.4)