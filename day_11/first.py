import sys
from collections import deque
import numpy as np
sys.path.append('..')
import common


def read_data(fpath):

    rows = []
    with open(fpath) as f:
        for line in f:
            numbers = list(map(int, line.strip()))
            rows.append(numbers)
    
    return np.array(rows, dtype=int)


class Process:

    def __init__(self, data):
        self.grid = data
        self.n_flashes = 0
        self.rows, self.cols = data.shape

    def get_neighbors(self, coord):
        i, j = coord
        
        coordinates = []

        candidates = (
            (i - 1, j),
            (i + 1, j),
            (i, j - 1),
            (i, j + 1),
            (i - 1, j - 1),
            (i + 1, j + 1),
            (i - 1, j + 1),
            (i + 1, j - 1)
        )

        for point in candidates:
            y, x = point
            if y == -1 or y == self.rows:
                continue
            if x == -1 or x == self.cols:
                continue
            coordinates.append(point)

        return coordinates

    def step(self):
        self.grid += 1

        flashed = self.grid > 9
        where_flashed = np.argwhere(flashed)

        q = deque()
        q.extend(map(tuple, where_flashed))

        while len(q) > 0:
            coord = q.pop()
            self.n_flashes += 1
            neighbors = self.get_neighbors(coord)
            for neigbor_coord in neighbors:
                if self.grid[neigbor_coord] > 9:
                    continue
                self.grid[neigbor_coord] += 1
                if self.grid[neigbor_coord] > 9:
                    q.append(neigbor_coord)

        self.grid[self.grid > 9] = 0

        
if __name__ == '__main__':

    fpath = common.file_path('input.txt')
    data = read_data(fpath)
    process = Process(data)

    for i in range(100):
        process.step()

    assert process.n_flashes == 1562

    print(f'Total flashes: {process.n_flashes}')