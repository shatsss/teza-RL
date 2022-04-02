import numpy as np

from players.AbstractPlayer import AbstractPlayer
from players.DQN.DQN import DQN, GRID_SIZE, WINDOW_SIZE

# NOT_LEGAL_STATE = np.expand_dims(np.full((GRID_SIZE, GRID_SIZE), -1), axis=2)
#
#
NOT_LEGAL_STATE = np.expand_dims(np.full((WINDOW_SIZE * 2 + 1, WINDOW_SIZE * 2 + 1), -1), axis=2)


def convert_data_to_state(current_location, opponent_location, graph):
    world = np.copy(graph.get_combined_values_matrix())
    # set all values to 1 if we visited these cells
    # for i in range(world.size):
    #     value = 1 if world.item(i) > 0 else 0
    #     world.itemset(i, value)
    world[current_location[0], current_location[1]] = 20
    world[opponent_location[0], opponent_location[1]] = 10
    # return np.expand_dims(world, axis=2)
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


class DQNPlayer(AbstractPlayer):
    def __init__(self, id, model=None):
        super().__init__(id)
        self.dqn = DQN(4, model=model)

    def next_move(self, current_location, opponent_location=None):
        state = convert_data_to_state(current_location, opponent_location, self.graph)
        index = self.dqn.act(state)
        return self.get_next_location_according_to_index(current_location, index)
