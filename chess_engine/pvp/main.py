#!/usr/bin/python3

import chess
from gameplay import GameplayLoop
import numpy as np
import players

if __name__ == "__main__":
    # Establish players with 0-0 records
    p1 = players.Player(True, 0, 0)
    p2 = players.Player(False, 0, 0)

    while True:
        # Establish new board and initialize Stockfish
        area = chess.Board()

        # Gameplay loop
        termination, winner, result = GameplayLoop(p1, p2, area)
        if result is None:
            break

        # Add wins/losses to players' records
        p1.add_win() if winner else p2.add_win()
        p2.add_loss() if winner else p1.add_loss()

        # Print results
        print()
        victor, victor_color = "Player 1" if winner else "Player 2", p1.color if winner else p2.color
        if winner:
            print(f"{victor} ({victor_color}) wins! The score is {p1.wins}-{p1.losses}")
        else:
            print(f"The game ended in a draw! The score is {p1.wins}-{p1.losses}")

        # Restarting game loop
        dec = input("Would you like to play again? (y/n) ")
        if dec == "n":
            break
