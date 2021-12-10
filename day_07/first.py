import numpy as np
from pathlib import Path


def file_path(basename):
    return  Path('.') / 'data' / basename


def read_numbers(fpath):
    with open(fpath) as f:
        line = f.readline()
        return np.array(list(map(int, line.split(','))))


def count_frequencies(numbers):
    freq = {}
    for x in numbers:
        if x not in freq:
            freq[x] = 1
        else:
            freq[x] += 1

    return freq


class Search:

    def __init__(self, numbers):

        self.max_val = numbers.max()
        self.min_val = numbers.min()

        size = self.max_val - self.min_val + 1
        self.scores = np.zeros(size, dtype=int)

    def search(self, freq):

        for dst in range(self.min_val, self.max_val + 1):
            score = 0
            for src, count in freq.items():
                distance = np.abs(src - dst)
                score += (distance * count)
            self.set_score(dst, score)

    def set_score(self, index, value):
        self.scores[index - self.min_val] = value

    def get_score(self, index):
        return self.scores[index - self.min_val]

    def argmin(self):
        internal_argmin = np.argmin(self.scores)
        return self.min_val + internal_argmin


if __name__ == '__main__':

    fpath = file_path('input.txt')
    numbers = read_numbers(fpath)
    freq = count_frequencies(numbers)

    search = Search(numbers)
    search.search(freq)

    result = search.argmin()
    result_score = search.get_score(result)
    
    assert result_score == 352707
    
    print(f'Result: {result} with score of {result_score}')