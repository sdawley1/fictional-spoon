def whose_move(p1, p2, area):
    """ Determine whose turn it is to move in the game """
    board_move = area.turn # Bool. If White's turn to move, returns True
    if board_move == p1.bool_color:
        return "PLAYER 1"
    else:
        return "PLAYER 2"

def cpu_move(player, area):
    """ Function which pushes and tracks moves made by AI """
    # Unlike before, I'm not worried about Stockfish returning an illegal move
    print(f"{player.color} is thinking...")
    move = player.engine.get_best_move() # This returns a string in UCI formatting
    area.push_uci(move)
    return move
