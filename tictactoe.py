"""
Tic Tac Toe Player
"""

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

#The player function should take a board state as input, and return which player’s turn it is (either X or O).
def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #In the initial game state, X gets the first move. Subsequently, the player alternates with each additional move.
    if board == initial_state():
        return X
    else: #Any return value is acceptable if a terminal board is provided as input (i.e., the game is already over).
        x_count = 0
        o_count = 0
        for row in board:
            for cell in row:
                if cell == X:
                    x_count += 1
                elif cell == O:
                    o_count += 1
        if x_count > o_count:
            return O
        else:
            return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #Each action should be represented as a tuple (i, j) where i corresponds to the row of the move (0, 1, or 2) and j corresponds to which cell in the row corresponds to the move (also 0, 1, or 2).
    # #Possible moves are any cells on the board that do not already have an X or an O in them.
    # Any return value is acceptable if a terminal board is provided as input.
    possible_moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_moves.add((i, j))
    return possible_moves

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #if action is not a valid action for the board, your program should raise an exception.
    # The returned board state should be the board that would result from taking the original input board, and letting the player whose turn it is make their move at the cell indicated by the input action.
    # Importantly, the original board should be left unmodified: since Minimax will ultimately require considering many different board states during its computation. This means that simply updating a cell in board itself is not a correct implementation of the result function. You’ll likely want to make a deep copy of the board first before making any changes.
    #print("action",action)
    if action not in actions(board):
        print("action",action)
        raise Exception("Invalid move")
    else:
        new_board = [[cell for cell in row] for row in board]
        new_board[action[0]][action[1]] = player(board)
        return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #If the X player has won the game, your function should return X. If the O player has won the game, your function should return O.
    
    # One can win the game with three of their moves in a row horizontally, vertically, or diagonally.
    # You may assume that there will be at most one winner (that is, no board will ever have both players with three-in-a-row, since that would be an invalid board state).
    # If there is no winner of the game (either because the game is in progress, or because it ended in a tie), the function should return None.
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]
    return None

    
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #If the game is over, either because someone has won the game or because all cells have been filled without anyone winning, the function should return True.
    #Otherwise, the function should return False if the game is still in progress.
    if winner(board) is not None:
        return True
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    #If X has won the game, the utility is 1. If O has won the game, the utility is -1. If the game has ended in a tie, the utility is 0.
    # You may assume utility will only be called on a board if terminal(board) is True.
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
    #The move returned should be the optimal action (i, j) that is one of the allowable actions on the board. If multiple moves are equally optimal, any of those moves is acceptable.
    # If the board is a terminal board, the minimax function should return None.
    if terminal(board):
        return utility(board)

    best_move = None  # Initialize best_move

    if player(board) == X:  # Maximizing player
        v = -math.inf
        for action in actions(board):
            # Get the minimax value of the resulting board, only return the score here
            score = minimax(result(board, action))  # Get score from recursion
            if isinstance(score, tuple):
                
                score = score[0]  # If score is a tuple (score, move), extract the score
                
            if score > v:
                v = score
                best_move = action  # Store the best action
    else:  # Minimizing player
        v = math.inf
        for action in actions(board):
            # Get the minimax value of the resulting board, only return the score here
            score = minimax(result(board, action))  # Get score from recursion
            if isinstance(score, tuple):
                score = score[0]  # If score is a tuple (score, move), extract the score

            if score < v:
                v = score
                best_move = action  # Store the best action
                
    # Return the score during recursion and the best move at the top level

    if best_move is not None:
        return best_move  # At the top level, return both score and move
    return v  # If no move is available, return the score
