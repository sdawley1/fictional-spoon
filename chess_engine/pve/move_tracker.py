def whose_move(human, cpu, area):
    """ Determine whose turn it is to move in the game """
    if area.turn == human.bool_color:
        return human.color
    else:
        return cpu.color

def human_move(human, area):
    """ Function which pushes and tracks moves made by human """
    while True:  # while loop to test for legality of moves
        move = input(f"Input move for {human.color}: ")
        try:
            area.push_san(move)
            return move # This function is great because it only allows legal moves
        except ValueError:  # Catch if move is illegal
            print("ILLEGAL MOVE")

def cpu_move(cpu, area):
    """ Function which pushes and tracks moves made by AI """
    # Unlike before, I'm not worried about Stockfish returning an illegal move
    print(f"{cpu.color} is thinking...")
    move = cpu.engine.get_best_move() # This returns a string in UCI formatting
    area.push_uci(move)
    return move # This function is great because it only allows legal moves
