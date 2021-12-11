import sys
import numpy as np

sys.path.append('..')

import common
import lib

def read_data(fpath):

    result = []

    with open(fpath) as f:
        for line in f:
            patterns, encoded_digits = lib.parse_line(line)
            unique_set = lib.UniqueSet()
            unique_set.find_unique(patterns)

            entrt = (unique_set.cases, encoded_digits)
            result.append(entrt)

    return result


if __name__ == '__main__':
    fpath = common.file_path('input.txt')
    data = read_data(fpath)

    numbers = []
    for cases, encoded_strings in data:
        mapping, _ = lib.decode(cases)
        digits = [lib.decode_intermediate_digit(lib.process_encoded_digit(s, mapping)) for s in encoded_strings]
        number = lib.digits_to_decimal(digits)
        numbers.append(number)

    result = np.sum(numbers)
    assert result == 1012089

    print(f'Result: {result}')
        
