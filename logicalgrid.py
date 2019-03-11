import copy
import json


class LogicalGrid:
    def __init__(self):
        # Initialization of row and column
        self.row = 35
        self.column = 40
        self.enter_json_file = 'gilder_gun.json'

        # Initialization of empty grid
        self.datas = []
        self.initialize_empty_list_grid()

        # Fill the grid
        self.read_file_case()

    def initialize_empty_list_grid(self):
        """ Each empty grid cell take '.' value corresponding to an dead cell """
        for i in range(self.row):
            self.datas.append(['.'] * self.column)

    def read_file_case(self):
        # Load a json file into a list of alive cell
        with open(self.enter_json_file, 'r') as f:
            data = json.load(f)

        # Change dead cells to alive cells corresponding to the json file
        for item in data:
            self.datas[item['x']][item['y']] = '*'

    def update_datas(self):
        update_grid = copy.deepcopy(self.datas)

        for i in range(self.row):
            for j in range(self.column):
                value = self.datas[i][j]

                if value == '*':
                    self.update_alive_cell(i, j, update_grid)

                elif value == '.':
                    self.update_dead_cell(i, j, update_grid)
                else:
                    raise Exception("Wrong value in the datas")
        
        is_finish = False
        if update_grid == self.datas:
            is_finish = True
        self.datas = copy.deepcopy(update_grid)
        return is_finish

    def update_alive_cell(self, i, j, datas_to_update):
        """ Test if the alive cell must be changed"""
        alive_neighbours = self.count_neighbours(i, j)
        if alive_neighbours < 2 or alive_neighbours > 3:
            datas_to_update[i][j] = '.'

    def update_dead_cell(self, i, j, datas_to_update):
        """ Test if the dead cell must be changed"""
        alive_neighbours = self.count_neighbours(i, j)
        if alive_neighbours == 3:
            datas_to_update[i][j] = '*'

    def count_neighbours(self, i, j):
        """ Count number of neighbours alive """

        # Cell to check cases
        cells_to_check=[
            [i - 1, j - 1],
            [i - 1, j],
            [i - 1, j + 1],
            [i, j + 1],
            [i + 1, j + 1],
            [i + 1, j],
            [i + 1, j - 1],
            [i, j - 1]]

        positive_neighbours = 0
        for item in cells_to_check:
            if self.is_in_grid(item):
                # Test if the neighbour is in grid
                if self.datas[item[0]][item[1]] == "*":
                    positive_neighbours += 1

        return positive_neighbours

    def is_in_grid(self, item):
        """Verify if the item is  in grid"""
        in_grid = True

        if item[0] < 0 or item[1] < 0:
            in_grid = False
        elif item[0] > (self.row -1) or item[1] > (self.column-1):
            in_grid = False
        return in_grid

