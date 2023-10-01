import unittest

from tic_tac_toe import initialize_board, is_win, tally_wins, valid_input

class TestTicTacToe(unittest.TestCase):

    def test_initialize_board_creates_empty_board(self):
        """Test that initialize_board function returns an empty 3x3 board."""
        self.assertEqual(initialize_board(), [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])

    def test_is_win_identifies_row_win(self):
        """Test that is_win function correctly identifies wins in rows."""
        board_row_win = [['X', 'X', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertTrue(is_win(board_row_win, 'X'))

    def test_is_win_identifies_column_win(self):
        """Test that is_win function correctly identifies wins in columns."""
        board_column_win = [['X', ' ', ' '], ['X', ' ', ' '], ['X', ' ', ' ']]
        self.assertTrue(is_win(board_column_win, 'X'))

    def test_is_win_identifies_diagonal_win(self):
        """Test that is_win function correctly identifies wins in diagonals (corners of 3x3 grid)."""
        board_diagonal_win = [['X', ' ', ' '], [' ', 'X', ' '], [' ', ' ', 'X']]
        self.assertTrue(is_win(board_diagonal_win, 'X'))

    def test_tally_wins_counts_correct_number_of_wins(self):
        """Test that tally_wins function correctly counts the number of wins."""
        results = [True, False, True]
        self.assertEqual(tally_wins(results), 2)

    def test_valid_input(self):
        """Test that a valid user input doesn't raise an error."""
        self.assertTrue(valid_input("0 2"))

    def test_invalid_pattern_double(self):
        """Test that an invalid user input of two valid integers without a space between raises an error."""
        self.assertFalse(valid_input("02"))

    def test_invalid_pattern_single(self):
        """Test that an invalid user input of a single integer raises an error."""
        self.assertFalse(valid_input("0"))

    def test_invalid_integers(self):
        """Test that an invalid user input of two integers outside the range of 0-2 raises an error."""
        self.assertFalse(valid_input("3 4"))

    def test_invalid_string(self):
        """Test that an invalid user input of string values raises an error."""
        self.assertFalse(valid_input("a b"))


# This allows running the tests by running the script
if __name__ == '__main__':
    unittest.main()

