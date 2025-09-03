"""
Tic Tac Toe Player
"""
import copy
import math

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
    # makes the sum of X s and O s
    # if X > O, X is next
    # else O is next
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    if x_count > o_count:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # create an empty set to add possible moves
    set = set()

    for i in range(3):
        for j in range(3):
            # check if a certain position is empty by comparing it to None
            if (board[i][j] is None):
                set.add((i, j))
    return set

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # this function takes a board and an action (a move/tuple (i,j)) and returns a new board state
    # raise exception, if action is not valid move on the board
    if action not in actions(board):
        raise ValueError("Invalid action")

    # using deepcopy so it doesn't make a shallow copy of the list
    # a shallow copy means it can lead to unintended modifications of the original board
    new_board = copy.deepcopy(board)
    # safer for nested structures

    # get current player, determined by player(board) function
    current_player = player(board)

    # define action
    i, j = action
    # update new board with current action by assigning a value to it
    new_board[i][j] = current_player

    # returns a new board state after the current_player makes that move
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # iterates through all the rows to check if all cells are the same and not empty (None)
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]

    # same as rows
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] and board[0][column] is not None:
            return board[0][column]

    # same as rows and collumns, but diagonally
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    # if a winner is found, it returns X or O
    # else returns None and the code goes on
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # checks if there's a winner
    if winner(board) is not None:
        # return True means the game is over, return False means the game continues
        return True

    # checks if there are empty cells
    # if not and there is no winner, results in tie
    for i in range(3):
        for j in range(3):
            # check if a certain position is empty by comparing it to None
            if (board[i][j] is None):
                # return True means the game is over, return False means the game continues
                return False

    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # call utility on a board only if terminal(board) is full, if the game ended
    if terminal(board) is True:
        utility(board)

    # if game ended in a tie
    if winner(board) is None:
        return 0
    elif winner(board) == 'X':
        return 1
    else:
        return -1

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # The Minimax algorithm is a decision-making algorithm used in game theory
    # to minimize the possible loss for a worst-case (maximum loss) scenario

    # first, checks if the game is already over
    # if so, no move is possible
    if terminal(board):
        return None

    # Determine whose turn it is (X or O)
    current_player = player(board)

    # initialize best_move with None
    best_move = None
    # initializes best_score to negative infinity for the maximizing player ('X')
    # and positive infinity for the minimizing player ('O')
    best_score = -float('inf') if current_player == 'X' else float('inf')

    # Iterate through all possible moves on the 3x3 board
    for i in range(3):
        for j in range(3):
            # Check if the current cell is empty
            if board[i][j] is None:
                # Simulate making this move for the current player
                board[i][j] = current_player

                # Recursively calculate the score for this move:
                # If current player is X, we want to minimize opponent's best outcome
                # If current player is O, we want to maximize opponent's worst outcome
                if current_player == 'X':
                    score = min_value(board)
                else:
                    score = max_value(board)

                # Undo the simulated move to maintain board state
                board[i][j] = None

                # Update the best move based on the score:
                # For X (maximizing player), we want the highest score
                # For O (minimizing player), we want the lowest score
                if current_player == 'X':
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
                else:
                    if score < best_score:
                        best_score = score
                        best_move = (i, j)

    # Return the best move found (coordinates i,j)
    return best_move

# max_value() for X and min_value() for O
# when X plays, it wants to maximize its chances of winning
# when O plays, it wants to minimize X's chances of winning
# based on utility, for X it's +1. for O it's -1

def max_value(board):
    """Calculate the maximum possible score for the maximizing player (X)"""
    # If game is over, return the utility value
    if terminal(board):
        return utility(board)

    # Initialize worst possible score for maximizer
    worst_possible_score_x = -float('inf')

    # Check all possible moves
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                # Simulate X's move
                board[i][j] = 'X'
                # Recursively get the minimum value opponent could get
                # X anticipating O's optimal response (which is to minimize X's score)
                worst_possible_score_x = max(worst_possible_score_x, min_value(board))
                # Undo the move
                board[i][j] = None
    return worst_possible_score_x

def min_value(board):
    """Calculate the minimum possible score for the minimizing player (O)"""
    # If game is over, return the utility value
    if terminal(board):
        return utility(board)

    # Initialize worst possible score for minimizer
    worst_possible_score_O = float('inf')

    # Check all possible moves
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                # Simulate O's move
                board[i][j] = 'O'
                # Recursively get the maximum value opponent could get
                # O anticipating X's optimal response (which is to maximize O's score)
                worst_possible_score_O = min(worst_possible_score_O, max_value(board))
                # Undo the move
                board[i][j] = None
    return worst_possible_score_O

def explain_move(board):
    move = minimax(board)
    return f"The best move for player {player(board)} is {move}"
