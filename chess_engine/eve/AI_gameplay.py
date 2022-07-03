import move_tracker
import chess_AI

def AIGameplay(p1, p2, area):
    """
    Gameplay loop with AI opponent
    Params
    ------
    human (players.Player) = White
    cpu (players.Player) = Black
    area (chess.Board) = Board to play on. Keeps track of pretty much everything
    Returns
    -------
    outcome.termination () =
    outcome.winner (bool) = Winner of game (white == True, black == False)
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

    print()
    if input("Proceed? (y/n): ") == "y":
        pass
    else:
        print("Another day...")
        return None, None, None

    while not outcome:
        # Print playing board
        print()
        print(f"MOVE {area.fullmove_number} ({'white' if area.turn else 'black'})")
        print("---------------")
        print(area)
        print("---------------")
        # Making moves
        if move_tracker.whose_move(p1, p2, area) == "PLAYER 1":
            chess_AI.InitializeAI(p1.engine, area)
            move = move_tracker.cpu_move(p1, area)
            print(f"{p1.color} played {move}")
        else:
            chess_AI.InitializeAI(p2.engine, area)
            move = move_tracker.cpu_move(p2, area)
            print(f"{p2.color} played {move}")

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


