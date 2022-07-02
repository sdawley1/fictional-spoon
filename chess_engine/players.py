class Player:
    def __init__(self, color, wins, losses):
        self.color = "white" if color else "black"
        self.wins = wins
        self.losses = losses

    def add_win(self):
        """ Add a win to a player's record"""
        self.wins += 1
        return

    def add_loss(self):
        """ Add a loss to a player's record"""
        self.losses += 1
        return

