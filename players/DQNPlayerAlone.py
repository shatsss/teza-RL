import  random

import numpy as np

from players.DQN import DQN, WINDOW_SIZE, GRID_SIZE

NOT_LEGAL_STATE = np.expand_dims(np.full((WINDOW_SIZE * 2 + 1, WINDOW_SIZE * 2 + 1), -1), axis=2)
random.seed(1997)

def convert_data_to_state(current_location, graph):
    world = np.copy(graph.data)
    world[current_location[0], current_location[1]] = 2
    sub_world = np.zeros((WINDOW_SIZE * 2 + 1, WINDOW_SIZE * 2 + 1))
    for i in range(current_location[0] - WINDOW_SIZE, current_location[0] + WINDOW_SIZE + 1):
        for j in range(current_location[1] - WINDOW_SIZE, current_location[1] + WINDOW_SIZE + 1):
            if not (legal_location(i) and legal_location(j)):
                sub_world[i - (current_location[0] - WINDOW_SIZE), j - (current_location[1] - WINDOW_SIZE)] = -1
            else:
                sub_world[i - (current_location[0] - WINDOW_SIZE), j - (current_location[1] - WINDOW_SIZE)] = world[
                    i, j]
    return np.expand_dims(sub_world, axis=2)


def legal_location(location):
    return 0 <= location < GRID_SIZE


class DQNPlayerAlone:
    def __init__(self, grid_size, model=None):
        self.dqn = DQN(4, grid_size, model=model)
        self.graph = None

    def set_graph(self, graph):
        self.graph = graph

    def next_move(self, current_location):
        state = convert_data_to_state(current_location, self.graph)
        index = self.dqn.act(state)
        if index == 0:
            if current_location[0] - 1 >= 0:
                return (current_location[0] - 1, current_location[1]), index
            else:
                return current_location, index
        if index == 1:
            if current_location[1] + 1 < len(self.graph.data[0]):
                return (current_location[0], current_location[1] + 1), index
            else:
                return current_location, index

        if index == 2:
            if current_location[0] + 1 < len(self.graph.data):
                return (current_location[0] + 1, current_location[1]), index
            else:
                return current_location, index

        if index == 3:
            if current_location[1] - 1 >= 0:
                return (current_location[0], current_location[1] - 1), index
            else:
                return current_location, index
