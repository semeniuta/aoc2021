import numpy as np

UNIQUE_LENGTHS = {
    2: 1,
    3: 7,
    4: 4,
    7: 8
}

INTERMEDIATE_TO_DIGIT = {
    (2, 1, 2, 1): 0,
    (2, 0, 0, 0): 1,
    (1, 1, 2, 1): 2,
    (2, 1, 1, 1): 3,
    (2, 0, 0, 2): 4,
    (1, 1, 1, 2): 5,
    (1, 1, 2, 2): 6,
    (2, 1, 0, 0): 7,
    (2, 1, 2, 2): 8,
    (2, 1, 1, 2): 9,
}

class UniqueSet:
    def __init__(self):
        self.count = 0
        self.cases = {}

    def find_unique(self, sequences):
    
        for seq in sequences:
            length = len(seq)
            if length in UNIQUE_LENGTHS.keys():
                self.count += 1
                number = UNIQUE_LENGTHS[length]
                self.cases[number] = seq


def parse_line(line):
    parts = line.split('|')
    return tuple(tuple(s.strip().split()) for s in parts)


def read_four_last(fpath):

    result = []
    with open(fpath) as f:
        for line in f:
            _, four_last = parse_line(line)
            result.append(four_last)

    return result


def find_unique_in_all_last(four_last):
    
    result = UniqueSet()
    
    for sequences in four_last:
        result.find_unique(sequences)

    return result


def decode(cases):

    sets = {number: set(cases[number]) for number in UNIQUE_LENGTHS.values()}

    top = sets[7] - sets[1]
    right = sets[1]
    left_top = sets[4] - sets[7]
    left_bottom = sets[8] - sets[4] - sets[7]

    res = {}

    parts = (right, top, left_bottom, left_top)
    for i, current_set in enumerate(parts):
        for value in current_set:
            res[value] = i

    return res, parts


def process_encoded_digit(encoded_str, mapping):

    res = np.zeros(4, dtype=int)
    mapped = [mapping[c] for c in encoded_str]

    for val in mapped:
        res[val] += 1

    return res


def decode_intermediate_digit(x):
    return INTERMEDIATE_TO_DIGIT[tuple(x)]


def digits_to_decimal(digits):
    res = 0
    n = len(digits)
    for i, d in enumerate(digits):
        power = n - i - 1
        res += d * (10 ** power)
    return res
