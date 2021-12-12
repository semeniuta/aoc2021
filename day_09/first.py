import sys
import numpy as np
sys.path.append('..')
import common


def parse_line(line):
    line = line.strip()
    return np.array(list(map(int, line)), dtype=int)


def read_data(fpath):
    with open(fpath) as f:
        lines = np.array([parse_line(line) for line in f])
    return lines


class HeightMap:

    def __init__(self, height_data):
        self.heights = height_data
        self.rows, self.cols = height_data.shape

    def find_low_points(self):
        result = []
        for i in range(self.rows):
            for j in range(self.cols):
                if self.is_low_point(i, j):
                    result.append((i, j))
        return result

    def is_low_point(self, i, j):
        neighbors = self.get_neigbors(i, j)
        neighboring_values = np.array([self.heights[coord] for coord in neighbors], dtype=int)
        this_value = self.heights[i, j]
        return np.all(this_value < neighboring_values)

    def get_neigbors(self, i, j):
        
        coordinates = []

        up = (i - 1, j)
        down = (i + 1, j)
        left = (i, j - 1)
        right = (i, j + 1)

        for point in (up, down, left, right):
            y, x = point
            if y == -1 or y == self.rows:
                continue
            if x == -1 or x == self.cols:
                continue
            coordinates.append(point)

        return coordinates

    def sum_risk_levels(self, coordinates):

        s = 0
        for i, j in coordinates:
            s += self.heights[i, j] + 1
        
        return s


if __name__ == '__main__':

    fpath = common.file_path('input.txt')
    data = read_data(fpath)
    hmap = HeightMap(data)
    low_points = hmap.find_low_points()

    risk_sum = hmap.sum_risk_levels(low_points)
    assert risk_sum == 514

    print(f'Result: {risk_sum}')