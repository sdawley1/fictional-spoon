"""
A* pathfinding algorithm for moving pieces across board

8/12/2022
BOARD IS CURRENTLY ROTATED pi/2 RADIANS WITH THIS MODEL
I THINK THE LEAST CONFUSING METHOD IS TO ACCOUNT FOR THIS ROTATION SOMEWHERE ELSE IN THE PROJECT
"""
from array import array
from pathfinding.a_star import Astar, Node
import chess
import numpy as np

def board_to_array(fen: str) -> list:
    """
    Generate numpy array to represent chess board from FEN representation
    :param fen: (str) FEN representation of board
    :return: numpy array representing board
    """
    # First, generate numpy array
    # If piece present in that position, array[row][col] = 1
    # Otherwise, array[row][col] = 0
    z = np.zeros((8, 8))
    board = chess.BaseBoard(board_fen=fen).piece_map() # Returns dict of int:chess.Piece()
    # Iterate through all occupied spaces on board
    # If a piece occupies the position on the board, change area[row][col] from 0 to 1
    for square, piece in board.items():
        row, col = divmod(square, 8)
        z[row][col] = 1
    return z

def uci_to_coords(move: str, move_class: bool=False) -> tuple:
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

def board_path(array: array, uci_move: str) -> list:
    """
    Get path from start square to end square on chess board using A* pathfinding algorithm
    :param array: (numpy.array()) Array representing positions of pieces on chess board
    :param uci_move: (str) UCI representation of chess move to be made
    """
    initial, final = uci_to_coords(uci_move)  # returns coords of initial and final points
    start_square, end_square = Node(None, (initial[0], initial[1])), Node(None, (final[0], final[1]))
    return Astar(array, start_square, end_square) # Should test if A* returns None in future

if __name__ == "__main__":
    # List of random FEN strings for testing
    # There are currently 323 lines in the text file
    fens = []
    with open("test_fens.txt", "r") as f:
        fens = [line for line in f.readlines()]
    # Setup board
    area = board_to_array(fens[64])
    # UCI move
    move1, move2 = "b1f8", "g2g8"
    # Get path from A* algorithm
    path = board_path(area, move2)
    print(f"Move: {move2}")
    print(f"Path: {path}")
    # Print area
    # Note the the board is flipped about the x-axis
    for r in area:
        print(r)

