"""
The Bomber man Game
https://www.hackerrank.com/challenges/bomber-man/problem

"""


class BomberMan(object):
    def __init__(self, row, col, n, grid):
        self.row = row
        self.col = col
        self.steps = n
        self.initial_grid = grid
        self.grid_list = self.grid_construct()

    def grid_construct(self):
        default_grid_lis = [[0 for c in range(self.col)] for r in range(self.row)]
        print(default_grid_lis, self.initial_grid)
        return default_grid_lis


if __name__ == "__main__":
    default_grid = ['.......', '...O...', '....O..', '.......', 'OO.....', 'OO.....']
    bomber = BomberMan(row=6, col=7, n=3, grid=default_grid)
