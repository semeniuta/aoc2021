import numpy as np
from pathlib import Path


def file_path(basename):
    return  Path('.') / 'data' / basename


def parse_binary(binary_as_str):
    return np.array([True if char == '1' else False for char in binary_as_str], dtype=bool)


def read_data(fname):
    
    with open(file_path(fname)) as f:
        return np.array([parse_binary(line.strip()) for line in f])


def binary_array_to_int(x):
    
    result = 0
    for i, value in enumerate(reversed(x)):
        if value:
            result += (2 ** i)

    return result


def find_common(data):
    n_rows = data.shape[0]
    n_true = np.sum(data, axis=0)
    
    threshold = n_rows - n_rows // 2
    return n_true >= threshold

