import sys
sys.path.append('..')

import common
import lib

if __name__ == '__main__':
    fpath = common.file_path('input.txt')
    four_last = lib.read_four_last(fpath)

    n_unique = lib.count_unique(four_last)
    assert n_unique == 274

    print(f'Number of unique: {n_unique}')
