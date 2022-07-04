from stockfish import Stockfish

def BuildStockfish(depth=15, elo=1200):
    """
    Function to build an arbitrary Stockfish engine. Used primarily for game evaluation in pvp mode.
    Returns a Stockfish engine based on stockfish.Stockfish()
    """
    pathname = "/Users/samdawley/Downloads/stockfish_15_linux_x64_bmi2/stockfish_15_src/src/stockfish"
    stockfish = Stockfish(
        path=pathname,
        depth=depth,
        parameters={"UCI_Elo": elo}  # Modifies ELO in addition to default params above
    )
    return stockfish

def InitializeAI(engine, area):
    """ Function to initialize chess engine on starting board (also validates starting position for fun) """
    if engine.is_fen_valid(area.fen()):
        engine.set_fen_position(area.fen())
        return
    else:
        raise Exception("INVALID STARTING POSITION.")

def PollStockfishMoves(engine, n):
    """
    Get top 3 moves from chess engine. Assumes engine is already initialized to board
    Params
    ------
    engine (i.e., stockfish.Stockfish()) = chess engine
    n (int) = number of moves to poll
    Returns
    ------
    list of dicts --> [{"Move":move, "Centipawn":centipawn, "Mate":1}, ...] (len is given by param 'n')
    """
    return engine.get_top_moves(n)

if __name__ == "__main__":
    ...
