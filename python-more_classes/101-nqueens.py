#!/usr/bin/python3
<<<<<<< HEAD
"""This module solves the nqueen bactracking problem"""
import sys


class Solution:
    def solveNQueens(self, n):
        """Find all solutions to the N-Queens problem.
        Args: n (int) - The size of the chessboard (N).
        Returns: list - A list of solutions, each as a nested list of
                [row, column] positions for each queen.
        """
        solutions = []
        state = []
        self.search(state, solutions, n)
        return solutions

    def is_valid_state(self, state, n):
        """Check if the current state is a valid solution.
        Args: state (list) - A list representing the current state of
                the chessboard.
              n (int) - The size of the chessboard (N).
        Returns: bool - True if the state is a valid solution, False otherwise.
        """
        return len(state) == n

    def get_candidates(self, state, n):
        """Get the valid candidate positions for the next queen placement.
        Args: state (list) - A list representing the current state of the
                chessboard.
              n (int) - The size of the chessboard (N).
        Returns: set - A set of column indices representing the valid
                candidate positions.
        """
        if not state:
            return set(range(n))

        position = len(state)
        candidates = set(range(n))
        for row, col in enumerate(state):
            candidates.discard(col)
            dist = position - row
            candidates.discard(col + dist)
            candidates.discard(col - dist)
        return candidates

    def search(self, state, solutions, n):
        """Recursively search for all valid solutions to the N-Queens problem.
        Args: state (list) - A list representing the current state of the
                chessboard.
              solutions (list) - A list to store the valid solutions.
              n (int) - The size of the chessboard (N).
        """
        if self.is_valid_state(state, n):
            state_string = self.state_to_nested_list(state, n)
            solutions.append(state_string)
            return

        for candidate in self.get_candidates(state, n):
            state.append(candidate)
            self.search(state, solutions, n)
            state.pop()

    def state_to_nested_list(self, state, n):
        """Convert the state representation to a nested list.
        Args: state (list) - A list representing the current state of the
                chessboard.
              n (int) - The size of the chessboard (N).
        Returns: list - A nested list of [row, column] positions for each queen
        """
        answer = []
        for index, value in enumerate(state):
            answer.append([index, value])
        return answer

arg = sys.argv
try:
    arg_1 = int(sys.argv[1])
except (ValueError, TypeError):
    print("N must be a number")
except IndexError:
    print("Usage: nqueens N")
else:
    if arg_1 < 4:
        print("N must be at least 4")
    else:
        NQueen = Solution()
        solution_list = NQueen.solveNQueens(int(sys.argv[1]))
        for solution in solution_list:
            print(solution)
=======
"""Solves the N-queens puzzle.
Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.
Example:
    $ ./101-nqueens.py N
N must be an integer greater than or equal to 4.
Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.
Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """Return a deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return (solution)


def xout(board, row, col):
    """X out spots on a chessboard.
    All spots where non-attacking queens can no
    longer be played are X-ed out.
    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    # X out all forward spots
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    # X out all backwards spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # X out all spots below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # X out all spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # X out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # X out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    # X out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # X out all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle.
    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
