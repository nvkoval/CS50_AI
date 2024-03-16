"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    sum_EMPTY = sum([row.count(EMPTY) for row in board])
    if sum_EMPTY != 0 and sum_EMPTY % 2 == 0:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = deepcopy(board)
    if action not in actions(board):
        raise Exception("This is not a valid action")
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    num_col = len(board[0])

    principal_diag = []
    for i in range(len(board)):
        principal_diag.append(board[i][i])

    diag = []
    for i in range(len(board)):
        diag.append(board[i][num_col - i - 1])

    for player in (X, O):
        for row in board:
            if row.count(player) == num_col:
                return player

        board_transpose = list(zip(*board))
        for row in board_transpose:
            if row.count(player) == num_col:
                return player

        if (principal_diag.count(player) == num_col
                or diag.count(player) == num_col):
            return player

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) or not actions(board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if board == initial_state():
        return (1, 1)

    def max_value(board):
        best_value, optimal_action = -math.inf, None
        if terminal(board):
            return utility(board), optimal_action
        else:
            for action in actions(board):
                new_value = min_value(result(board, action))[0]
                new_value = max(new_value, best_value)
                if new_value == 1:
                    return new_value, action
                if new_value != best_value:
                    best_value = new_value
                    optimal_action = action

            return best_value, optimal_action

    def min_value(board):
        best_value, optimal_action = math.inf, None
        if terminal(board):
            return utility(board), optimal_action
        else:
            for action in actions(board):
                new_value = max_value(result(board, action))[0]
                new_value = min(new_value, best_value)
                if new_value == -1:
                    return new_value, action
                if new_value != best_value:
                    best_value = new_value
                    optimal_action = action

            return best_value, optimal_action

    if terminal(board):
        return None

    if player(board) == X:
        return max_value(board)[1]
    else:
        return min_value(board)[1]
