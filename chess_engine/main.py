#!/usr/bin/python3

"""
Script to invoke gameplay
"""
import sys
import chess
import chess_AI
import numpy as np
import players
from eve import eve_gameplay
from pve import pve_gameplay
from pvp import pvp_gameplay
sys.path.append("..")
from pathfinding.board_setup import board_to_array

def main() -> None:
    """ Main function """
    # Randomly choose colors
    p1_color = True if np.random.uniform() < 0.5 else False
    while True:
        const_game = input("Would you like to play pvp, pve, or eve? ")
        # Player versus Player
        if const_game == "pvp":
            p1 = players.Player(p1_color, 0, 0)
            p2 = players.Player(not p1_color, 0, 0)
            break
        # Player versus computer
        elif const_game == "pve":
            p1 = players.Player(p1_color, 0, 0)
            p2 = players.Player(not p1_color, 0, 0)
            # Initialize Stockfish
            p2.InitializeStockfish(elo=1000)
            break
            # Computer versus computer
        elif const_game == "eve":
            p1 = players.Player(p1_color, 0, 0)
            p2 = players.Player(not p1_color, 0, 0)
            # Initialize Stockfish for both computers
            p1.InitializeStockfish(elo=1000)
            p2.InitializeStockfish(elo=1000)
            break

        else:
            print("Must answer with any of 'pvp', 'pve', or 'eve'.")

    while True:
        # Establish chess board and get fen representation
        area = chess.Board()

        # Gameplay loop
        if const_game == "pvp":
            termination, winner, result = pvp_gameplay.GameplayLoop(p1, p2, area)
        elif const_game == "pve":
            # Initialize engine for computer player
            chess_AI.InitializeAI(p2.engine, area)
            termination, winner, result = pve_gameplay.GameplayLoop(p1, p2, area)
        else:
            # Initialize engines for computer players
            chess_AI.InitializeAI(p1.engine, area)
            chess_AI.InitializeAI(p2.engine, area)
            termination, winner, result = eve_gameplay.GameplayLoop(p1, p2, area)

        # Termination
        if result is None:
            break

        # Add wins/losses to players' records
        p1.add_win() if winner else p2.add_win()
        p2.add_loss() if winner else p1.add_loss()

        # Print results
        print()
        victor, victor_color = "Player 1" if winner else "Player 2", "white" if winner else "black"
        if winner:
            print(f"{victor} ({victor_color}) wins! The score is {p1.wins}-{p1.losses}")
        else:
            print(f"The game ended in a draw! The score is {p1.wins}-{p1.losses}")

        # Restarting game loop
        dec = input("Would you like to play again? (y/n) ")
        if dec == "n":
            break

if __name__ == "__main__":
    main()
