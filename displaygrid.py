#!/usr/bin/python3
from tkinter import Tk, Frame, Button, Label

from logicalgrid import LogicalGrid


class DisplayGrid:
    def __init__(self):
        # Creation of the interface structure
        self.window = Tk()
        self.grid = Frame(self.window)

        # Initialization of datas
        self.logicalgrid = LogicalGrid()

        # Initialization of the interface
        self.initialize()
        self.window.mainloop()

    def initialize(self):
        button = Button(self.window, text="Create grid", command=self.first_fill_grid)
        button.grid(row=0, column=1)
        self.grid.grid(row=1, columnspan=3)

    def fill_grid(self):
        """ Display of a grid corresponding to the datas"""
        for i in range(self.logicalgrid.row):
            for j in range(self.logicalgrid.column):
                value = self.logicalgrid.datas[i][j]
                cell = Label(self.grid, text=value)
                cell.grid(row=i, column=j)

    def update_grid(self):
        """Update grid datas"""
        while not self.logicalgrid.update_datas():
            self.fill_grid()

    def first_fill_grid(self):
        """Fill the grid and create button "Go" to start the game"""
        self.fill_grid()
        button = Button(self.window, text="Go !", command=self.update_grid)
        button.grid(row=2, column=1)
