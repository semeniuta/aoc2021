import sys
import numpy as np
sys.path.append('..')
import common
import lib

if __name__ == '__main__':

    fpath = common.file_path('input.txt')
    data = lib.read_data(fpath)
    hmap = lib.HeightMap(data)
    low_points = hmap.find_low_points()

    risk_sum = hmap.sum_risk_levels(low_points)
    assert risk_sum == 514

    print(f'Result: {risk_sum}')