import numpy as np
from pathlib import Path


class Line:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

        self.max_x = max(self.p1[0], self.p2[0])
        self.max_y = max(self.p1[1], self.p2[1])
    
    def is_vertical(self):
        return self.p1[0] == self.p2[0]
    
    def is_horizontal(self):
        return self.p1[1] == self.p2[1]

    def is_horizontal_or_vertical(self):
        return self.is_horizontal() or self.is_vertical()

    def __repr__(self):
        return f'{self.p1} -> {self.p2}'


def file_path(basename):
    return  Path('.') / 'data' / basename


def parse_line(line_str):

    def parse_endpoint(s):
        a, b = s.split(',')
        return int(a), int(b)

    endpoints = line_str.split(' -> ')

    p1 = parse_endpoint(endpoints[0])
    p2 = parse_endpoint(endpoints[1])

    return Line(p1, p2)


def read_lines(fpath):

    selected_lines = []
    max_x = 0
    max_y = 0

    with open(fpath) as f:
        for line_str in f:
            line = parse_line(line_str)
            if line.is_horizontal_or_vertical():
                selected_lines.append(line)
                if line.max_x > max_x:
                    max_x = line.max_x
                if line.max_y > max_y:
                    max_y = line.max_y

    return selected_lines, max_x, max_y


def fill_field(selected_lines, max_x, max_y):

    field = np.zeros((max_y + 1, max_x + 1), dtype=int)

    for line in selected_lines:
        if line.is_horizontal():
            
            y = line.p1[1]
            x_from = min(line.p1[0], line.p2[0])
            x_to = max(line.p1[0], line.p2[0]) + 1
            field[y, x_from:x_to] += 1

        elif line.is_vertical:
            
            x = line.p1[0]
            y_from = min(line.p1[1], line.p2[1])
            y_to = max(line.p1[1], line.p2[1]) + 1
            field[y_from:y_to, x] += 1

    return field


if __name__ == '__main__':

    fpath = file_path('input.txt')
    selected_lines, max_x, max_y = read_lines(fpath)

    field = fill_field(selected_lines, max_x, max_y)

    result = np.sum(field >= 2)

    assert result == 4745

    print(f'Result: {result}')