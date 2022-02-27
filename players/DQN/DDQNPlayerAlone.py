import numpy as np

from players.AbstractPlayer import AbstractPlayer
from players.DQN.DDQN import DDQN
from players.DQN.DQN import GRID_SIZE

NOT_LEGAL_STATE = np.expand_dims(np.full((GRID_SIZE, GRID_SIZE), -1), axis=2)


# NOT_LEGAL_STATE = np.expand_dims(np.full((WINDOW_SIZE * 2 + 1, WINDOW_SIZE * 2 + 1), -1), axis=2)


# def convert_data_to_state(current_location, graph):
#     world = np.copy(graph.data)
#     world[current_location[0], current_location[1]] = 2
#     sub_world = np.zeros((WINDOW_SIZE * 2 + 1, WINDOW_SIZE * 2 + 1))
#     for i in range(current_location[0] - WINDOW_SIZE, current_location[0] + WINDOW_SIZE + 1):
#         for j in range(current_location[1] - WINDOW_SIZE, current_location[1] + WINDOW_SIZE + 1):
#             if not (legal_location(i) and legal_location(j)):
#                 sub_world[i - (current_location[0] - WINDOW_SIZE), j - (current_location[1] - WINDOW_SIZE)] = -1
#             else:
#                 sub_world[i - (current_location[0] - WINDOW_SIZE), j - (current_location[1] - WINDOW_SIZE)] = world[
#                     i, j]
#     return np.expand_dims(sub_world, axis=2)
def convert_data_to_state(current_location, graph):
    world = np.copy(graph.data)
    world[current_location[0], current_location[1]] = 2
    return np.expand_dims(world, axis=2)


def legal_location(location):
    return 0 <= location < GRID_SIZE


class DDQNPlayerAlone(AbstractPlayer):
    def __init__(self, grid_size, model=None):
        super().__init__()
        self.ddqn = DDQN(4, grid_size, model=model)

    def next_move(self, current_location):
        state = convert_data_to_state(current_location, self.graph)
        index = self.ddqn.act(state)
        return self.get_next_location_according_to_index(current_location, index)
