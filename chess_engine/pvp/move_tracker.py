def whose_move(p1, area):
    """ Determine whose turn it is to move in the game """
    board_move = area.turn # Bool. If White's turn to move, returns True
    if board_move == p1.bool_color:
        return "WHITE"
    else:
        return "BLACK"

def make_move(player, area):
    """
    Function to track human moves
    area (chess.Board()) = Playing board
    Return
    ------
    Move made by player (str)
    """
    while True:  # while loop to test for legality of moves
        move = input(f"Input move for {player.color}: ")
        try:
            # Push move and return it as a string using algebraic notation
            area.push_san(move)
            return move
        except ValueError:  # Catch if move is illegal
            print("ILLEGAL MOVE")


