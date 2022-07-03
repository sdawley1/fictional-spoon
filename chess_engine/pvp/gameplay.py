from move_tracker import whose_move, make_move

def GameplayLoop(p1, p2, area):
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
        # Players making moves
        if whose_move(p1, area) == p1.color:
            move = make_move(p1, area)
            print(f"{p1.color} played {move}")
        else:
            move = make_move(p2, area)
            print(f"{p2.color} played {move}")

        # Test termination condition
        outcome = area.outcome()

    # Return results of the match
    return outcome.termination, outcome.winner, outcome.result()


