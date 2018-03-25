"""
The Bomber man Game
https://www.hackerrank.com/challenges/bomber-man/problem

"""
#!/bin/python3

import sys


class BomberMan(object):
    def __init__(self, row, col, n, grid):
        self.row = row
        self.col = col
        self.steps = n
        self.initial_grid = grid
        self.grid_list = []
        self.grid = []

    def grid_construct(self):
        """
        matrix approach of grid construction
        pros:
        implementation : easy
        cons:
        space complexity: high
        time to lookup : high
        :return: integer matrix of given grid of string
        """
        default_grid_lis = [[0 for c in range(self.col)] for r in range(self.row)]
        for row in range(len(self.initial_grid)):
            for col in range(len(self.initial_grid[row])):
                if self.initial_grid[row][col].strip() == 'O':
                    default_grid_lis[row][col] = 3
        return default_grid_lis

    def plant(self):
        """ plant the bombs for grid matrix """
        for row in range(self.row):
            for col in range(self.col):
                if self.grid_list[row][col] == 0:
                    self.grid_list[row][col] = 3
                elif self.grid_list[row][col] > 0:
                    self.grid_list[row][col] -= 1

    def explode(self, row, col):
        """ explode bombs recursively in grid matrix """
        # print("exploding bomb at {} {}".format(row, col))
        for i in range(-1, 2, 2):
            if 0 < row+i < self.row:
                if self.grid_list[row+i][col] == 1:
                    self.grid_list[row + i][col] = 0
                    self.explode(row+i, col)
                else:
                    self.grid_list[row+i][col] = 0
            if 0 < col+i < self.col:
                if self.grid_list[row][col+i] == 1:
                    self.grid_list[row][col + i] = 0
                    self.explode(row, col+i)
                else:
                    self.grid_list[row][col+i] = 0

    def iterative_explode(self, row, col):
        if row - 1 > 0:
            self.grid_list[row-1][col] = 0
        if col - 1 > 0:
            self.grid_list[row][col-1] = 0
        # for i in range(row, self.row+1):
        i, c = row, col
        while i < self.row:
            self.grid_list[i][col] = 0
            if i+1 < self.row:
                if self.grid_list[i+1][col] != 1:
                    break
            i += 1
        while c < self.col:
            self.grid_list[row][c] = 0
            if c+1 < self.col:
                if self.grid_list[row][c+1] != 1:
                    break
            c += 1

    def hold_explode(self, flag="explode"):
        for row in range(self.row):
            for col in range(self.col):
                if self.grid_list[row][col] > 0:
                    self.grid_list[row][col] = self.grid_list[row][col] - 1
                    if self.grid_list[row][col] == 0 and flag == "explode":
                        self.iterative_explode(row, col)

    def bombing_sequence(self):
        """
        After one second, Bomber man does nothing
        After one more second, Bomber man plants bombs in all cells without bombs, thus filling the whole grid with bombs.
            It is guaranteed that no bombs will detonate at this second.
        After one more second, any bombs planted exactly three seconds ago will detonate.
            Here, Bomber man stands back and observes.
        """
        flag = 0
        for i in range(1, self.steps+1):
            if flag == 0:
                if i == 1:
                    self.grid_list = self.grid_construct()
                    self.hold_explode()
                else:
                    self.hold_explode()
                flag = 1
                continue
            elif flag == 1:
                self.plant()
                flag = 0
                continue
        return True

    def display_grid(self):
        if self.bombing_sequence():
            for row in range(self.row):
                for col in range(self.col):
                    if self.grid_list[row][col] == 0:
                        self.grid_list[row][col] = '.'
                    elif self.grid_list[row][col] > 0:
                        self.grid_list[row][col] = 'O'
                self.grid.insert(row, ''.join(self.grid_list[row]))
        # print(self.grid_list)
        return self.grid


if __name__ == "__main__":
    default_grid = ['.......', '...O...', '....O..', '.......', 'OO.....', 'OO.....']
    bomber = BomberMan(row=6, col=7, n=3, grid=default_grid)
    print("\n".join(map(str, bomber.display_grid())))
