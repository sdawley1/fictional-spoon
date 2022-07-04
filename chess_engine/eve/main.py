#!/usr/bin/python3

import chess
import numpy as np
import AI_gameplay
import players
from chess_AI import InitializeAI

if __name__ == "__main__":
    # Choose colors for either player
    p1_color = True if np.random.uniform() < 0.5 else False
    # Establish players
    # Human player
    p1 = players.Player(p1_color, 0, 0)
    # Computer player
    p2 = players.Player(not p1_color, 0, 0)
    # Create engines
    p1.InitializeStockfish()
    p2.InitializeStockfish()

    while True:
        # Establish new board and initialize Stockfish
        area = chess.Board()
        # Initialize engines
        InitializeAI(p1.engine, area)
        InitializeAI(p2.engine, area)

        # Gameplay loop
        termination, winner, result = AI_gameplay.AIGameplay(p1, p2, area)
        if result is None:
            break

        # Add wins/losses to players' records
        p1.add_win() if winner else p2.add_win()
        p2.add_loss() if winner else p1.add_loss()

        # Print results
        print()
        victor = "PLAYER 1" if winner else "PLAYER 2"
        if winner or not winner:
            print(f"{victor} wins! The score is {p1.wins}-{p1.losses}")
        else:
            print(f"The game ended in a draw! The score is {p1.wins}-{p1.losses}")

        # Restarting game loop
        dec = input("Would you like to play again? (y/n) ")
        if dec == "n":
            break
