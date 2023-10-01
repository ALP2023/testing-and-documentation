'''A buggy Tic-Tac-Toe game that provides an opportunity to debug code by both reasoning about it and stepping through it in a debugger.

The program has a number of bugs that are introduced one at a time. The goal is to find and fix the bugs.

Ensure you step through this program in an IDE debugger and pdb to understand how the program works and to find the bugs.'''

def initialize_board():
    '''Initialise the game board'''
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    '''Print the game board'''
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def _check_rows(board, player):
    '''Check rows for win condition for a given player.
    Args:
      board(list): 3x3 grid to represent game board
      player(str): Checks for a win for player 'X' or 'O'

    Returns:
      bool: True if wins any row, else False
    '''
    for i in range(3):
        if all([cell == player for cell in board[i]]):  
            return True
    return False

# fix not PEP-8 standard
def _check_columns(board, player):
    '''Check columns for win condition for a given player.
    Args:
        board(list): 3x3 grid to represent game board
        player(str): Checks for a win for player 'X' or 'O'

    Returns:
        bool: True if wins any column, else False
    '''
    for i in range(3):
        if all([board[j][i] == player for j in range(3)]):  
            return True
    return False

def _check_diagonals(board, player):
    '''Check diagonals for win condition for a given player.
    Args:
        board(list): 3x3 grid to represent game board
        player(str): Checks for a win for player 'X' or 'O'

    Returns:
         bool: True if wins any diagonal, else False
    '''
    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_win(board, player):
    '''Check rows, columns, and diagonals for win condition for a given player.
    Args:
        board(list): 3x3 grid to represent game board
        player(str): Checks for a win for player 'X' or 'O'

    Returns:
        bool: True if wins (any rows, column or diagonal), else False
    '''
    return _check_rows(board, player) or _check_columns(board, player) or _check_diagonals(board, player)

def tally_wins(results):
    '''Count the number of wins.
    Args:
        results (list):  a list of wins (bools)

    Returns:
        int: sum of wins
    '''
    return sum(results)

def valid_input(input_str):
    """Checks if user input is valid.

    Args:
        input_str (str): the user input string to be validated.

    Returns:
        bool: True if the input is valid, otherwise False.

    The function checks whether the input string represents a valid move.
    A valid input consist of two integers, in the range of 0 to 2 (inclusive), separated by a single space.
    Any other input format is considered invalid.

    Examples:
        - Valid input: "0 2"
        - Invalid input: "02" (no space), "0" (single integer), "3 4" (out of range),
                        "a b" (non-integer characters)

    Returns True for valid inputs and False for invalid ones.
    """
    try:
        row, col = map(int, input_str.split())
        return row in (0, 1, 2) and col in (0, 1, 2)
    except ValueError:
        return False

def main():
    board = initialize_board()
    current_player = 'X'
    moves = 0
    results = []

    while moves < 9:
        print_board(board)
        user_input = input(f"Player {current_player}, enter row and column (0-2) separated by a space: ")

        if valid_input(user_input):
            row, col = map(int, user_input.split())
            if board[row][col] == ' ':
                board[row][col] = current_player
                win = is_win(board, current_player)
                results.append(win)
                if win:
                    print_board(board)
                    print(f"Player {current_player} wins!")
                    return
                current_player = 'O' if current_player == 'X' else 'X'
                moves += 1
            else:
                print("Cell already occupied! Try again.")
        else:
            print("Invalid input! Please enter two integers between 0 and 2 separated by a space.")

    print_board(board)
    print("It's a draw!")
    print(f"Number of wins during the game: {tally_wins(results)}")


if __name__ == "__main__":
    main()

