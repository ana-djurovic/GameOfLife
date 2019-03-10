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
        button = Button(self.window, text="Create grid", command=self.fill_grid)
        button.grid(row=0, column=4)
        self.grid.grid(row=1, columnspan=5)

    def fill_grid(self):
        """ Display of a grid corresponding to the datas"""
        for i in range(self.logicalgrid.row):
            for j in range(self.logicalgrid.column):
                value = self.logicalgrid.datas[i][j]
                cell = Label(self.grid, text=value)
                cell.grid(row=i, column=j)
