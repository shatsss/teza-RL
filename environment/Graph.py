import random

import matplotlib.pyplot as plt
import numpy as np


class Graph:
    def __init__(self, grid_size, number_of_obstacles=0):
        self.empty_array = np.zeros((grid_size, grid_size))
        self.data = {}
        self.grid_size = grid_size

    def set_visited(self, location, id):
        if id not in self.data.keys():
            self.data[id] = np.copy(self.empty_array)
        self.data[id][location[0]][location[1]] = id

    def is_visited(self, location, id):
        return id in self.data.keys() and self.data[id][location[0]][location[1]] == id

    def is_legal(self, location):
        return 0 <= location[0] < self.grid_size and 0 <= location[1] < self.grid_size

    def delete_opponent_pheromone(self, location, id):
        self.data[id][location[0]][location[1]] = 5

    def get_combined_values_matrix(self):
        combined = np.copy(self.empty_array)
        for value in self.data.values():
            combined += value
        return combined

    def get_visited_value_of_cell(self, location):
        combined = self.get_combined_values_matrix()
        return combined[location[0]][location[1]]

    def is_visited_by_any_robot(self, location):
        combined = self.get_combined_values_matrix()
        return combined[location[0]][location[1]] > 0

    def get_random_cell(self):
        x = random.randint(0, self.grid_size - 1)
        y = random.randint(0, self.grid_size - 1)
        return x, y

    def all_vertices_visited(self):
        number_of_elements = self.grid_size * self.grid_size
        combined = self.get_combined_values_matrix()
        return all(combined.item(i) > 0 for i in range(number_of_elements))

    def draw_graph(self, current_location, opponent_location):
        combined = (self.get_combined_values_matrix())
        combined[current_location[0], current_location[1]] = 20
        combined[opponent_location[0], opponent_location[1]] = 10
        plt.imshow(combined)
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                c = combined[j][i]
                plt.text(i, j, str(c), va='center', ha='center')
        plt.colorbar()
        plt.show()
