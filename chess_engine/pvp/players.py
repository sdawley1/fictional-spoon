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



