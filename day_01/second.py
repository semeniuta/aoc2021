import numpy as np
from pathlib import Path


def sliding_sum(x, window_size):
    n = len(x) - window_size + 1
    return np.array([np.sum(x[i:i+window_size]) for i in range(n)])


def count_increases(x):
    return np.sum(np.diff(x) > 0)


if __name__ == '__main__':

    fname = Path('.') / 'data' / 'input.txt'
    measurements = np.loadtxt(fname, dtype=int)

    smooth = sliding_sum(measurements, 3)
    n_increases = count_increases(smooth)

    assert n_increases == 1748

    print(f'Result: {n_increases}')