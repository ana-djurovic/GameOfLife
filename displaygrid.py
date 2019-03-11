#!/usr/bin/python3
from tkinter import Tk, Frame, Button, Label, Canvas, ALL

from logicalgrid import LogicalGrid


class DisplayGrid:
    def __init__(self):
        # Creation of the interface structure
        self.window = Tk()


        # Initialization of datas
        self.logicalgrid = LogicalGrid()

        self.canvas = Canvas(self.window, width=self.logicalgrid.row*10, height=self.logicalgrid.column*10, bg='white')
        self.canvas.pack(padx=5, pady=5)

        # Initialization of the interface
        self.create_grid()
        self.window.mainloop()

    def initialize(self):
        """Fill the grid and create button "Go" and "Stop" to start the game"""
        self.create_grid()
        button_go = Button(self.window, text="Go !", command=self.fill_grid)
        button_go.pack()
        button_stop = Button(self.window, text="Stop", command=self.stop)
        button_stop.pack()

    def fill_grid(self):
        """ Display of a grid corresponding to the datas"""
        for i in range(self.logicalgrid.row):
            for j in range(self.logicalgrid.column):
                if self.logicalgrid.datas[i][j] == '*':
                    self.canvas.create_rectangle(i*10, j*10, (i*10)+10, (j*10)+10, fill='black')
                elif self.logicalgrid.datas[i][j] == '.':
                    self.canvas.create_rectangle(i*10, j*10, (i*10)+10, (j*10)+10, fill='white')
                else:
                    raise Exception("Wrong cell value")

    def create_grid(self):
        self.canvas.delete(ALL)
        for x in range(0, self.logicalgrid.row*10, 10):
            self.canvas.create_line(x, 0, x, self.logicalgrid.column*10, width=1, fill='black')
        for y in range(0, self.logicalgrid.column*10, 10):
            self.canvas.create_line( 0, y, self.logicalgrid.row*10, y, width=1, fill='black')
        self.fill_grid()

    def update_grid(self):
        """Update grid datas"""
        while not self.logicalgrid.update_datas():
            self.create_grid()
            self.fill_grid()

    def stop(self):
        pass

