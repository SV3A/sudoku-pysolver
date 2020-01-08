"""
Module for solving sudokus using backtracking.
"""
from math import floor
from time import sleep


def print_board(board):
    """
    Printes the sudoku board that is implemented as a 1D list.
    """

    line = "".join("-"*29)  # divider line

    for i in range(9):
        if (i == 0 or i == 3 or i == 6):
            print(line)

        j = i*9  # line start index
        print(board[j:j+3], board[j+3:j+6], board[j+6:j+9])

    print(line, "\n")


def _check_if_valid(num, seq_idx, board):
    """
    Check for a given unfilled entry whether a proposed number already appears
    in the particular row, column, and 3x3 box.
    """

    # Determine 2D indices from sequential index
    i = floor(seq_idx/9)
    j = seq_idx % 9

    # Check row
    if (num in board[i*9:i*9+9]):
        return False

    # Check column
    if (num in board[j::9]):
        return False

    # Check 3x3 box
    box = []

    # Determine start index
    start_i = floor(i/3)*3
    start_j = floor(j/3)*3
    start_idx = start_i*9 + start_j

    # Build list containing box entries and check
    for r in range(3):
        for k in range(3):
            box.append(board[start_idx+k])
        start_idx += 9

    if (num in box):
        return False

    return True


def _find_unfilled(board):
    """
    Finds the first empty (unfilled) entry in the board and returns its
    sequential index.
    """

    for i in range(9):
        for j in range(9):
            idx = i*9+j
            if board[idx] == 0:
                return idx

    # If no unfilled entries are left, return special number to halt
    return 9999


def solve_board(board, debug=False):
    """
    Main function to solve sudoku boards (implemented as 1D list of length 81).
    The function is called recursively.
    """

    if debug:
        print(chr(27) + "[2J")
        print_board(board)
        sleep(1.2)

    # Obtain unfilled entry to try to solve
    unfil_idx = _find_unfilled(board)

    # Base case: Check if entire board has been solved
    if unfil_idx == 9999:
        return True

    # Try numbers 1-9
    for n in range(1, 10):
        if (_check_if_valid(n, unfil_idx, board)):

            # Update unfilled entry tentatively
            board[unfil_idx] = n

            # Make recursive call with the guess above
            if solve_board(board, debug):
                return True

            # If the proceeding recursion returned False the current guess for
            # this level (or previous guesses) must be wrong.  Thus we try a
            # different number for this location (or if n = 9, the current
            # location is set to 0 and we proceed to backtrack)
            board[unfil_idx] = 0

    # At this level all has failed, thus we backtrack by returning False
    return False


if __name__ == '__main__':
    # Example
    board = [2, 0, 3, 0, 0, 0, 7, 0, 4,
             0, 9, 1, 2, 7, 4, 5, 0, 3,
             0, 6, 7, 3, 5, 9, 2, 0, 1,
             7, 0, 0, 6, 0, 3, 0, 4, 5,
             5, 3, 4, 0, 1, 7, 6, 2, 8,
             0, 8, 0, 0, 2, 0, 9, 0, 7,
             9, 1, 0, 5, 3, 6, 4, 7, 2,
             3, 4, 5, 0, 9, 0, 0, 0, 6,
             0, 0, 2, 0, 0, 1, 0, 0, 9]

    print("Unsolved board:")
    print_board(board)

    solve_board(board)
    # solve_board(board, debug=True)

    print("Solution:")
    print_board(board)
