import random

import numpy

random.seed(1997)


class Graph:
    def __init__(self, number_of_rows, number_of_columns, number_of_obstacles=0):
        self.data = numpy.zeros(shape=(number_of_rows, number_of_columns))

    def set_visited(self, location):
        self.data[location[0]][location[1]] = 1

    def is_visited(self, location):
        return self.data[location[0]][location[1]] == 1

    def get_random_cell(self):
        x = random.randint(0, len(self.data) - 1)
        y = random.randint(0, len(self.data[x]) - 1)
        return x, y

    def all_vertices_visited(self):
        number_of_elements = len(self.data) * len(self.data[0])
        return all(self.data.item(i) == 1 for i in range(number_of_elements))
