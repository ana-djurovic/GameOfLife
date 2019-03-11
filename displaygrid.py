#!/usr/bin/python3
from tkinter import Tk, Frame, Button, Canvas, ALL, TOP, BOTTOM, LEFT

from logicalgrid import LogicalGrid


class DisplayGrid:
    def __init__(self):
        # Initialization of datas
        self.logicalgrid = LogicalGrid()
        self.speed = 50
        self.cell_size = 10
        self.is_finish = True

        # Creation of the interface structure
        self.window = Tk()

        #  Grid frame
        self.grid = Frame(self.window)
        self.grid.pack(side=TOP, padx=10, pady=10)

        # Configuration frame
        self.config = Frame(self.window)
        self.config.pack(side=BOTTOM, padx=10, pady=10)

        # Canvas creation
        self.canvas = Canvas(
            self.grid,
            width=self.logicalgrid.row*self.cell_size,
            height=self.logicalgrid.column*self.cell_size,
            bg='white')
        self.canvas.pack(padx=5, pady=5)

        # Initialization of the interface
        self.create_grid()
        self.initialize()
        self.fill_grid()
        self.window.mainloop()

    def initialize(self):
        """Fill the grid and create button "Go" and "Stop" to start the game"""
        self.create_grid()
        button_go = Button(self.config, text="Go !", command=self.go)
        button_go.pack(side=LEFT, padx=3, pady=3)
        button_stop = Button(self.config, text="Stop", command=self.stop)
        button_stop.pack(side=LEFT, padx=3, pady=3)

    def fill_grid(self):
        """ Display of a grid corresponding to the datas"""
        for i in range(self.logicalgrid.row):
            for j in range(self.logicalgrid.column):
                if self.logicalgrid.datas[i][j] == '*':
                    self.canvas.create_rectangle\
                        (i*self.cell_size,
                         j*self.cell_size,
                         (i*self.cell_size)+self.cell_size,
                         (j*self.cell_size)+self.cell_size,
                         fill='black')
                elif self.logicalgrid.datas[i][j] == '.':
                    self.canvas.create_rectangle\
                        (i*self.cell_size,
                         j*self.cell_size,
                         (i*self.cell_size)+self.cell_size,
                         (j*self.cell_size)+self.cell_size,
                         fill='white')
                else:
                    raise Exception("Wrong cell value")

    def create_grid(self):
        """ Delete last canvas and create new one """
        self.canvas.delete(ALL)
        for x in range(0, self.logicalgrid.row*self.cell_size, self.cell_size):
            self.canvas.create_line(x, 0, x, self.logicalgrid.column*10, width=1, fill='black')
        for y in range(0, self.logicalgrid.column*self.cell_size, self.cell_size):
            self.canvas.create_line( 0, y, self.logicalgrid.row*10, y, width=1, fill='black')

    def play(self):
        """ Update grid datas """
        no_more_update = self.logicalgrid.update_datas()
        self.create_grid()
        self.fill_grid()
        if not self.is_finish or no_more_update:
            self.window.after(self.speed, self.play)

    def go(self):
        """ Start the game """
        if self.is_finish:
            self.is_finish = False
            self.play()

    def stop(self):
        """ Stop the game """
        self.is_finish = True

