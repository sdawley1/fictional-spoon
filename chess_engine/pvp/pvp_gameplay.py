import chess_AI
import move_tracker

def GameplayLoop(p1, p2, area):
    """
    Gameplay loop
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

    print()
    print("Let the game begin!")
    print(f"Player 1 will play {p1.color} and Player 2 will play {p2.color}.")
    print("All desired moves must be written in standard algebraic notation, e.g., 'e4', 'Nc6', or 'Qxf7'.")

    # Establish current outcome of game
    # This variable is updated whenever the end of the while loop is broken
    # i.e., test for termination before another loop begins in the while loop
    outcome = area.outcome()

    # Confirm game
    print()
    if input("Proceed? (y/n): ") == "y":
        # Here's a good spot to initialize the Stockfish engine!
        stockfish = chess_AI.BuildStockfish(depth=15, elo=1200)
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
        # Players making moves
        if move_tracker.whose_move(p1, p2, area) == p1.color:
            move = move_tracker.human_move(p1, area)
        else:
            move = move_tracker.human_move(p2, area)

        # Get board evaluation
        adv = move_tracker.get_stockfish_evaluation(stockfish)

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


