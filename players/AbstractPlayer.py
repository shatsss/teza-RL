from abc import ABC, abstractmethod

from environment.Graph import Graph


class AbstractPlayer(ABC):
    def __init__(self, id):
        self.id = id
        self.graph: Graph = None

    def set_graph(self, graph: Graph):
        self.graph = graph

    @abstractmethod
    def next_move(self, current_location):
        pass

    def get_id(self):
        return self.id

    def get_next_location_according_to_index(self, current_location, index):
        if index == 0:
            if current_location[0] - 1 >= 0:
                next_location = (current_location[0] - 1, current_location[1]), index
            else:
                next_location = current_location, index
        elif index == 1:
            if current_location[1] + 1 < self.graph.grid_size:
                next_location = (current_location[0], current_location[1] + 1), index
            else:
                next_location = current_location, index

        elif index == 2:
            if current_location[0] + 1 < self.graph.grid_size:
                next_location = (current_location[0] + 1, current_location[1]), index
            else:
                next_location = current_location, index

        else:
            if current_location[1] - 1 >= 0:
                next_location = (current_location[0], current_location[1] - 1), index
            else:
                next_location = current_location, index
        return next_location
