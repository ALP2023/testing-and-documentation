The following is a documentation of bugs identified.

1. Not PEP8 naming standard:
def _check_rows(board, player):
def _check_columns(board, player):
def _check_diagonals(board, player):

2. def main(): 

    while moves < 9:
        row, col = map(int, input(f"Player {current_player}, enter row and column (0-2) separated by space: ").split())

Error raised:
__exception__ = {tuple: 3} (<class 'ValueError'>, ValueError('not enough values to unpack (expected 2, got 1)'), <traceback object at 0x000002C3DE8A70C0>)
 0 = {type} <class 'ValueError'>
 1 = {ValueError} not enough values to unpack (expected 2, got 1)
 2 = {traceback} <traceback object at 0x000002C3DE8A70C0>
 __len__ = {int} 3
board = {list: 3} [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
current_player = {str} 'X'
moves = {int} 0
results = {list: 0} []