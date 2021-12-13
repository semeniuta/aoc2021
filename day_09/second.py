import sys
import numpy as np
import heapq
sys.path.append('..')
import common
import lib

if __name__ == '__main__':

    fpath = common.file_path('input.txt')
    data = lib.read_data(fpath)
    hmap = lib.HeightMap(data)
    low_points = hmap.find_low_points()

    basins = [hmap.determine_basin(p) for p in low_points]
    basin_sizes = []
    for b in basins:
        heapq.heappush(basin_sizes, len(b))

    three_largest_sizes = heapq.nlargest(3, basin_sizes)
    product =  np.prod(three_largest_sizes)
    assert product == 1103130

    print(f'Result: {product}')