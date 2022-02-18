from typing import Tuple

from players.AbstractPlayer import AbstractPlayer


class StcPlayer(AbstractPlayer):
    def __init__(self):
        super().__init__()
        self.map = {
            (0, 0)
        }

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

    def next_move(self, current_location: Tuple[float]):
        if current_location[0] % 2 == 0:
            if current_location[1] % 2 == 0:
                next_location = (current_location[0], current_location[1] - 1)
                next_location_in_same_sub_cell = (current_location[0] + 1, current_location[1])
                if all([not self.graph.is_visited(sub_node) for sub_node in
                        StcPlayer.__get_cells_of_big_node(next_location)]) or self.graph.is_visited(next_location_in_same_sub_cell):
                    return (current_location[0], current_location[1] - 1), None
                else:
                    return next_location_in_same_sub_cell, None

            else:
                next_location_in_same_sub_cell = (current_location[0], current_location[1] - 1)
                next_location = (current_location[0] - 1, current_location[1])
                if all([not self.graph.is_visited(sub_node) for sub_node in
                        StcPlayer.__get_cells_of_big_node(next_location)]) or self.graph.is_visited(next_location_in_same_sub_cell):
                    return (current_location[0] - 1, current_location[1]), None
                else:
                    return next_location_in_same_sub_cell, None
        else:
            if current_location[1] % 2 == 0:
                next_location_in_same_sub_cell = (current_location[0], current_location[1] + 1)
                next_location = (current_location[0] + 1, current_location[1])
                if all([not self.graph.is_visited(sub_node) for sub_node in
                        StcPlayer.__get_cells_of_big_node(next_location)]) or self.graph.is_visited(next_location_in_same_sub_cell):
                    return (current_location[0] + 1, current_location[1]), None
                else:
                    return next_location_in_same_sub_cell, None
            else:
                next_location_in_same_sub_cell = (current_location[0] - 1, current_location[1])
                next_location = (current_location[0], current_location[1] + 1)
                if all([not self.graph.is_visited(sub_node) for sub_node in
                        StcPlayer.__get_cells_of_big_node(next_location)]) or self.graph.is_visited(next_location_in_same_sub_cell):
                    return (current_location[0], current_location[1] + 1), None
                else:
                    return next_location_in_same_sub_cell, None
