def InitializeAI(engine, area):
    """ Function to initialize chess engine on starting board (also validates starting position for fun) """
    if engine.is_fen_valid(area.fen()):
        engine.set_fen_position(area.fen())
        return
    else:
        raise Exception("INVALID STARTING POSITION.")