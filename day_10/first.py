import sys
from collections import deque
sys.path.append('..')
import common

PAIRS = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

ILLEGAL_POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def read_data(fpath):
    with open(fpath) as f:
        return list(map(lambda s: s.strip(), f.readlines()))


def is_closing(c):
    return c in (')', ']', '}', '>')


class WrongLiteral(Exception):
    def __init__(self, expected, found):
        self.expected = expected
        self.found = found


class Validator:
    
    def __init__(self):
        self.stack = deque()

    def is_empty(self):
        return len(self.stack) == 0
    
    def update(self, c):
        
        if not is_closing(c):
            self.stack.append(c)
            return

        top = self.stack.pop()
        expected  = PAIRS[top]

        if c != expected:
            raise WrongLiteral(expected, c)
            


def validate(s, verbose=False):

    validator = Validator()
    
    for c in s:
        try:
            validator.update(c)
        except WrongLiteral as e:
            if verbose:
                print(f'{s}: wrong literal: expected {e.expected}, found {e.found}')
            return ILLEGAL_POINTS[e.found]

    return 0


if __name__ == '__main__':

    fpath = common.file_path('input.txt')
    data = read_data(fpath)

    score = 0
    for s in data:
        score_increment = validate(s, verbose=False)
        score += score_increment

    print(f'Total score: {score}')
