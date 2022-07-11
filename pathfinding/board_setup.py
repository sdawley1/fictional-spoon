"""
A* pathfinding algorithm for moving pieces across board
"""
from a_star import Astar, Node
import chess
import numpy as np

def board_to_array(fen) -> list:
    """
    Generate numpy array to represent chess board from FEN representation
    :param fen: (str) FEN representation of board
    :return: numpy array representing board
    """
    # First, generate numpy array
    # If piece present in that position, array[row][col] = 1
    # Otherwise, array[row][col] = 0
    area = np.zeros((8, 8))
    board = chess.BaseBoard(board_fen=fen).piece_map() # Returns dict of int:chess.Piece()
    # Iterate through all occupied spaces on board
    # If a piece occupies the position on the board, change area[row][col] from 0 to 1
    for square, piece in board.items():
        row, col = divmod(square, 8)
        area[row][col] = 1
    return area

def uci_to_coords(move, move_class=False):
    """
    Convert UCI representation of a move to coordinate for an array
    :param move: (str) move being made. MUST BE UCI FORM
    :param move_class: (bool) If move is chess.Move() class already
    :return: Returns tuples of (x, y) for initial and final positions given a move
    """
    # Get initial and final squares from UCI representation
    if not move_class:
        # chess.parse_square(str) returns an integer which represents a square on the board
        from_square, to_square = chess.parse_square(move[:2]), chess.parse_square(move[2:])
        return divmod(from_square, 8), divmod(to_square, 8)
    else: # If we're passing through chess.Move() objects, skip the middle man
        return divmod(move.from_square, 8), divmod(move.to_square, 8)

def board_path(array, uci_move):
    """
    Get path from start square to end square on chess board using A* pathfinding algorithm
    :param array: (numpy.array()) Array representing positions of pieces on chess board
    :param uci_move: (str) UCI representation of chess move to be made
    """
    initial, final = uci_to_coords(uci_move)  # returns coords of initial and final points
    start_square, end_square = Node(None, (initial[0], initial[1])), Node(None, (final[0], final[1]))
    return Astar(array, start_square, end_square)

if __name__ == "__main__":
    f = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
    # Setup board
    area = board_to_array(f)
    # UCI move
    move1 = "d3d6"
    # Get path from A* algorithm
    path = board_path(area, move1)
    print(area)
    print(path)

