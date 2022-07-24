"""
A* pathfinding algorithm for moving pieces across board

8/12/2022
BOARD IS CURRENTLY ROTATED pi/2 RADIANS WITH THIS MODEL
I THINK THE LEAST CONFUSING METHOD IS TO ACCOUNT FOR THIS ROTATION SOMEWHERE ELSE IN THE PROJECT
"""
import sys
from array import array
from tabnanny import check
import chess
import numpy as np
sys.path.append("../")
from pathfinding.a_star import Astar, Node
from chess_engine.move_tracker import check_castles_int, check_castles_str


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
        # Check if the player castles
        if check_castles_str(move): # If castles, UCI move = "e1h1", e.g.
            # return tuple for king initial/final positions and rook initial/final positions
            return castles_to_coords(move, move_class)[0], castles_to_coords(move, move_class)[1]
        else:
            # chess.parse_square(str) returns an integer which represents a square on the board
            # This function returns an index on the interval [0, 63] w/ '0' representing the square a1
            from_square, to_square = chess.parse_square(move[:2]), chess.parse_square(move[2:]) 
            return divmod(from_square, 8), divmod(to_square, 8)
    else: # If we're passing through chess.Move() objects, skip the middle man
        if check_castles_int(move):
            # return tuple for king initial/final positions and rook initial/final positions
            return castles_to_coords(move, move_class)[0], castles_to_coords(move, move_class)[1]
        else:
            return divmod(move.from_square, 8), divmod(move.to_square, 8)

def castles_to_coords(move: str, move_class: bool=False) -> tuple:
    """
    Move must be in UCI format
    """
    if not move_class:
        # Castling short for white
        if move[:2] == "e1" and move[2::] == "h1":
            return ((7, 4), (7, 6)), ((7, 7), (7, 5)) # king: (to_square, from_square) & rook: (to_square, from_square)
        # Castling long for white
        elif move[:2] == "e1" and move[2::] == "a1":
            return ((7, 4), (7, 2)), ((7, 0), (7, 3)) # king: (to_square, from_square) & rook: (to_square, from_square)
        # Castling short for black
        elif move[:2] == "e8" and move[2::] == "h8":
            return ((0, 4), (0, 6)), ((0, 7), (0, 5)) # king: (to_square, from_square) & rook: (to_square, from_square)
        # Castling long for black
        elif move[:2] == "e8" and move[2::] == "a8":
            return ((0, 4), (0, 2)), ((0, 0), (0, 3)) # king: (to_square, from_square) & rook: (to_square, from_square)
    else:
        # Castling short for white
        if move.from_square == 4 and move.to_square == 7:
            return ((7, 4), (7, 6)), ((7, 7), (7, 5)) # king: (to_square, from_square) & rook: (to_square, from_square)
        # Castling long for white
        elif move.from_square == 4 and move.to_square == 0:
           return ((7, 4), (7, 2)), ((7, 0), (7, 3)) # king: (to_square, from_square) & rook: (to_square, from_square)
        # Castling short for black
        elif move.from_square == 60 and move.to_square == 63:
            return ((0, 4), (0, 6)), ((0, 7), (0, 5)) # king: (to_square, from_square) & rook: (to_square, from_square)
        # Castling long for black
        elif move.from_square == 60 and move.to_square == 56:
            return ((0, 4), (0, 2)), ((0, 0), (0, 3)) # king: (to_square, from_square) & rook: (to_square, from_square)

## THIS IS THE IMPORTANT FUNCTION ##
def board_path(array: array, uci_move: str, castles: bool=False) -> list:
    """
    Get path from start square to end square on chess board using A* pathfinding algorithm
    :param array: (numpy.array()) Array representing positions of pieces on chess board
    :param uci_move: (str) UCI representation of chess move to be made
    """
    if not castles:
        initial, final = uci_to_coords(uci_move)  # returns coords of initial and final points
        start_square, end_square = Node(None, (initial[0], initial[1])), Node(None, (final[0], final[1]))
        return Astar(array, start_square, end_square) # Should test if A* returns None in future
    else:
        king_initial, king_final, rook_initial, rook_final = uci_to_coords(uci_move)[0], uci_to_coords(uci_move)[1]
        # Get start and end nodes for king
        king_start, king_end = Node(None, (king_initial[0], king_initial[1])), Node(None, (king_final[0], king_final[1]))
        # Get start and end nodes for rook
        rook_start, rook_end = Node(None, (rook_initial[0], rook_initial[1])), Node(None, (rook_final[0], rook_final[1]))
        return [Astar(array, king_start, king_end), Astar(array, rook_start, rook_end)] # Return list of paths

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

