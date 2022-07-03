from stockfish import Stockfish

# All customizable parameters for Stockfish
params = {
        "Debug Log File": "",
        "Contempt": 0,
        "Min Split Depth": 0,

        # More threads will make the engine stronger,
        # but should be kept at less than the number of logical processors on your computer.
        "Threads": 1,
        "Ponder": "false",

        # Default size is 16 MB. It's recommended that you increase this value,
        # but keep it as some power of 2.
        # E.g., if you're fine using 2 GB of RAM, set Hash to 2048 (11th power of 2).
        "Hash": 16,
        "MultiPV": 1,
        "Skill Level": 20,
        "Move Overhead": 10,
        "Minimum Thinking Time": 20,
        "Slow Mover": 100,
        "UCI_Chess960": "false",
        "UCI_LimitStrength": "true",
        "UCI_Elo": 1200
}

class Player:
    def __init__(self, color, wins, losses, engine=None):
        self.color = "WHITE" if color else "BLACK"
        self.bool_color = color
        self.wins = wins
        self.losses = losses
        self.engine = engine

    def add_win(self):
        """ Add a win to a player's record"""
        self.wins += 1
        return

    def add_loss(self):
        """ Add a loss to a player's record"""
        self.losses += 1
        return

    def InitializeStockfish(self):
        """ Initialize the Stockfish engine """
        pathname = "/Users/samdawley/Downloads/stockfish_15_linux_x64_bmi2/stockfish_15_src/src/stockfish"
        stockfish = Stockfish(
            path=pathname,
            depth=15,
            parameters=params
        )
        self.engine = stockfish
        return



