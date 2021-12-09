import numpy as np
from pathlib import Path


def file_path(basename):
    return  Path('.') / 'data' / basename


def read_ages(fpath):
    with open(fpath) as f:
        line = f.readline()
        return list(map(int, line.split(',')))


def evolve(ages, n_days):

    for day in range(n_days):
        
        n_this_day = len(ages)
        for i in range(n_this_day):

            if ages[i] == 0:
                ages[i] = 6
                ages.append(8)
                continue

            ages[i] -= 1


def test():

    fpath = file_path('test_input.txt')
    ages_18 = read_ages(fpath)
    ages_80 = ages_18.copy()

    evolve(ages_18, n_days=18)
    evolve(ages_80, n_days=80)

    assert len(ages_18) == 26
    assert len(ages_80) == 5934


if __name__ == '__main__':

    test()

    fpath = file_path('input.txt')
    ages = read_ages(fpath)
    evolve(ages, n_days=80)

    print(f'Result: {len(ages)}')


