import random

import matplotlib.pyplot as plt
import numpy


class Graph:
    def __init__(self, grid_size, number_of_obstacles=0):
        self.data = numpy.zeros(shape=(grid_size, grid_size))
        self.grid_size = grid_size

    def set_visited(self, location):
        self.data[location[0]][location[1]] = 1

    def is_visited(self, location):
        return self.data[location[0]][location[1]] == 1

    def is_legal(self, location):
        return 0 <= location[0] < self.grid_size and 0 <= location[1] < self.grid_size

    def get_random_cell(self):
        x = random.randint(0, self.grid_size - 1)
        y = random.randint(0, self.grid_size - 1)
        return x, y

    def all_vertices_visited(self):
        number_of_elements = self.grid_size ** 2
        return all(self.data.item(i) == 1 for i in range(number_of_elements))

    def draw_graph(self):
        plt.imshow(self.data)
        plt.colorbar()
        plt.show()
