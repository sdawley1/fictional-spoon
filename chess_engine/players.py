class Player:
    def __init__(self, color: bool, wins: float, losses: float) -> None:
        self.color = "white" if color else "black"
        self.wins = wins
        self.losses = losses
        return

    def add_win(self) -> None:
        """ Add a win to a player's record"""
        self.wins += 1
        return

    def add_loss(self) -> None:
        """ Add a loss to a player's record"""
        self.losses += 1
        return

