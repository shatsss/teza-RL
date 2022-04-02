import random
from typing import Tuple

from players.AbstractPlayer import AbstractPlayer


class StcPlayerWithDeletingPheromones(AbstractPlayer):
    def __init__(self, id):
        super().__init__(id)

    @staticmethod
    def __get_cells_of_big_node(sub_node):
        if sub_node[0] % 2 == 0 and sub_node[1] % 2 == 0:
            return [sub_node, (sub_node[0] + 1, sub_node[1]), (sub_node[0], sub_node[1] + 1),
                    (sub_node[0] + 1, sub_node[1] + 1)]
        elif sub_node[0] % 2 == 0 and sub_node[1] % 2 == 1:
            return [sub_node, (sub_node[0], sub_node[1] - 1), (sub_node[0] + 1, sub_node[1]),
                    (sub_node[0] + 1, sub_node[1] - 1)]
        elif sub_node[0] % 2 == 1 and sub_node[1] % 2 == 0:
            return (sub_node, (sub_node[0] - 1, sub_node[1]), (sub_node[0], sub_node[1] + 1),
                    (sub_node[0] - 1, sub_node[1] + 1))
        else:
            return (sub_node, (sub_node[0] - 1, sub_node[1]), (sub_node[0], sub_node[1] - 1),
                    (sub_node[0] - 1, sub_node[1] - 1))

    def get_random_cell(self, location):
        possible_locations = [(location[0] - 1, location[1]), (location[0], location[1] - 1),
                              (location[0] + 1, location[1]), (location[0], location[1] + 1)]
        legal_locations = list(
            filter(lambda neighbor_location: self.graph.is_legal(neighbor_location), possible_locations))
        random_cell = random.randint(0, len(legal_locations) - 1)
        return legal_locations[random_cell], None

    def next_move(self, current_location: Tuple[float]):
        if current_location[0] % 2 == 0:
            if current_location[1] % 2 == 0:
                next_location = (current_location[0], current_location[1] - 1)
                next_location_in_same_sub_cell = (current_location[0] + 1, current_location[1])
                return self.get_next_location(current_location, next_location, next_location_in_same_sub_cell)

            else:
                next_location_in_same_sub_cell = (current_location[0], current_location[1] - 1)
                next_location = (current_location[0] - 1, current_location[1])
                return self.get_next_location(current_location, next_location, next_location_in_same_sub_cell)
        else:
            if current_location[1] % 2 == 0:
                next_location_in_same_sub_cell = (current_location[0], current_location[1] + 1)
                next_location = (current_location[0] + 1, current_location[1])
                return self.get_next_location(current_location, next_location, next_location_in_same_sub_cell)
            else:
                next_location_in_same_sub_cell = (current_location[0] - 1, current_location[1])
                next_location = (current_location[0], current_location[1] + 1)
                return self.get_next_location(current_location, next_location, next_location_in_same_sub_cell)

    def get_next_location(self, current_location, next_location, next_location_in_same_sub_cell):
        if (not self.graph.is_legal(next_location)) or self.graph.is_visited(next_location, self.id):
            if not self.graph.is_visited(next_location_in_same_sub_cell, self.id):
                return next_location_in_same_sub_cell, None
            else:
                return self.get_random_cell(current_location)
        else:
            if all([not self.graph.is_visited(sub_node, self.id) for sub_node in
                    StcPlayerWithDeletingPheromones.__get_cells_of_big_node(next_location)]) or \
                    self.graph.is_visited(next_location_in_same_sub_cell, self.id):
                return next_location, None
            else:
                return next_location_in_same_sub_cell, None
