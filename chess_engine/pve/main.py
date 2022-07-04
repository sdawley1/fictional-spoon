#!/usr/bin/python3

import chess
import numpy as np
import AI_gameplay
import players
from chess_AI import InitializeAI

if __name__ == "__main__":
    # Choose colors for either player
    human_color = True if np.random.uniform() < 0.5 else False
    # Establish players
    # Human player
    human = players.Player(human_color, 0, 0)
    # Computer player
    cpu = players.Player(not human_color, 0, 0)
    cpu.InitializeStockfish(elo=1000) # Set the cpu engine to be Stockfish

    while True:
        # Establish new board and initialize Stockfish
        area = chess.Board()
        InitializeAI(cpu.engine, area)

        # Gameplay loop
        termination, winner, result = AI_gameplay.AIGameplay(human, cpu, area)
        if result is None:
            break

        # Add wins/losses to players' records
        human.add_win() if winner else cpu.add_win()
        cpu.add_loss() if winner else human.add_loss()

        # Print results
        print()
        victor, victor_color = "Player 1" if winner else "Player 2", "white" if winner else "black"
        if winner:
            print(f"{victor} ({victor_color}) wins! The score is {human.wins}-{human.losses}")
        else:
            print(f"The game ended in a draw! The score is {human.wins}-{human.losses}")

        # Restarting game loop
        dec = input("Would you like to play again? (y/n) ")
        if dec == "n":
            break
