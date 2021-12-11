UNIQUE_LENGTHS = {
    2: 1,
    3: 7,
    4: 4,
    7: 8
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