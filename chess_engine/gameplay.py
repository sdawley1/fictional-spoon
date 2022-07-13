"""
"""

from tkinter import Place
from chess import Board
from chess_engine.players import Player


def GameplayLoop(p1: Player, p2: Player, area: Board) -> tuple:
    """
    Gameplay loop
    Params
    ------
    p1 (players.Player) = White
    p2 (players.Player) = Black
    area (chess.Board) = Board to play on. Keeps track of pretty much everything
    Returns
    -------
    outcome.termination () =
    outcome.winner (bool) = Winner of game (white == True, black == False)
    outcome.result() (str) = Any of "1-0", "0-1", or "1/2-1/2" to denote outcome of game
    """

    print()
    print("Let the game begin!")
    print(f"Player 1 will play {p1.color} and Player 2 will play {p2.color}.")
    print("All desired moves must be written in standard algebraic notation, e.g., 'e4', 'Nc6', or 'Qxf7'.")

    # Establish current outcome of game
    # This variable is updated whenever the end of the while loop is broken
    # i.e., test for termination before another loop begins in the while loop
    outcome = area.outcome()
    while not outcome:
        # Keeping track of whose turn it is
        whose_move = area.turn
        # Print playing board
        print()
        print(f"MOVE {area.fullmove_number} ({'white' if whose_move else 'black'})")
        print("---------------")
        print(area)
        print("---------------")
        # Players making moves
        if whose_move:
            while True: # while loop to test for legality of moves
                move = input("Input move for Player 1: ")
                try:
                    area.push_san(move) # This function is great because it only allows legal moves
                    break
                except ValueError: # Catch if move is illegal
                    print("ILLEGAL MOVE")
        else:
            while True: # while loop to test for legality of moves
                move = input("Input move for Player 2: ")
                try:
                    area.push_san(move)
                    break
                except ValueError: # Catch if move is illegal
                    print("ILLEGAL MOVE")

        # Test termination condition
        outcome = area.outcome()

    # Return results of the match
    return outcome.termination, outcome.winner, outcome.result()


