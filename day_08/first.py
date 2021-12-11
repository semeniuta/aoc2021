import sys
sys.path.append('..')

import common

UNIQUE_LENGTHS = set([2, 3, 4, 7])


def read_four_last(fpath):

    result = []
    with open(fpath) as f:
        for line in f:
            str_four_last = line.split('|')[-1].strip()
            four_last = tuple(str_four_last.split())
            result.append(four_last)

    return result


def count_unique(four_last):
    
    count = 0
    for entry in four_last:
        for seq in entry:
            if len(seq) in UNIQUE_LENGTHS:
                count += 1

    return count


if __name__ == '__main__':
    fpath = common.file_path('input.txt')
    four_last = read_four_last(fpath)

    n_unique = count_unique(four_last)
    assert n_unique == 274

    print(f'Number of unique: {n_unique}')
