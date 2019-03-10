import json


class LogicalGrid:
    def __init__(self):
        # Initialization of row and column
        self.row = 8
        self.column = 6

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
        with open('test_case.json', 'r') as f:
            data = json.load(f)

        # Change dead cells to alive cells corresponding to the json file
        for item in data:
            self.datas[item['x']][item['y']] = '*'
