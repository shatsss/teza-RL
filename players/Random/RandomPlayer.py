import random

from players.AbstractPlayer import AbstractPlayer


class RandomPlayer(AbstractPlayer):
    def __init__(self, grid_size=None, model=None):
        super().__init__()

    def next_move(self, current_location):
        index = random.randint(0, 3)
        return self.get_next_location_according_to_index(current_location, index)
