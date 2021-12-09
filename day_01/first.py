
import os
import numpy as np


def count_increases(measurements):
    differences = np.diff(measurements)
    return np.sum(differences > 0)


if __name__ == '__main__':

    data_file = os.path.join('data', 'input.txt')
    measurements = np.loadtxt(data_file, dtype=int)
    n_increases = count_increases(measurements)

    assert n_increases == 1722

    print(f'Result: {n_increases}')
