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
    # List of random FEN strings for testing
    rf = [
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR",
        "2n1K3/1N3N2/3P3p/2P1P3/1pr5/1pp2p2/4k3/1b1R4",
        "1K4k1/7r/1p3pBp/BP6/b1p2R2/2q5/2p5/4R1N1",
        "2n1R1K1/5p1P/pPB5/2p5/p4Pp1/3kB3/3P4/1N6",
        "7k/1P6/1B3R2/3p4/1b2b3/Q7/p1R1BKpP/1q4n1",
        "7R/b1r1B3/1p1p4/1p1q4/P1k2p1p/8/P3P3/5Kn1",
        "5r2/1P3p2/1Kp1r3/1R1P1Np1/8/2p4k/np1P3P/8",
        "1b4Rr/2pRKP1B/7n/4P2k/P7/Q2P3b/1n6/8",
        "2k3N1/2n1P2B/P3p3/8/3rp1P1/p5P1/1p2P2R/5K2",
        "6BK/4b3/P7/2R1P3/2Rp3p/1p2k3/NP4pP/4r"
    ]
    # Setup board
    area = board_to_array(rf[4])
    # UCI move
    move1 = "b1g4"
    # Get path from A* algorithm
    path = board_path(area, move1)
    print(area)
    print(path)

