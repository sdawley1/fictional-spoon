import move_tracker
import chess_AI

def AIGameplay(human, cpu, area):
    """
    Gameplay loop with AI opponent
    Params
    ------
    human (players.Player) = White
    cpu (players.Player) = Black
    area (chess.Board) = Board to play on. Keeps track of pretty much everything
    Returns
    -------
    outcome.termination () = Reason that the game ended
    outcome.winner (bool) = Winner of game (WHITE == True, BLACK == False)
    outcome.result() (str) = Any of "1-0", "0-1", or "1/2-1/2" to denote outcome of game
    """
    # Get ELO of Stockfish to display
    cpu_elo = cpu.engine.get_parameters()["UCI_Elo"]

    print()
    print("Let the game begin!")
    print(f"The Human will play {human.color} and Stockfish (ELO: {cpu_elo}) will play {cpu.color}.")
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
        white = human.color if area.turn == human.bool_color else cpu.color
        # Keeping track of whose turn it is
        whose_move = area.turn
        # Print playing board
        print()
        print(f"MOVE {area.fullmove_number} ({'WHITE' if whose_move else 'BLACK'})")
        print("---------------")
        print(area)
        print("---------------")
        # This is for when the human needs to make a move
        if move_tracker.whose_move(human, cpu, area) == human.color:
            move = move_tracker.human_move(human, area)
            print(f"{human.color} played {move}")
        # This is for when the computer needs to make a move
        else:
            chess_AI.InitializeAI(cpu.engine, area) # Extra step to initialize engine to new position
            move = move_tracker.cpu_move(cpu, area)
            print(f"{cpu.color} played {move}")

        # Test termination condition
        outcome = area.outcome()

    # Return results of the match
    return outcome.termination, outcome.winner, outcome.result()


