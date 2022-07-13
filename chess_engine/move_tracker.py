import chess
from stockfish import Stockfish
from players import Player

def whose_move(p1: Player, p2: Player, area: chess.Board) -> int:
    """ Determine whose turn it is to move in the game """
    if area.turn == p1.bool_color:
        return p1.color
    else:
        return p2.color

def UCI_to_san(area: chess.Board(), move: str) -> chess.Move:
    """
    Convert UCI move to standard algebraic notation.
    Assumes move is a string in UCI format.
    Returns a string in algebraic notation.
    """
    # Get initial and final squares from UCI representation
    from_square, to_square = chess.parse_square(move[:2]), chess.parse_square(move[2:])
    # Convert string to type chess.Move
    uci_move = chess.Move(from_square, to_square)
    return area.san(uci_move)

def get_stockfish_evaluation(engine: Stockfish) -> str:
    """
    Evaluate board to determine which color is at an advantage. Assumes that engine is initialized to board.

    Returns a dictionary that looks something like
    {"type":"cp", "value":12} <-- cp == centipawn (unit of advantage)
    or {"type":"mate", "value":-3} <-- mate in 3 from current position
    """
    adv = engine.get_evaluation()
    if adv["type"] == "cp":
        if adv["value"] > 0: # Add a plus sign to positive advantages
            print(f"Current board evaluation: +{adv['value'] / 100}")
        else:
            print(f"Current board evaluation: {adv['value'] / 100}")
        return adv["value"]
    elif adv["type"] == "mate":
        print(f"A checkmate is looming!")
        return adv["value"]

def human_move(human: Player, area: Player) -> str:
    """ Function which pushes and tracks moves made by human """
    while True:  # while loop to test for legality of moves
        move = input(f"Input move for {human.color}: ")
        try:
            area.push_san(move) # This function is great because it only allows legal moves
            print(f"{human.color} plays {move}")
            if area.is_check():
                print(f"The king is in check!")
            return move
        except ValueError:  # Catch if move is illegal
            print("ILLEGAL MOVE")

def cpu_move(cpu: Player, area: chess.Board) -> str:
    """
    Function which pushes and tracks moves made by AI.
    Automatically selects best possible move as predicted by the computer
    """
    # Unlike before, I'm not worried about Stockfish returning an illegal move
    print(f"{cpu.color} is thinking...")
    move = cpu.engine.get_best_move() # This returns a string in UCI formatting
    print(f"{cpu.color} plays {UCI_to_san(area, move)}")
    area.push_uci(move)
    if area.is_check():
        print(f"The king is in check!")
    return move

if __name__ == "__main__":
    ...

