import players
from chess_AI import InitializeAI
from players import Player
import chess


def whose_move(human, cpu, area):
    """ Determine whose turn it is to move in the game """
    board_move = area.turn # Bool. If White's turn to move, returns True
    if board_move == human.bool_color:
        return "human"
    else:
        return "cpu"

def human_move(human, area):
    """
    Function to track human moves
    human (players.Player) = human player
    area (chess.Board()) = Playing board
    Return
    ------
    Move made by player
    """
    while True:  # while loop to test for legality of moves
        move = input("Input move for Player 1: ")
        try:
            return area.push_san(move)  # This function is great because it only allows legal moves
        except ValueError:  # Catch if move is illegal
            print("ILLEGAL MOVE")

def cpu_move(cpu, area):
    """

    cpu (stockfish.Stockfish()) = AI player
    area (chess.Board()) = Playing board
    Returns
    -------
    Move made by cpu
    """
    # Unlike before, I'm not worried about Stockfish returning an illegal move
    move = cpu.engine.get_best_move() # This returns a string in UCI formatting
    return area.push_uci(move)  # This function is great because it only allows legal moves

if __name__ == "__main__":
    board = chess.Board()
    pathname = "/Users/samdawley/Downloads/stockfish_15_linux_x64_bmi2/stockfish_15_src/src/stockfish"
    board = chess.Board()
    cpu = players.Player(0, 0, 0)
    cpu.InitializeStockfish() # Set the engine of the cpu to be Stockfish
    InitializeAI(cpu.engine, board) # This must be done before the cpu can make any moves
    cpu_move(cpu.engine, board)
    print("Lo hicimos!")
