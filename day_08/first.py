import sys
sys.path.append('..')

import common
import lib

if __name__ == '__main__':
    fpath = common.file_path('input.txt')
    four_last = lib.read_four_last(fpath)

    unique_res = lib.find_unique_in_all_last(four_last)
    assert unique_res.count == 274

    print(f'Number of unique: {unique_res.count}')
