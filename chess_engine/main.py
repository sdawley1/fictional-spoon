#!/usr/bin/python3

import chess
import gameplay
import players

if __name__ == "__main__":
    # Establish players
    white = players.Player(chess.WHITE, 0, 0)
    black = players.Player(chess.BLACK, 0, 0)

    while True:
        # Establish new board
        area = chess.Board()

        # Gameplay loop
        termination, winner, result =gameplay.GameplayLoop(white, black, area)
        # Add wins/losses to players' records
        white.add_win() if winner else black.add_win()
        black.add_loss() if winner else white.add_loss()

        # Print results
        print()
        victor, victor_color = "Player 1" if winner else "Player 2", "white" if winner else "black"
        if winner:
            print(f"{victor} ({victor_color}) wins! The score is {white.wins}-{white.losses}")
        else:
            print(f"The game ended in a draw! The score is {white.wins}-{white.losses}")

        # Restarting game loop
        dec = input("Would you like to play again? (y/n) ")
        if dec == "n":
            break
