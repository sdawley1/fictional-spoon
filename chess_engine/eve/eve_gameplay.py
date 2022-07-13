"""
Environment vs. Environment chess game
"""

import chess_AI
import chess
from players import Player
import move_tracker

def GameplayLoop(p1: Player, p2: Player, area: chess.Board()) -> tuple:
    """
    Gameplay loop with AI opponent
    Params
    ------
    p1 (players.Player)
    p2 (players.Player)
    area (chess.Board) = Board to play on. Keeps track of pretty much everything
    Returns
    -------
    outcome.termination () = Reason that the game ended
    outcome.winner (bool) = Winner of game (WHITE == True, BLACK == False)
    outcome.result() (str) = Any of "1-0", "0-1", or "1/2-1/2" to denote outcome of game
    """
    # Get ELO of Stockfish to display
    p1_elo = p1.engine.get_parameters()["UCI_Elo"]
    p2_elo = p2.engine.get_parameters()["UCI_Elo"]

    print()
    print("Let the game begin!")
    print(f"PLAYER 1 (ELO: {p1_elo}) will play {p1.color} and PLAYER 2 (ELO: {p2_elo}) will play {p2.color}.")
    print("All desired moves must be written in standard algebraic notation, e.g., 'e4', 'Nc6', or 'Qxf7'.")

    # Establish current outcome of game
    # This variable is updated whenever the end of the while loop is broken
    # i.e., test for termination before another loop begins in the while loop
    outcome = area.outcome()

    # Confirm game
    print()
    if input("Proceed? (y/n): ") == "y":
        pass
    else:
        print("Another day...")
        return None, None, None

    while not outcome:
        # Print playing board
        print()
        print(f"MOVE {area.fullmove_number} ({'WHITE' if area.turn else 'BLACK'})")
        print("---------------")
        print(area)
        print("---------------")
        # Making moves
        if move_tracker.whose_move(p1, p2, area) == p1.color:
            chess_AI.InitializeAI(p1.engine, area)
            move = move_tracker.cpu_move(p1, area)
        else:
            chess_AI.InitializeAI(p2.engine, area)
            move = move_tracker.cpu_move(p2, area)

        # Get board evaluation
        adv = move_tracker.get_stockfish_evaluation(p1.engine)

        # Test termination condition
        outcome = area.outcome()

    # Print final board
    print()
    print("Game over!")
    print("---------------")
    print(area)
    print("---------------")

    # Return results of the match
    return outcome.termination, outcome.winner, outcome.result()


